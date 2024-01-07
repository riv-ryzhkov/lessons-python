#  riv  @riv_chat_bot
# pip install fuzzywuzzy


import telebot
import os
from fuzzywuzzy import fuzz
import datetime
from my_token import token_chat

# Створюємо бот


def char_load():
    # Завантажуємо фрази та відповіді у список
    massive = []
    if os.path.exists('data/riv-chat.txt'):
        with open('data/riv-chat.txt', 'r') as file:
            for line in file:
                if len(line.strip()) > 2:
                    # massive.append(line.strip().lower())
                    massive.append(line.strip())



# Використовуємо fuzzywuzzy для підбору найбільш схожої фрази та повертаємо відповідь
def answer(text):
    try:
        text = text.lower().strip()
        if os.path.exists('data/riv-chat.txt'):
            max_rate = 0
            place = 0
            max_place = 0
            for question in massive:
                if 'q: ' in question:
                    # За допомогою fuzzywuzzy порівнюємо рядки
                    current = (fuzz.token_sort_ratio(question.replace('q: ', ''), text))
                    if current > max_rate and current != max_rate:
                        max_rate = current
                        max_place = place
                place += 1
            result = massive[max_place + 1]
            return result
        else:
            return 'Це дуже складне питання. Я поміркую і прокоментую наступного разу.'
    except Exception as err:
        # print(err)
        # return
        return 'Щось пішло не так з нашим чатом. Але я згодом розберуся. Обіцяю!'



def chat_start():
    # Команда «start»
    @bot.message_handler(commands=["start"])
    def start(m, res=False):
        global st
        start_text = '''
    Доброго дня! 
    
    Мене звуть Ігор Рижков.
    
    Проте, наразі я не зовсім Ігор. )))
    Я бот, створений ним. 
    Але я дуже добре знаю Ігоря і гадаю, що зможу відповісти на будь-які Ваші запитання.
    Сподіваюсь, наше спілкування буде інформативним і корисним.
    
    Скажіть, будь ласка, як я можу до Вас звертатись?'''
        bot.send_message(m.chat.id, start_text)
        st = 1



def chat_text():
    # Получение сообщений от юзера
    @bot.message_handler(content_types=["text"])
    def handle_text(message):
        global st, name
        if st == 1:
            st = 0
            name = message.text
            send_text = f'Дуже приємно, {name}.\n' \
                        f'Я впевнений, що Ви ознайомились з моїм CV.\n\n' \
                        f'Проте, воно надто коротке для повної інформації.\n' \
                        f'Тож, я уважно слухаю Вас.\n' \
                        f'Ви можете задати будь-яке питання і я обіцяю щиро відповісти на нього.'
        else:
            send_text = answer(message.text)

            # Запис логiв
        with open('data/' + str(message.chat.id) + '_log.txt', 'a') as f:
            f.write('q: ' + message.text + '\n' + send_text + ' ===> ' + str(datetime.datetime.now()) + '\n')

        # Відправка відповіді
        bot.send_message(message.chat.id, send_text)



if __name__ == '__main__':
    bot = telebot.TeleBot(token_chat)
    st = 0
    # Запуск боту
    bot.polling(none_stop=True, interval=0)
