"""
This is a echo bot.
It echoes any incoming text messages.
"""

import logging
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6264614299:AAGYcOFIX-G19ojmF2zFcuqZu0sOgAGEG7Y'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply(f"👋Salom { message.from_user.first_name }!\nMen aks sado Bot hisoblanaman!\nAiogram tomonidan quvvatlanganman .")

@dp.message_handler(content_types=['text'])
async def greeting(message: types.Message):
    if message.text == 'Salom':
        await message.reply("Va alaykum assalom")
    else:
        await message.reply("Sizga qanday ma'lumot kerak?🤔")
          
          
@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    
# Koreadagi musofirlarga yordam tariqasida Korea haqida ma'lumot beradigan bot.
#Qanday ma'lumot kerakligi so'raladi
#Qaysi vaqtda u bilan bog'lanishimiz mumkinligi so'raladi 