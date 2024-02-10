from aiogram.filters.callback_data import CallbackData


class Start(CallbackData, prefix='start'):
    start: str
    help: str
    full_name: str
