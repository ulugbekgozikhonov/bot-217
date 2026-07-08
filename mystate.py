from aiogram.fsm.state import StatesGroup, State

class UserInfoState(StatesGroup):
    ism = State()
    yosh = State()
    address = State()
    tel = State()