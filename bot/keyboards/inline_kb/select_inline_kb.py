from aiogram.utils.keyboard import InlineKeyboardBuilder
from bot.utils.callbackdata import Select


def select_kb():
    builder = InlineKeyboardBuilder()

    builder.button(
        text="Внести данные",
        callback_data=Select(select="save").pack()
    )

    builder.button(
        text="Посмотреть данные",
        callback_data=Select(select="view").pack()
    )

    builder.button(
        text="Редактировать данные",
        callback_data=Select(select="edit").pack()
    )

    builder.button(
        text="Удалить данные",
        callback_data=Select(select="delete").pack()
    )

    builder.adjust(2, 1)

    return builder.as_markup()
