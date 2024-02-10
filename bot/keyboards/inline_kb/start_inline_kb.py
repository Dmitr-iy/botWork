from aiogram.utils.keyboard import InlineKeyboardBuilder
from bot.utils.callbackdata import Start


def start_kb(full_name=""):
    builder = InlineKeyboardBuilder()

    builder.button(
        text="Начать",
        callback_data=Start(full_name=full_name, choice="start").pack()
    )

    builder.button(
        text="Инструкции",
        callback_data=Start(full_name=full_name, choice="help").pack()
    )
    return builder.as_markup()
