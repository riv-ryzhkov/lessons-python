#  riv  @riv_chat_bot
# pip install fuzzywuzzy


import telebot
import os
from fuzzywuzzy import fuzz
import datetime
from my_token import token_chat, token_echo


# Создаем бота, пишем свой токен
bot = telebot.TeleBot(token_chat)
# bot = telebot.TeleBot(token_echo)

# Загружаем список фраз и ответов в массив
mas = []
if os.path.exists('data/chat-ua.txt'):
    with open('data/chat-ua.txt', 'r') as f:
        print('run')
        for x in f:
            if len(x.strip()) > 2:
                mas.append(x.strip().lower())
else:
    print('NO FILE  data/chat-ua.txt  ')

# С помощью fuzzywuzzy вычисляем наиболее похожую фразу и выдаем в качестве ответа следующий элемент списка
def answer(text):
    try:
        text = text.lower().strip()
        if os.path.exists('data/chat-ua.txt'):
            rate_max = 0
            current_qst = 0
            best_qst = 0
            for q in mas:
                if 'q: ' in q:
                    # С помощью fuzzywuzzy получаем, насколько похожи две строки
                    current_rate = (fuzz.token_sort_ratio(q.replace('q: ', ''), text))
                    print('rate=', current_rate) #  0...100
                    if current_rate > rate_max and current_rate != rate_max:
                        rate_max = current_rate
                        best_qst = current_qst
                current_qst += 1
            res_answer = mas[best_qst + 1]
            print(rate_max, text, mas[best_qst])
            return res_answer
        else:
            return 'Помилка'
    except:
        return 'Помилка'

# Команда «Старт»
@bot.message_handler(commands=["start"])
def start(m):
    global start
    bot.send_message(m.chat.id, 'Привіт! Напиши мені як тебе зовуть? Пліііііз! )')
    start = 1



# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    global start, name
    if start == 1:
        start = 0
        name = message.text
        s = 'Привіт, ' + name + '! Дуже приємно!'
    else:
        s = answer(message.text)

        # Запись логов
    with open('data/' + str(message.chat.id) + '_log.txt', 'a') as f:
        f.write('u: ' + message.text + '\n' + s + ' ===> ' + str(datetime.datetime.now()) + '\n')

    # Отправка ответа
    bot.send_message(message.chat.id, s)

# Запускаем бота
bot.polling(none_stop=True, interval=0)