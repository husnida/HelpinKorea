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
culture.add(culture1)
culture.add(language)
culture.add(city)

go_culture = types.InlineKeyboardMarkup(resize_keyboard=True)
culture_button = types.InlineKeyboardButton("Korea bilan tanishamiz",callback_data="Learn Korea country")
go_culture.add(culture_button)


live = types.ReplyKeyboardMarkup(resize_keyboard=True)
live2 = types.KeyboardButton("Koreada ish topish sayti")
visa1 = types.KeyboardButton("Viza bo'yicha ma'lumot beruvchi sayt")

live.add(live2)
live.add(visa1)

connect_to_live = types.InlineKeyboardMarkup(resize_keyboard=True)
connect_button = types.InlineKeyboardButton("Yana qo'shimcha ma'lumot",callback_data="Contact us")
connect_to_live.add(connect_button)


culture = types.ReplyKeyboardMarkup(resize_keyboard=True)
language1 = types.KeyboardButton("Koreys tili gramatikasi")
culture2 = types.KeyboardButton("Korea taomlari")
city1 = types.KeyboardButton("Korea shaharlari bilan tanishamiz")

#culture.add()
culture.add(culture2)
culture.add(language1)
culture.add(city1)

go_culture = types.InlineKeyboardMarkup(resize_keyboard=True)
culture_button = types.InlineKeyboardButton("Korea madaniyati bilan tanishamiz",callback_data="Learn Korea country")
go_culture.add(culture_button)
