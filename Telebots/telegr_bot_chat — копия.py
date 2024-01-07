

import telebot
import os
from fuzzywuzzy import fuzz


# Создаем бота, пишем свой токен
bot = telebot.TeleBot('11111111111111111111111111111')

# Загружаем список фраз и ответов в массив
mas = []
if os.path.exists('data/chat.txt'):
    with open('data/chat.txt', 'r') as f:
        for x in f:
            if len(x.strip()) > 2:
                mas.append(x.strip().lower())

# С помощью fuzzywuzzy вычисляем наиболее похожую фразу и выдаем в качестве ответа следующий элемент списка
def answer(text):
    try:
        text = text.lower().strip()
        if os.path.exists('data/chat.txt'):
            a = 0
            n = 0
            nn = 0
            for q in mas:
                if 'u: ' in q:
                    # С помощью fuzzywuzzy получаем, насколько похожи две строки
                    aa = (fuzz.token_sort_ratio(q.replace('u: ', ''), text))
                    if aa > a and aa != a:
                        a = aa
                        nn = n
                n += 1
            s = mas[nn + 1]
            return s
        else:
            return 'Ошибка'
    except:
        return 'Ошибка'

# Команда «Старт»
@bot.message_handler(commands=["start"])
def start(m, res=False):
    global st
    bot.send_message(m.chat.id, 'Привет! Напиши мне как тебя зовут? Плиииз! )')
    st = 1



# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    global st, name
    if st == 1:
        st = 0
        name = message.text
        s = 'Привет, ' + name + '! Очень приятно!'
    else:
        # s = name + '! ' + answer(message.text)
        s = answer(message.text)

        # Запись логов
    with open('data/' + str(message.chat.id) + '_log.txt', 'a') as f:
        f.write('u: ' + message.text + '\n' + s +'\n')

    # Отправка ответа
    bot.send_message(message.chat.id, s)

# Запускаем бота
bot.polling(none_stop=True, interval=0)