#  riv  @riv_chat_bot
# pip install fuzzywuzzy

import telebot
import os
from fuzzywuzzy import fuzz
import datetime
from my_token import token_chat
from telebot import types
import speech_recognition


def chat_run(massive):
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
        return 'Щось пішло не так з нашим чатом. Але я згодом розберуся. Обіцяю!'



def listen_command():
    """Func will return the recognized command"""
    sr = speech_recognition.Recognizer()
    # sr.pause_threshold = 0.5
    try:
        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(source=mic, duration=0.5)
            audio = sr.listen(source=mic)
            query = sr.recognize_google(audio_data=audio, language='uk-UA').lower()
        return query
    except speech_recognition.UnknownValueError:
        return 'Вибачаюсь, Я не зрозумів, що Ви кажете, \nпроте Я спробую вгадати,' \
               ' \n\nАле, якщо я помилився, повторіть Ваше питання більш чітко ' \
               'і з невеличкою паузою після вводу "1"\n\n Дякую.'


def chat_keys(key_level):
    if key_level == "1.0":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Використовувати button-помічника.")
        markup.add(item1)
    elif key_level == '2.0':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Умови моєї роботи зараз...")
        markup.add(item1)
        item2 = types.KeyboardButton("Професійний досвід...")
        markup.add(item2)
        item3 = types.KeyboardButton("Іноземна мова...")
        markup.add(item3)
        item4 = types.KeyboardButton("Soft skills...")
        markup.add(item4)
        item5 = types.KeyboardButton("Мої очікування...")
        markup.add(item5)
    elif key_level == '2.1':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Моє місце роботи зараз.")
        markup.add(item1)
        item2 = types.KeyboardButton("Моя посада зараз.")
        markup.add(item2)
        item3 = types.KeyboardButton("Моя зарплатня зараз.")
        markup.add(item3)
        item4 = types.KeyboardButton("Стаж цієї роботи.")
        markup.add(item4)
        item5 = types.KeyboardButton("Перейти до головного меню.")
        markup.add(item5)
    elif key_level == '2.2':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Де, скільки і ким працював.")
        markup.add(item1)
        item2 = types.KeyboardButton("Досвід програмування.")
        markup.add(item2)
        item3 = types.KeyboardButton("Досвід використання Python.")
        markup.add(item3)
        item4 = types.KeyboardButton("Інші технології та ПЗ, що використовуєте.")
        markup.add(item4)
        item5 = types.KeyboardButton("Перейти до головного меню.")
        markup.add(item5)
    elif key_level == '2.3':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Якими іноземними мовами водолієте і на якому рівні.")
        markup.add(item1)
        item2 = types.KeyboardButton("Досвід використання іноземної мови у професійній діяльності.")
        markup.add(item2)
        item3 = types.KeyboardButton("Досвід використання іноземної мови у викладацькій діяльності.")
        markup.add(item3)
        item4 = types.KeyboardButton("Досвід зарубіжних професійних стажувань.")
        markup.add(item4)
        item5 = types.KeyboardButton("Перейти до головного меню.")
        markup.add(item5)
    elif key_level == '2.4':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Досвід роботи в команді.")
        markup.add(item1)
        item2 = types.KeyboardButton("Досвід організаційної діяльності.")
        markup.add(item2)
        item3 = types.KeyboardButton("Наявність ораторських здібностей.")
        markup.add(item3)
        item4 = types.KeyboardButton("Досвід організації та проведення перемовин з партнерами.")
        markup.add(item4)
        item5 = types.KeyboardButton("Інші особисті якості.")
        markup.add(item5)
        item6 = types.KeyboardButton("Перейти до головного меню.")
        markup.add(item6)
    elif key_level == '2.5':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Причина пошуку нової роботи.")
        markup.add(item1)
        item2 = types.KeyboardButton("FullTime vs PartTime.")
        markup.add(item2)
        item3 = types.KeyboardButton("Очікуємий режим роботи.")
        markup.add(item3)
        item4 = types.KeyboardButton("Очікуєма заробітна платня.")
        markup.add(item4)
        item5 = types.KeyboardButton("Інші особисті сподівання та умови.")
        markup.add(item5)
        item6 = types.KeyboardButton("Перейти до головного меню.")
        markup.add(item6)
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    return markup


