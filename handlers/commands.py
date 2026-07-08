from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from mystate import UserInfoState
from aiogram.fsm.context import FSMContext
from database import select_user

rt = Router()

@rt.message(Command("start"))
async def start(message: Message, state: FSMContext):
    user_id = message.from_user.id
    user = select_user(user_id)
    if user:
        await message.answer("Siz ro'yxatdan o'tgansiz😁")
    else:
        await state.update_data(user_id=user_id)
        await message.answer("salom ismingizni kiriting")
        await state.set_state(UserInfoState.ism)


@rt.message(Command("myinfo"))
async def my_info_handler(message: Message):
    user = select_user(user_id=message.from_user.id)
    await message.answer(f"Your data {user}")
