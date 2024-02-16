from aiogram.fsm.state import StatesGroup, State


class SaveObject(StatesGroup):
    name_work = State()
    data_start = State()
    yes_no = State()
    data_finish = State()
    work_price = State()
    save_cancelled = State()
    not_save = State()

class SaveWorkers(StatesGroup):
    name_workers = State()
    name_objects = State()
    salary = State()
    days = State()


