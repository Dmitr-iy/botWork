from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from bot.utils.callbackdata import Save
from bot.utils.class_state import SaveObject

router_save = Router()

@router_save.callback_query(Save.filter())
async def call_save(call: CallbackQuery, callback_data: Save, state: FSMContext):
    name = call.from_user.full_name
    table = callback_data.table
    if table == "'объект'":
        await call.message.answer(f"{name}, Выбрана таблица {table}, можно записать данные о "
                                  f"'названии объекта', 'начале объекта', 'окончании', 'стоимости'."
                                  f" Сначала введи название объекта:")
        await state.set_state(SaveObject.name_work)
    elif table == "'рабочие'":
        await call.message.answer(f"{name}, Выбрана таблица {table}, можно записать данные о "
                                  f"'Фамилия И.О.', 'названии объекта', 'ЗП', 'количество дней'. "
                                  f"Сначала введи название объекта:")
    elif table == "'вложения'":
        await call.message.answer(f"{name}, Выбрана таблица {table}")
    elif table == "'расходы'":
        await call.message.answer(f"{name}, Выбрана таблица {table}")
    elif table == "'прибыль'":
        await call.message.answer(f"{name}, Выбрана таблица {table}")
    elif table == "'инструмент'":
        await call.message.answer(f"{name}, Выбрана таблица {table}")
    else:
        await call.message.answer(f"{name}, Выбрана таблица {table}")


