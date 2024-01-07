#riv_wiki @riv_wiki_bot
# pip install wikipedia

import telebot, wikipedia, re
from my_token import token_wiki


# Створюємо екземпляр бота

bot = telebot.TeleBot(token_wiki)

# Встановлюємо мову в Wikipedia
wikipedia.set_lang("uk")

# Чистимо текст статті у Wikipedia і обмежуємо його тисячею символів
def get_info(word):
     try:
         info = wikipedia.page(word)


         # Отримуємо першу тисячу символів
         wiki_text = info.content[:1000]
         # return wiki_text

         # Розділяємо по точках
         wiki_list = wiki_text.split('.')

         # Відкидаємо все після останньої точки
         wiki_list = wiki_list[:-1]

         # Створюємо порожню змінну для тексту
         wiki_res = ''

         # Проходимося рядками, де немає знаків «рівно» (тобто все, крім заголовків)
         for i in wiki_list:
             if not('==' in i):
                     # Якщо в рядку залишилося більше трьох символів,
                     # додаємо її до нашої змінної
                     # і повертаємо втрачені при поділі рядків точки на місце
                 if len(i.strip()) > 3:
                     wiki_res = wiki_res + i + '.'
             else:
                 break

         # Тепер за допомогою регулярних виразів прибираємо розмітку
         wikitext_res = re.sub('\([^()]*\)', '', wiki_res)

         # Повертаємо текстовий рядок
         return wikitext_res

     # Обробляємо виняток, який міг повернути модуль wikipedia при запиті
     except Exception as e:
         return 'На жаль! Ця інформація відсутня у Wikipedia. Введіть інше слово.'

# Функція, що обробляє команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
     bot.send_message(m.chat.id, 'Якщо Ви відправите мені будь-яке слово, то я знайду його значення в Wikipedia.')

# Отримання повідомлень від користувача
@bot.message_handler(content_types=["text"])
def handle_text(message):
     bot.send_message(message.chat.id, get_info(message.text))

# Запускаємо бота
bot.polling(none_stop=True, interval=0)


