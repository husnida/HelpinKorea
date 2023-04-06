import logging
from aiogram import Bot, Dispatcher, executor, types
import buttons
import matnlar1
from aiogram.dispatcher.filters import Text

API_TOKEN = '6264614299:AAGYcOFIX-G19ojmF2zFcuqZu0sOgAGEG7Y'

user_data = {}

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await bot.send_message(message.from_user.id, matnlar1.welcome_text, reply_markup=buttons.welcome_keyboard, parse_mode = types.ParseMode.MARKDOWN)


@dp.message_handler(Text(equals=["Korea haqida ma'lumot", "Koreada yashash"]))
async def culture_or_live(message: types.Message):
    user_id = message.from_user.id
    text = message.text
    if text ==  "Koreada yashash":
        await bot.send_message(user_id, matnlar1.live_text, reply_markup = buttons.live, parse_mode = types.ParseMode.MARKDOWN)
    else:
        await bot.send_message(user_id, matnlar1.culture_text,reply_markup = buttons.culture, parse_mode = types.ParseMode.MARKDOWN)


@dp.message_handler(Text(equals=["Koreada ish topish", "Viza bo'yicha ma'lumot"]))
async def about_live(message: types.Message):
    user_id = message.from_user.id
    text = message.text
    if text == "Koreada ish topish":
        msg_txt = matnlar1.about_work
    else:
       msg_txt = matnlar1.about_visa
    await bot.send_message(user_id, msg_txt, reply_markup = buttons.connect_to_live, parse_mode = types.ParseMode.MARKDOWN)
    
@dp.message_handler(Text(equals=["Koreada ish topish sayti", "Viza bo'yicha ma'lumot beruvchi sayt"]))
async def about_live(message: types.Message):
    user_id = message.from_user.id
    text = message.text
    if text == "Koreada ish topish sayti":
        msg_txt = matnlar1.about_part_time_job
        msg_txt = matnlar1.part_time_job
        msg_txt = matnlar1.about_job
    else:
       msg_txt = matnlar1.about_visa1
    await bot.send_message(user_id, msg_txt, reply_markup = buttons.connect_to_live, parse_mode = types.ParseMode.MARKDOWN)
    
@dp.message_handler(Text(equals=["Koreys tili", "Korea madaniyati","Korea shaharlari"]))
async def about_culture(message: types.Message):
    user_id = message.from_user.id
    text = message.text
    if text == "Koreys tili":
        msg_txt = matnlar1.about_language
    elif text == "Korea madaniyati":
       msg_txt = matnlar1.about_culture
    else:
        msg_txt = matnlar1.about_cities
    await bot.send_message(user_id, msg_txt, reply_markup = buttons.go_culture, parse_mode = types.ParseMode.MARKDOWN) 
    
@dp.message_handler(Text(equals=["Koreys tili", "Korea madaniyati","Korea shaharlari"]))
async def about_live(message: types.Message):
    user_id = message.from_user.id
    text = message.text
    if text == "Koreada ish topish sayti":
        msg_txt = matnlar1.about_part_time_job
        msg_txt = matnlar1.part_time_job
        msg_txt = matnlar1.about_job
    else:
       msg_txt = matnlar1.about_visa1
    await bot.send_message(user_id, msg_txt, reply_markup = buttons.connect_to_live, parse_mode = types.ParseMode.MARKDOWN)


@dp.message_handler(content_types=['text'])
async def about_live(message: types.Message):
    user_id = message.from_user.id
    step = user_data[user_id]["step"]
    if step == "question":
        user_data[user_id]["question"] = message.text
        print(user_data[user_id])
        await bot.send_message(user_id, message.from_user.id)
        user_data[user_id]["step"] = message.from_user.id
    elif step == message.from_user.id:
        user_data[user_id][message.from_user.id] = message.text
        print(user_data[user_id])
        await bot.send_message(user_id, "Siz so'ragan savolga tez orada javob beramiz😊")
        


@dp.callback_query_handler()
async def callback(message: types.Message):
    user_id = callback.from_user.id
    await callback.answer("Biz bilan bog'langaningiz uchun sizdan minnatdormiz🤝")
    await bot.send_message(user_id, "Iltimos ismingizni yuboring: ")
    user_data[user_id] = {}
    user_data[user_id]["step"] = "name"

    

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
