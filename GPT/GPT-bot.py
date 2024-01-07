import telebot
import wikipedia
from my_token import token_wiki

bot = telebot.TeleBot(token_wiki)

# @bot.message_handler(content_types=['text'])
# def send_echo(message):
#     bot.send_message(message.chat.id, message.text)
#
# bot.polling()

@bot.message_handler(commands=['wiki'])
def send_wiki(message):
    bot.send_message(message.chat.id, 'Please enter the term you want to search in Wikipedia:')

@bot.message_handler(func=lambda message: True)
def send_wiki_result(message):
    term = message.text
    wikipedia.set_lang("ru")
    try:
        result = wikipedia.summary(term, sentences=2)
        bot.send_message(message.chat.id, result)
    except wikipedia.exceptions.DisambiguationError as e:
        bot.send_message(message.chat.id, e.options)

bot.polling()