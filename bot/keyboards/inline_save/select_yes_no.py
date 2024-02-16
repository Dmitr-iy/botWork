from aiogram.utils.keyboard import InlineKeyboardBuilder


def select_yes_no():
    builder = InlineKeyboardBuilder()
    builder.button(
        text="Да",
        callback_data=f"yes"
    )

    builder.button(
        text="Нет",
        callback_data=f"no"
    )
    return builder.as_markup()

def yes_cancel():
    builder = InlineKeyboardBuilder()
    builder.button(
        text="Да",
        callback_data=f"next"
    )

    builder.button(
        text="Нет",
        callback_data=f"cancel"
    )
    return builder.as_markup()
