from aiogram.utils.keyboard import InlineKeyboardBuilder


def select_kb(name):
    builder = InlineKeyboardBuilder()

    builder.button(
        text="Внести данные",
        callback_data=f"save:{name}"
    )

    builder.button(
        text="Посмотреть данные",
        callback_data=f"view:{name}"
    )

    builder.button(
        text="Редактировать данные",
        callback_data=f"edit:{name}"
    )

    builder.button(
        text="Удалить данные",
        callback_data=f"delete:{name}"
    )

    builder.adjust(2, 1)

    return builder.as_markup()
