
import telebot, wikipedia, re


# Создаем экземпляр бота
bot = telebot.TeleBot('111111111111111111111111111111111')

# Устанавливаем язык в Wikipedia
wikipedia.set_lang("ru")

# Чистим текст статьи в Wikipedia и ограничиваем его тысячей символов
def get_info(word):
    try:
        info = wikipedia.page(word)

        # Получаем первую тысячу символов
        wiki_text = info.content[:1000]

        # Разделяем по точкам
        wiki_list = wiki_text.split('.')

        # Отбрасываем всЕ после последней точки
        wiki_list = wiki_list[:-1]

        # Создаем пустую переменную для текста
        wiki_res = ''

        # Проходимся по строкам, где нет знаков «равно» (то есть все, кроме заголовков)
        for i in wiki_list:
            if not('==' in i):
                    # Если в строке осталось больше трех символов, добавляем ее к нашей переменной и возвращаем утерянные при разделении строк точки на место
                if len(i.strip()) > 3:
                    wiki_res = wiki_res + i + '.'
            else:
                break

        # Теперь при помощи регулярных выражений убираем разметку
        wikitext_res = re.sub('\([^()]*\)', '', wiki_res)

        # Возвращаем текстовую строку
        return wikitext_res

    # Обрабатываем исключение, которое мог вернуть модуль wikipedia при запросе
    except Exception as e:
        return 'Увы! Данная информация отсутствует в Wikipedia. Введите другое слово.'

# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Если Вы отправете мне любое слово, то я найду его значение в Wikipedia.')

# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, get_info(message.text))

# Запускаем бота
bot.polling(none_stop=True, interval=0)