from secret import TELEGRAM_TOKEN as token
import asyncio
from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message

bot = Bot(token=token)
loop = asyncio.get_event_loop()
dp = Dispatcher(bot, loop=loop)

@dp.message_handler()
async def messages(message: Message):
    await bot.send_message(chat_id=message.from_id, text=message.text)

if __name__ == '__main__':
    executor.start_polling(dispatcher=dp)