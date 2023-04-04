from aiogram import types

welcome_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
button1 = types.KeyboardButton("Korea haqida ma'lumot")
button2 = types.KeyboardButton("Koreada yashash")
welcome_keyboard.add(button1, button2)


live = types.ReplyKeyboardMarkup(resize_keyboard=True)
live1 = types.KeyboardButton("Koreada ish topish")
visa = types.KeyboardButton("Viza bo'yicha ma'lumot")

#live.add()
live.add(live1)
live.add(visa)

connect_to_live = types.InlineKeyboardMarkup(resize_keyboard=True)
connect_button = types.InlineKeyboardButton("Biz bilan bog'lanish",callback_data="Contact us")
connect_to_live.add(connect_button)

culture = types.ReplyKeyboardMarkup(resize_keyboard=True)
language = types.KeyboardButton("Koreys tili")
culture1 = types.KeyboardButton("Korea madaniyati")
city = types.KeyboardButton("Korea shaharlari")

#culture.add()
culture.add(culture)
culture.add(language)
culture.add(city)

go_culture = types.InlineKeyboardMarkup(resize_keyboard=True)
culture_button = types.InlineKeyboardButton("Korea bilan tanishamiz",callback_data="Learn Korea country")
go_culture.add(culture_button)