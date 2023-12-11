from secret import TELEGRAM_TOKEN as token
import asyncio
from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup

bot = Bot(token=token)
loop = asyncio.get_event_loop()
dp = Dispatcher(bot, loop=loop)

@dp.message_handler()
async def messages(message: Message):
    await bot.send_message(
        chat_id=message.from_id, 
        text=str(message.from_user),
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[[
                InlineKeyboardButton(
                    text=message.text, 
                    callback_data='1'
                )]]
        )
    )

if __name__ == '__main__':
    executor.start_polling(dispatcher=dp)