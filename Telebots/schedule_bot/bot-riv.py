from datetime import datetime
from threading import Thread

import telebot
import schedule
import time

# TODO ЗАПИСЬ ВЕБИНАРА БУДЕТ ДОСТУПНА!
from models import User, Todo

# bot = telebot.TeleBot('<your_api_key>')
bot = telebot.TeleBot('5034062450:AAEj1f3Qfq4zv4roJGaTh9LsgYCc4tEmsEc')


# /start /help /some
@bot.message_handler(commands=['start'])
def start_handler(message):
    if not User.select().where(User.chat_id == message.chat.id):
        User.create(
            chat_id=message.chat.id
        )
    bot.send_message(
        message.chat.id,
        f"Hello, {message.chat.first_name} {message.chat.last_name or ''}!"
    )

@bot.message_handler(content_types=['text'])
def create_todo_handler(message):
    user = User.get(User.chat_id == message.chat.id)
    Todo.create(
        task=message.text,
        is_done=False,
        user=user,
        date=datetime.today()
    )
    bot.send_message(
        message.chat.id,
        "Your todo was saved!"
    )


bot.infinity_polling()

