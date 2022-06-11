from aiogram.dispatcher.filters.state import StatesGroup, State


class FSMProf(StatesGroup):
    prof_pay_and_get = State()
    prof_pay_choise = State()
    prof_pay_2800_any = State()
    prof_pay_2800_sbor = State()
