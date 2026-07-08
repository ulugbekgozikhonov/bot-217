from aiogram import Dispatcher
from handlers.commands import rt as commands_router
from handlers.register import rt as register_router


dp = Dispatcher()
dp.include_router(commands_router)
dp.include_router(register_router)
