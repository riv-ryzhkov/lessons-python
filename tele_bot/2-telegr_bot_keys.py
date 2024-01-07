# igor   @riv_keys_bot

import telebot
from telebot import types
from my_token import token_keys


bot = telebot.TeleBot(token_keys)


@bot.message_handler(commands=['start', 's'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привіт! Хочеш погратися з кнопками?\n Надійшли команду /button')


@bot.message_handler(commands=['button'])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton(keys[1])
    item2 = types.KeyboardButton(keys[2])
    item3 = types.KeyboardButton(keys[3])
    markup.add(*[item1, item2, item3])
    # print(markup.to_json())
    bot.send_message(message.chat.id, 'Натисни на Першу кнопку!', reply_markup=markup)


@bot.message_handler(content_types='text')
def message_reply(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if message.text == keys[1]:
        item1 = types.KeyboardButton(keys[0])
        item2 = types.KeyboardButton(keys[2])
        item3 = types.KeyboardButton(keys[3])
        markup.add(*[item1, item2, item3])
        # print('*'*80)
        bot.send_message(message.chat.id, 'Натисни на Другу кнопку, щоб перейти до неї!', reply_markup=markup)
    elif message.text == keys[2]:
        item1 = types.KeyboardButton(keys[1])
        item2 = types.KeyboardButton(keys[0])
        item3 = types.KeyboardButton(keys[3])
        markup.add(*[item1, item2, item3])
        bot.send_message(message.chat.id, 'Натисни на Першу кнопку, щоб перейти до неї!', reply_markup=markup)
    elif message.text == keys[3]:
        item1 = types.KeyboardButton(keys[1])
        item2 = types.KeyboardButton(keys[2])
        item3 = types.KeyboardButton(keys[0])
        markup.add(*[item1, item2, item3])
        bot.send_message(message.chat.id, 'Я знав, що ти її натиснешь! )))))', reply_markup=markup)


keys = ["☑️🇺🇦", "1️⃣ Перша Кнопка!👌", "2️⃣ Друга Кнопка!👨‍🎓", "3️⃣ Третя Кнопка!"]
bot.infinity_polling()