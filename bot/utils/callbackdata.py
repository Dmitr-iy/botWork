from aiogram.filters.callback_data import CallbackData


class Start(CallbackData, prefix='start'):
    choice: str


class Select(CallbackData, prefix='select'):
    select: str


class Save(CallbackData, prefix='save'):
    table: str
