import os
from aiogram.types import Message
from data.dbconnect import Request


async def get_start(message: Message, request: Request):
    allowed_chat_ids = [int(chat_id) for chat_id in os.environ.get('allowed_chat_ids', '').split(',')]

    chat_id = message.chat.id
    if chat_id in allowed_chat_ids:
        await request.add_data(message.from_user.id, message.from_user.full_name)
        await message.answer("Привет, разрешенный пользователь!")
    else:
        await message.answer("У вас нет доступа к этому боту.")
