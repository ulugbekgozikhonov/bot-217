from bot import bot
from dispatcher import dp
import logging
import asyncio
from database import create_tables

logging.basicConfig(level=logging.INFO)


async def main():
    create_tables()
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
