
import telebot
import random
from telebot import types


# Загружаем список IT
with open('data/it_news.txt', 'r') as f:
    it_facts = f.read().split('\n')


# Загружаем список sport
with open('data/sport_news.txt', 'r') as f:
    sport_news = f.read().split('\n')

# Создаем бота
bot = telebot.TeleBot('11111111111111111111111111111111111')

# Команда start
@bot.message_handler(commands=["start"])
def start(m, res=False):
        # Добавляем кнопки
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Спортивні новини")
        item2 = types.KeyboardButton("Новини IT")
        markup.add(item1)
        markup.add(item2)
        bot.send_message(m.chat.id, 'Натисни: \n"Спортивні новини" для отримання інформації про спорт\n"Новини IT" — для отримання інформації в галузі IT ',  reply_markup=markup)

# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    # Если юзер прислал 1, выдаем ему Sport
    if message.text.strip() == "Спортивні новини":
            answer = random.choice(sport_news)

    # Если юзер прислал 2, выдаем IT
    elif message.text.strip() == "Новини IT":
            answer = random.choice(it_facts)

    # Отсылаем юзеру сообщение в его чат
    bot.send_message(message.chat.id, answer)

# Запускаем бота
bot.polling(none_stop=True, interval=0)