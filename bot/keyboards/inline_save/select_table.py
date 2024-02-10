from aiogram.utils.keyboard import InlineKeyboardBuilder


def select_table_kb(name):
    builder = InlineKeyboardBuilder()

    builder.button(
        text="Объект",
        callback_data=f"save:{name}"
    )

    builder.button(
        text="Рабочие",
        callback_data=f"view:{name}"
    )

    builder.button(
        text="Вложения",
        callback_data=f"edit:{name}"
    )

    builder.button(
        text="Расходы",
        callback_data=f"edit:{name}"
    )

    builder.button(
        text="Прибыль",
        callback_data=f"delete:{name}"
    )

    builder.button(
        text="Инструмент",
        callback_data=f"edit:{name}"
    )

    builder.button(
        text="Необходимый инструмент",
        callback_data=f"edit:{name}"
    )

    builder.adjust(2, 2, 2)

    return builder.as_markup()
