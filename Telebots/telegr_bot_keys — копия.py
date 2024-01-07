
import telebot
from telebot import types


token = '1111111111111111111111111111111'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет! Хотите поиграться с кнопками?\n Пришлите команду /button')


@bot.message_handler(commands=['button'])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Первая Кнопка!")
    markup.add(item1)
    item2 = types.KeyboardButton("Третья Кнопка!")
    markup.add(item2)
    bot.send_message(message.chat.id, 'Нажмите на Первую кнопку!', reply_markup=markup)


@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text == "Первая Кнопка!":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Вторая Кнопка!")
        markup.add(item1)
        item2 = types.KeyboardButton("Третья Кнопка!")
        markup.add(item2)
        bot.send_message(message.chat.id, 'Нажмите на Вторую кнопку, чтобы к ней перейти!', reply_markup=markup)
    elif message.text == "Вторая Кнопка!":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Первая Кнопка!")
        markup.add(item1)
        item2 = types.KeyboardButton("Третья Кнопка!")
        markup.add(item2)
        bot.send_message(message.chat.id, 'Нажмите на Первую кнопку, чтобы к ней перейти!', reply_markup=markup)
    elif message.text == "Третья Кнопка!":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Первая Кнопка!")
        markup.add(item1)
        item2 = types.KeyboardButton("Третья Кнопка!")
        markup.add(item2)
        bot.send_message(message.chat.id, 'Я знал, что Вы ее нажмете! )))))', reply_markup=markup)


bot.infinity_polling()