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


class Leo(StatesGroup):
    class TopOzon(StatesGroup):
        top_ozon_pay = State()
        top_ozon_paid = State()

    class TopMarket(StatesGroup):
        top_market_pay = State()
        top_market_paid = State()


class Pavel(StatesGroup):
    class ToTheLyam(StatesGroup):
        to_the_lyam_pay = State()
        to_the_lyam_paid = State()

    class TotalDom(StatesGroup):
        total_dom_pay = State()
        total_dom_paid = State()


class Elena(StatesGroup):
    azbuka_pay = State()
    azbuka_paid = State()