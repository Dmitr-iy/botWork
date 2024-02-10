from aiogram.types import CallbackQuery


async def call_select(call: CallbackQuery):
    name = call.data.split(":")[1]
    select = call.data.split(":")[0]

    if select == "save":
        await call.message.answer(f"{name}, внесите данные")
    elif select == "view":
        await call.message.answer(f"{name}, данные")
    elif select == "edit":
        await call.message.answer(f"{name}, редактировать данные")
    elif select == "delete":
        await call.message.answer(f"{name}, удалить данные")
