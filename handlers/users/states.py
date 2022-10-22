from aiogram.dispatcher.filters.state import StatesGroup, State


class FSMProf(StatesGroup):
    prof_duration_choise = State()
    prof_pay = State()
    trial = State()
    extension = State()
    full_month = State()


class FSMPrem(StatesGroup):
    prem_pay = State()
    prem_paid = State()


class FSMComposite(StatesGroup):
    composite_pay = State()
    composite_paid = State()


class FSMTop(StatesGroup):
    top_pay = State()
    top_paid = State()


class FSMTotalDom(StatesGroup):
    total_dom_pay = State()
    total_dom_paid = State()


class FSMOzon(StatesGroup):
    ozon_pay = State()
    ozon_paid = State()