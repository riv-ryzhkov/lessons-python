# riv_echo   riv_echo_bot

# pip install pyTelegramBotAPI

import telebot
from my_token import token_echo


def main():
    # Створюємо бота
    bot = telebot.TeleBot(token_echo)
    # print(type(bot))
    # print(*dir(bot), sep='\n')
    #
    # breakpoint()

    # Функція, обробляє команду /start
    @bot.message_handler(commands=["start", "s"])
    def start(mess, res=False):
        bot.send_message(mess.chat.id, "Я на зв'зку. Напиши мні щось. )")

    # Отримання тексту від користувача
    @bot.message_handler(content_types=["text"])
    def handle_text(message):
        # message.text = message.text[::-1].upper()
        bot.send_message(message.chat.id, 'Ти написав:              ' + message.text)
        return message.text

    # Запускаєм бота
    bot.polling(none_stop=True, interval=0)



if __name__ == "__main__":
    main()