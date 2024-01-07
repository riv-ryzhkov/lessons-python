# riv_schedule_bot   riv_schedule

from datetime import datetime
from threading import Thread

import telebot
import schedule
import time
from models import User, Todo


# bot = telebot.TeleBot('<your_api_key>')
bot = telebot.TeleBot('5399565390:AAH6e5WdsnKR1EDp_74btYj1Lag6ueiGwbM')


# /start /help
@bot.message_handler(commands=['start', 's'])
def start_handler(message):
    if not User.select().where(User.chat_id == message.chat.id):
        User.create(
            chat_id=message.chat.id
        )
    bot.send_message(
        message.chat.id,
        f"Hello {message.chat.first_name or ''} {message.chat.last_name or ''}!"
    )

@bot.message_handler(commands=['help', 'h'])
def start_handler(message):
    bot.send_message(
        message.chat.id,
        '''
        
        You can input any text as a new task.
        After that You can check, delete any your tasks
        or mark as "task is done".
        
        
        commands:
        
        /start, /s  \t- start the bot
        /help,  /h  \t- information about the bot
        /today, /t  \t- list of tasks for today
        
        
        <id> done   \t- mark the task is done
        <id> del    \t- delete the task
        '''
    )


def create_all_todo_message(chat_id):
    user = User.get(User.chat_id == chat_id)
    todos = Todo.select().where(Todo.user == user,
                                Todo.date <= datetime.today())
    message_text = []
    # +++++++++++++++++++++

    for todo in todos:
        if todo.is_done:
            message_text.append(f"<b><s>{todo.id}. {todo.task}       \t: {todo.date}</s></b>\n")
        else:
            message_text.append(f"<b>{todo.id}. {todo.task}       : \t{todo.date}</b>\n")
    return "".join(message_text)


@bot.message_handler(commands=['today', 't'])
def get_todo_list(message):
    bot.send_message(
        message.chat.id,
        create_all_todo_message(message.chat.id),
        parse_mode='HTML'
    )


@bot.message_handler(regexp="\d+ done")
def make_done(message):
    todo_id = message.text.split(' ')[0]
    todo = Todo.get(Todo.id == todo_id)
    todo.is_done = True
    todo.save()

    bot.send_message(
        message.chat.id,
        f"<b>{todo.task}</b> is done now",
        parse_mode='HTML'
    )

@bot.message_handler(regexp="\d+ del")
def make_done(message):
    todo_id = message.text.split(' ')[0]
    todo = Todo.get(Todo.id == todo_id)
    task_del = todo.task
    Todo.delete_by_id(todo_id)
    todo.save()

    bot.send_message(
        message.chat.id,
        f"<b>{task_del}</b> is deleted now",
        parse_mode='HTML'
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


def check_notify():
    for user in User.select():
        todos = Todo.select().where(Todo.user == user,
                                    Todo.date == datetime.today(),
                                    Todo.is_done == False)
        if todos:
            bot.send_message(
                user.chat_id,
                create_all_todo_message(user.chat_id),
                parse_mode='HTML'
            )


def run_scheduler():
    schedule.every(1).hours.do(check_notify)
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    Thread(target=run_scheduler).start()
    bot.infinity_polling()

# Python GIL
