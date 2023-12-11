from secret import TELEGRAM_TOKEN as token
import asyncio
import navigation as nav
from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup


bot = Bot(token=token)
loop = asyncio.get_event_loop()
dp = Dispatcher(bot, loop=loop)

@dp.message_handler(commands=["start"])
async def command_start_handler(message: Message):
    text, reply_markup = nav.get_reply_message({'new_state':1})
    await bot.send_message(
        chat_id=message.chat.id, 
        text=text,
        reply_markup=reply_markup)

@dp.message_handler()
async def messages(message: Message):
    pass

@dp.callback_query_handler(lambda callback_query: callback_query.data)
async def callback_query(callback_query: CallbackQuery):
    context = eval(callback_query.data)    
    text, reply_markup = nav.get_reply_message(context)
    await bot.send_message(
        chat_id=callback_query.message.chat.id, 
        text=text,
        reply_markup=reply_markup)

if __name__ == '__main__':
    executor.start_polling(dispatcher=dp)