from aiogram.types import CallbackQuery
from aiogram import Router
from bot.keyboards.inline_kb.select_inline_kb import select_kb
from bot.keyboards.inline_save.select_table import select_table_kb
from bot.utils.callbackdata import Start, Select


router_start = Router()

@router_start.callback_query(Start.filter())
async def call_start(call: CallbackQuery, callback_data: Start):
    # name = callback_data.full_name
    start = callback_data.choice
    if start == 'start':
        await call.message.answer(f"{call.from_user.full_name}, Выбери действие", reply_markup=select_kb())
    else:
        await call.message.answer(f"{call.from_user.full_name}, инструкция пока не доступна")


@router_start.callback_query(Select.filter())
async def call_select(call: CallbackQuery, callback_data: Select):
    # name = callback_data.name
    select = callback_data.select
    if select == "save":
        await call.message.answer(f"{call.from_user.full_name}, выбери таблицу для внесения данных",
                                  reply_markup=select_table_kb())
    elif select == "view":
        await call.message.answer(f"{call.from_user.full_name}, данные")
    elif select == "edit":
        await call.message.answer(f"{call.from_user.full_name}, редактировать данные")
    elif select == "delete":
        await call.message.answer(f"{call.from_user.full_name}, удалить данные")


