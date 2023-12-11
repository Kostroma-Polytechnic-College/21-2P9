from secret import TELEGRAM_TOKEN as token
import asyncio
from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

bot = Bot(token=token)
loop = asyncio.get_event_loop()
dp = Dispatcher(bot, loop=loop)

@dp.message_handler()
async def messages(message: Message):
    await bot.send_message(
        chat_id=message.chat.id, 
        text=str(message.from_user),
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[[
                InlineKeyboardButton(
                    text=message.text, 
                    callback_data=message.from_user.username
                )]]
        )
    )

@dp.callback_query_handler(lambda callback_query: callback_query.data)
async def callback_query(callback_query: CallbackQuery):
    await bot.send_message(
        chat_id=callback_query.message.chat.id, 
        text=callback_query.data)

if __name__ == '__main__':
    executor.start_polling(dispatcher=dp)