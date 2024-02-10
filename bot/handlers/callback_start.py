from aiogram.types import CallbackQuery

from bot.keyboards.inline_kb.select_inline_kb import select_kb


async def call_start(call: CallbackQuery):
    name = call.data.split(":")[1]
    start = call.data.split(":")[0]
    if start == 'start':
        await call.message.answer(f"{name}, Выбери действие", reply_markup=select_kb(name=name))
    else:
        await call.message.answer(f"{name}, инструкция пока не доступна")

