from secret import TELEGRAM_TOKEN as token
import asyncio
from aiogram import Bot, Dispatcher, executor

bot = Bot(token=token)
loop = asyncio.get_event_loop()
dp = Dispatcher(bot, loop=loop)

if __name__ == '__main__':
    executor.start_polling(dispatcher=dp)