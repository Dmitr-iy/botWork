from aiogram.utils.keyboard import InlineKeyboardBuilder
from bot.utils.callbackdata import Save


def select_table_kb():
    builder = InlineKeyboardBuilder()
    builder.button(
        text="Объект",
        callback_data=Save(table="'объект'").pack()
    )

    builder.button(
        text="Рабочие",
        callback_data=Save(table="'рабочие'").pack()
    )

    builder.button(
        text="Вложения",
        callback_data=Save(table="'вложения'").pack()
    )

    builder.button(
        text="Расходы",
        callback_data=Save(table="'расходы'").pack()
    )

    builder.button(
        text="Прибыль",
        callback_data=Save(table="'прибыль'").pack()
    )

    builder.button(
        text="Инструмент",
        callback_data=Save(table="'инструмент'").pack()
    )

    builder.button(
        text="Необходимый инструмент",
        callback_data=Save(table="'необходимый инструмент'").pack()
    )

    builder.adjust(2, 2, 2)

    return builder.as_markup()
