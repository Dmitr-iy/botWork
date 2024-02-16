from aiogram.utils.keyboard import InlineKeyboardBuilder


def select_change():
    builder = InlineKeyboardBuilder()
    builder.button(
        text="название объекта",
        callback_data=f"name_object"
    )

    builder.button(
        text="дата начала",
        callback_data=f"date_start"
    )

    builder.button(
        text="дата окончания",
        callback_data=f"date_finish"
    )

    builder.button(
        text="стоимость объекта",
        callback_data=f"price"
    )

    builder.button(
        text="к выбору таблицы",
        callback_data=f"select_table"
    )
    builder.adjust(2, 2)
    return builder.as_markup()

def replay():
    builder = InlineKeyboardBuilder()
    builder.button(
        text="К выбору действий",
        callback_data=f"change"
    )

    builder.button(
        text="К выбору таблицы",
        callback_data=f"table"
    )

    builder.button(
        text="Закончить",
        callback_data=f"end"
    )
    return builder.as_markup()