def chat_main(bot, st, name, key_level):
    mark = 0
    # Команда «start»
    @bot.message_handler(commands=["start"])
    def start(message):
        global st, mark
        start_text = f'Доброго дня, {message.from_user.first_name} {message.from_user.last_name}!'
        start_text += '''
        
        Мене звуть Ігор Рижков.
        
        Проте, наразі я не зовсім Ігор. )))
        Я бот, створений ним. 
        
Але я дуже добре знаю Ігоря і гадаю, що зможу відповісти на будь-які Ваші запитання.
Сподіваюсь, наше спілкування буде інформативним і корисним.\n
        '''
        start_text += f'{message.from_user.first_name}, cкажіть, будь ласка, як я можу до Вас звертатись?'
        st = 1
        bot.send_message(message.chat.id, start_text)



    # Получение сообщений от юзера
    @bot.message_handler(content_types=["text"])
    def handle_text(message):

        global st, name, key_level, mark
        print('st=', st)
        try:
            # markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            if st == 1:
                name = message.text
                send_text = f'Дуже приємно, {name}.\n'
                send_text += '''
Я впевнений, що Ви ознайомились з моїм CV.
Проте, воно надто коротке для повної інформації.
                
Тож, я уважно слухаю Вас і готов розповісти про себе.
Ви можете задати будь-яке питання і я обіцяю щиро відповісти на нього.
                
Звертаю Вашу увагу на те, що Ви маєте можливість задавати питання у різні способи:
                
1) Ви маєте можливість вільно набирати будь-яке питання з клавіатури.
                
2) Ви можете скористатись button-помічником. 
Для цього Вам достатньо просто ввести з клавіатури слово "меню", або, якщо меню вже активно, у будь-яку мить Ви можете його згорнути чи разгорнути, натиснувши квадратик праворуч на рядку ввода тексту. (користуйтесь прокруткою, щоб побачити усі пункти меню).
                
3) Скористайтесь можливістю поставити питання просто голосом.
Для цього введіть з клавіатури "1", натисніть ENTER і спокійно поставте питання просто голосом через мікрофон. Поспішати і нічого додатково натискати не потрібно.
                
ВАЖЛИВО! Якщо Ви не заперечуєте, цей чат буде автоматично записуватись. Це дозволить мені його проаналізувати, поліпшити і відкоректувати деякі відповіді.

Дякую за розуміння.
    
Для завершення спілкування введіть "Дякую", а потім - "Ні" у відповідь на пропозицию продовжити діалог.
                
З нетерпінням очікую на Ваше перше запитання...
                
                '''

                # key_level = '1'
            else:
                # print(message.text)
                if message.text == "Використовувати button-помічника.":
                    key_level = "2.0"
                    print(1)
                else:
                    key_level = '0.0'
            
            if message.text == '1':
                bot.send_message(message.chat.id, '"Голосовий ввод". Нічого не натискайте, просто говоріть у мікрофон. Я Вас уважно слухаю...')
                mark = 1
                message.text = listen_command().lower()
                key_level = '0.0'
                bot.send_message(message.chat.id, message.text)
            print(message.text)

            if st:
                st = 0
            else:
                send_text = answer(message.text)[:-3]
                key_level = answer(message.text)[-3:]
            # Запис логiв
            with open('data/' + str(message.chat.id) + '_log.txt', 'a') as f:
                f.write('q: ' + message.text + '\n' + send_text + ' ===> ' + str(datetime.datetime.now()) + '\n')

             # Відправка відповіді
            markup = chat_keys(key_level)
            if key_level != '0.0':
                bot.send_message(message.chat.id, send_text, reply_markup=markup)
            else:
                bot.send_message(message.chat.id, send_text)
        except:
            sorry_text = f'Щиро вибачаюсь, {name}!'
            sorry_text +='''
            Щось пішло не так... Я обов'язково все з'ясую і виправлю цю ситуацію.
            А зараз прошу повторити запитання і не використовувати "смайлики", 
            або ще якісь складні до сприйняття символи.
            
            Дякую за розуміння. 
            
            '''
            bot.send_message(message.chat.id, sorry_text)



if __name__ == '__main__':
    # Створюємо бот
    bot = telebot.TeleBot(token_chat)
    st = 0
    mark = 0
    massive = []
    name = ''
    key_level = "0.0"
    # Завантажуємо фрази та відповіді у список
    chat_run(massive)
    chat_main(bot, st, name, key_level)
    bot.polling(none_stop=True, interval=0)

