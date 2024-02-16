from aiogram.filters.callback_data import CallbackData


class Start(CallbackData, prefix='start'):
    choice: str
    # full_name: str


class Select(CallbackData, prefix='select'):
    select: str
    # name: str

class Save(CallbackData, prefix='save'):
    # name: str
    table: str
