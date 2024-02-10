from aiogram.utils.keyboard import InlineKeyboardBuilder
from bot.utils.callbackdata import Select


def select_kb(name):
    builder = InlineKeyboardBuilder()

    builder.button(
        text="Внести данные",
        callback_data=Select(select="save", name=name).pack()
    )

    builder.button(
        text="Посмотреть данные",
        callback_data=Select(select="view", name=name).pack()
    )

    builder.button(
        text="Редактировать данные",
        callback_data=Select(select="edit", name=name).pack()
    )

    builder.button(
        text="Удалить данные",
        callback_data=Select(select="delete", name=name).pack()
    )

    builder.adjust(2, 1)

    return builder.as_markup()
