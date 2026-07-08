from aiogram import Router, F
from aiogram.types import Message
from mystate import UserInfoState
from aiogram.fsm.context import FSMContext
from database import insert_user

rt = Router()


@rt.message(F.text, UserInfoState.ism)
async def ism_handler(message: Message, state: FSMContext):
    ism = message.text
    await state.update_data(first_name=ism)
    await message.answer("yoshingizni kiriting")
    await state.set_state(UserInfoState.yosh)


@rt.message(F.text, UserInfoState.yosh)
async def yosh_handler(message: Message, state: FSMContext):
    yosh = message.text
    await state.update_data(age=yosh)
    await message.answer("Addresingizni kiriting")
    await state.set_state(UserInfoState.address)


@rt.message(F.text, UserInfoState.address)
async def address_handler(message: Message, state: FSMContext):
    address = message.text
    await state.update_data(address=address)
    await message.answer("Telefon raqamingizni kiriting")
    await state.set_state(UserInfoState.tel)


@rt.message(F.text, UserInfoState.tel)
async def tel_handler(message: Message, state: FSMContext):
    tel = message.text
    await state.update_data(phone=tel)
    data = await state.get_data()
    is_insert = insert_user(
        data.get("user_id"),
        data.get("first_name"),
        data.get("age"),
        data.get("address"),
        data.get("phone"),
    )
    if is_insert:
        await message.answer("Malumotlariz saqlandi ko'rish uchun /myinfo ni bosing")
    else:
        await message.answer("BOTDA XATOLIK")
    await state.clear()
