# .venv\Scripts\activate
# black . для всего
# git add .
# git commit -m "ававыафывафыафыафыв"
# git push

import asyncio
from aiogram import Bot, Dispatcher

from app.handlers import router
from app.database.models import async_main


async def main():
    await async_main()
    bot = Bot(token="7342148548:AAEtG8xEz93qNH7r-OB8Dll86noxLV1NHZ4")
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот выключен")
