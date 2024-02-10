from aiogram.filters import CommandStart
from aiogram.types import CallbackQuery
from aiogram import Router
import os
from aiogram.types import Message
from bot.keyboards.inline_kb.select_inline_kb import select_kb
from bot.keyboards.inline_save.select_table import select_table_kb
from bot.utils.callbackdata import Start, Select
from bot.keyboards.inline_kb.start_inline_kb import start_kb
from data.dbconnect import Request


router_start = Router()

@router_start.message(CommandStart())
async def get_start(message: Message, request: Request):
    allowed_chat_ids = [int(chat_id) for chat_id in os.environ.get('allowed_chat_ids', '').split(',')]
    chat_id = message.chat.id
    if chat_id in allowed_chat_ids:
        await request.add_data(message.from_user.id, message.from_user.full_name)
        await message.answer(f"Привет{message.from_user.full_name}, для начала работы нажми начать."
                             f" Для ознакомления с инструкциями нажми инструкции.",
                             reply_markup=start_kb(message.from_user.full_name))
    else:
        await message.answer("У вас нет доступа к этому боту.")


@router_start.callback_query(Start.filter())
async def call_start(call: CallbackQuery, callback_data: Start):
    name = callback_data.full_name
    start = callback_data.choice
    if start == 'start':
        await call.message.answer(f"{name}, Выбери действие", reply_markup=select_kb(name=name))
    else:
        await call.message.answer(f"{name}, инструкция пока не доступна")


@router_start.callback_query(Select.filter())
async def call_select(call: CallbackQuery, callback_data: Select):
    name = callback_data.name
    select = callback_data.select
    if select == "save":
        await call.message.answer(f"{name}, выбери таблицу для внесения данных",
                                  reply_markup=select_table_kb(name=name))
    elif select == "view":
        await call.message.answer(f"{name}, данные")
    elif select == "edit":
        await call.message.answer(f"{name}, редактировать данные")
    elif select == "delete":
        await call.message.answer(f"{name}, удалить данные")


