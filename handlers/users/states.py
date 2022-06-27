from aiogram.dispatcher.filters.state import StatesGroup, State


class FSMProf(StatesGroup):
    prof_pay_and_get = State()
    prof_pay_choise = State()
    prof_paid = State()


class FSMPrem(StatesGroup):
    prem_pay_and_get = State()
    prem_pay_choise = State()
    prem_paid = State()

    
class FSMComposite(StatesGroup):
    composite_pay_and_get = State()
    composite_pay_choise = State()
    composite_paid = State()


class FSMTop(StatesGroup):
    top_pay_and_get = State()
    top_pay_choise = State()
    top_paid = State()


class FSMTotalDom(StatesGroup):
    total_dom_pay_and_get = State()
    total_dom_pay_choise = State()
    total_dom_paid = State()