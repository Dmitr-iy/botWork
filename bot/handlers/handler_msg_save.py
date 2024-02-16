from aiogram import Router, Bot
from aiogram.fsm.context import FSMContext
import datetime
from aiogram.types import Message, CallbackQuery
import re

from bot.keyboards.inline_kb.select_inline_kb import select_kb
from bot.keyboards.inline_save.change import select_change, replay
from bot.keyboards.inline_save.select_table import select_table_kb
from bot.keyboards.inline_save.select_yes_no import select_yes_no, yes_cancel
from bot.utils.class_state import SaveObject
from data.dbconnect import Request

router_save_msg = Router()

@router_save_msg.message(SaveObject.name_work)
async def msg_work_object(message: Message, bot: Bot, state: FSMContext, request: Request):
    name_work = message.text
    existing_names = await request.get_existing_names()
    if name_work in existing_names:
        await bot.send_message(message.from_user.id, "Это название объекта уже существует."
                                                     " Пожалуйста, введи другое название.")
    else:
        await state.update_data(name_work=name_work)
        await bot.send_message(message.from_user.id, "Введи дату начала в формате ГГГГ-ММ-ДД")
        await state.set_state(SaveObject.data_start)


@router_save_msg.message(SaveObject.data_start)
async def msg_start_date(message: Message, bot: Bot, state: FSMContext):
    start_date_str = message.text
    try:
        start_date = datetime.datetime.strptime(start_date_str, "%d.%m.%Y").strftime("%Y-%m-%d")
        await state.update_data(data_start=start_date)
        await bot.send_message(message.from_user.id, f"дата окончания известна?", reply_markup=select_yes_no())
        await state.set_state(SaveObject.yes_no)
    except ValueError:
        await bot.send_message(message.from_user.id,
                               "Неправильный формат даты. Введи дату начала в формате ГГГГ-ММ-ДД")


@router_save_msg.callback_query(SaveObject.yes_no)
async def call_start_date(call: CallbackQuery, state: FSMContext):
    await state.update_data(yes_no=call.data)
    yes = call.data
    if yes == 'yes':
        await call.message.answer(f"Введи дату окончания в формате ГГГГ-ММ-ДД")
        await state.set_state(SaveObject.data_finish)
    else:
        await call.message.answer(f"Введи стоимость объекта")
        await state.set_state(SaveObject.work_price)


@router_save_msg.message(SaveObject.data_finish)
async def msg_finish_date(message: Message, bot: Bot, state: FSMContext):
    finish_date_str = message.text
    try:
        finish_date = datetime.datetime.strptime(finish_date_str, "%d.%m.%Y").strftime("%Y-%m-%d")

        try:
            get_data = await state.get_data()
            data_start = datetime.datetime.strptime(get_data.get('data_start'), "%Y-%m-%d")
            data_finish = datetime.datetime.strptime(finish_date, "%Y-%m-%d")

            if data_finish >= data_start:
                await state.update_data(data_finish=finish_date)
                await bot.send_message(message.from_user.id, f"Введи стоимость объекта")
                await state.set_state(SaveObject.work_price)
            else:
                await bot.send_message(message.from_user.id, "Дата окончания должна быть позже или равна дате начала.")
                await state.set_state(SaveObject.data_finish)
        except ValueError:
            await bot.send_message(message.from_user.id, 'Ошибка при обработке дат. Пожалуйста, попробуйте еще раз.')
    except ValueError:
        await bot.send_message(message.from_user.id,
                               "Неправильный формат даты. Введи дату окончания в формате ГГГГ-ММ-ДД")


@router_save_msg.message(SaveObject.work_price)
async def msg_price_object(message: Message, bot: Bot, state: FSMContext):
    price_str = message.text
    if re.match(r'^\d+(\.\d+)?$', price_str):
        price = float(price_str)
        print("Price", price)
        await state.update_data(work_price=price)
        get_data = await state.get_data()
        print(get_data)
        name_object = get_data.get('name_work')
        start_date = get_data.get('data_start')
        finish_date = get_data.get('data_finish')
        price_object = get_data.get('work_price')
        if finish_date is not None:
            data_object = f"Сохраняем эти данные ?\n" \
                          f"Имя объекта: {str(name_object)}\n" \
                          f"Название объекта: {str(name_object)}\n" \
                          f"Дата начала: {str(start_date)}\n" \
                          f"Дата окончания: {str(finish_date)}\n" \
                          f"Стоимость объекта: {str(price_object)}"
        else:
            data_object = f"Сохраняем эти данные ?\n" \
                          f"Название объекта: {str(name_object)}\n" \
                          f"Дата начала: {str(start_date)}\n" \
                          f"Стоимость объекта: {str(price_object)}"
        await bot.send_message(message.from_user.id, data_object, reply_markup=yes_cancel())
        await state.set_state(SaveObject.save_cancelled)
    else:
        await bot.send_message(message.from_user.id, "Неправильный формат цены. Введите цену в виде числа.")


@router_save_msg.callback_query(SaveObject.save_cancelled)
async def call_save_cancelled(call: CallbackQuery, state: FSMContext, request: Request):
    cancel = call.data
    if cancel == 'next':
        data = await state.get_data()
        name_work = data.get('name_work')
        data_start = data.get('data_start')
        data_finish = data.get('data_finish')
        work_price = data.get('work_price')
        if data_finish is not None:
            await request.save_object(name_work, work_price, data_start, data_finish)
        else:
            await request.save_object_not_finish_data(name_work, work_price, data_start)
        await call.message.answer(f"Сохранено", reply_markup=replay())
        await state.clear()
    else:
        await call.message.answer(f"Сохранение данных отменено. Что нужно изменить?", reply_markup=select_change())
        await state.set_state(SaveObject.not_save)

@router_save_msg.callback_query()
async def call_save(call: CallbackQuery):
    option = call.data
    if option == 'change':
        await call.message.answer(f"К выбору действий", reply_markup=select_kb())
    elif option == 'table':
        await call.message.answer(f"К выбору таблицы", reply_markup=select_table_kb())
    else:
        await call.message.answer(f"end")


@router_save_msg.callback_query(SaveObject.not_save)
async def call_save_cancel(call: CallbackQuery, state: FSMContext):
    calls = call.data
    user = call.from_user.full_name
    if calls == 'name_object':
        await call.message.answer(f"Введи название объекта")
        await state.set_state(SaveObject.name_work)
    elif calls == 'date_start':
        await call.message.answer(f"Введи дату начала в формате ГГГГ-ММ-ДД")
        await state.set_state(SaveObject.data_start)
    elif calls == 'date_finish':
        await call.message.answer(f"Введи дату окончания в формате ГГГГ-ММ-ДД")
        await state.set_state(SaveObject.data_finish)
    elif calls == 'price':
        await call.message.answer(f"Введи стоимость объекта")
        await state.set_state(SaveObject.work_price)
    else:
        await call.message.answer(f"{user}, выбери таблицу для внесения данных",
                                  reply_markup=select_table_kb())
        await state.clear()





