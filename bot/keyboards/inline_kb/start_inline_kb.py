from aiogram.utils.keyboard import InlineKeyboardBuilder


def start_kb(full_name=""):
    builder = InlineKeyboardBuilder()

    builder.button(
        text="Начать",
        callback_data=f"start:{full_name}".format(full_name=full_name)
    )

    builder.button(
        text="Инструкции",
        callback_data=f"help:{full_name}".format(full_name=full_name)
    )
    return builder.as_markup()
