# print(__name__)





# text = 'Hello, world!'  # str
# words = text.split()   # list
# print(words)
# print(type(words))
# res = '='.join(words)
# print(res, type(res))


#
# import random
#
#
# def initialize_word():
#     words = ["apple", "banana", "orange", "grape", "pineapple"]  # Список слов
#     return random.choice(words).upper()  # Выбираем случайное слово и приводим его к верхнему регистру
#
#
# def display(word, guessed_letters, attempts):
#     masked_word = ''.join([letter if letter in guessed_letters else '_' for letter in word])
#     print("=" * 41)
#     print(f"{masked_word} (отгаданные буквы: {', '.join(sorted(guessed_letters))})")
#     print("=" * 41)
#     print(f"У Вас осталось {attempts} попыток.")
#     print("=" * 41)
#
#
# def game():
#     secret_word = initialize_word()
#     guessed_letters = set()
#     attempts = len(secret_word)
#
#     while True:
#         display(secret_word, guessed_letters, attempts)
#         if '_' not in ''.join([letter if letter in guessed_letters else '_' for letter in secret_word]):
#             print("Поздравляем, вы угадали слово!")
#             break
#         if attempts == 0:
#             print(f"Вы проиграли! Загаданное слово было: {secret_word}")
#             break
#
#         user_input = input("Введите букву: ").upper()
#         if len(user_input) != 1 or not user_input.isalpha():
#             print("Введите одну букву!")
#             continue
#         if user_input in guessed_letters:
#             print("Эта буква уже использовалась!")
#             continue
#
#         guessed_letters.add(user_input)
#         if user_input not in secret_word:
#             attempts -= 1
#
#
# if __name__ == "__main__":
#     game()










# def foo(name, surname, age):
#     print(name, surname, age)
#
#
# foo(name='Ivan', age=25, surname='Petrov')


#################################################
# pip install flake8
# flake8 1.py
########################################################

# from faker import Faker
# import requests
# import requests
# from faker import Faker
# import datetime

#
# def sin1(alfa):
#     import math
#     a = 1 + 2
#     b = a ** 2
#     print(b)
#     print()
#     print()
#
#     return math.sin(alfa)
#
#
# a = sin1(45)
# print('a=', a)
# #
# #
# #
# url_mono = 'https://api.monobank.ua/bank/currency'
# mono = requests.get(url_mono)
# url_pb = 'https://api.privatbank.ua/p24api/pubinfo?' \
#          'json&exchange&coursid=5&#39'
# privat = requests.get(url_pb)
#
# print('-' * 50)
# print('|             |  PRIVAT \t|  MONOBANK |')
# print('-' * 50)
# print('|DOLL USA sale|', privat.json()[1]['sale'], '\t|',
#       mono.json()[0]['rateSell'], '\t|')
# print('|DOLL USA buy |', privat.json()[1]['buy'], '\t|',
#       mono.json()[0]['rateBuy'], '\t|')
# print('|EURO sale    |', privat.json()[0]['sale'], '\t|',
#       mono.json()[1]['rateSell'], '\t|')
# print('|EURO buy     |', privat.json()[0]['buy'], '\t|',
#       mono.json()[1]['rateBuy'], '\t|')
#
# input("Нажмите Enter для выхода")
# #
# #
# #
# fake = Faker(locale='ru')
#
# print(*dir(fake), sep='\n')
#
# # print(fake.word())
# # print(type(fake.name()), fake.name())
# f = fake.name()
# print(f)
# name = f.split()[0]
# surname = f.split()[1]
# print('name :', name)
# print('surname :', surname)
#
# #
# #
# url = "https://google-translate113.p.rapidapi.com/api/v1/translator/text"
#
# payload = {
#     "from": "auto",
#     "to": "en",
#     "text": "xin chào"
# }
# headers = {
#     "content-type": "application/x-www-form-urlencoded",
#     "X-RapidAPI-Key": "36eb7185f9msh45f7c7652f43036p1fc15fjsn3383c6123fe6",
#     "X-RapidAPI-Host": "google-translate113.p.rapidapi.com"
# }
#
# response = requests.post(url, data=payload, headers=headers)
#
# print(response.json())
# #
# #
# #
# # fake = Faker()
# # print(fake.first_name(), fake.last_name(), fake.words(7))
# #
# # print(*dir(fake), sep='\n')
#
#
# # print(__name__)


# text = 'Hello, world!'
#
# print(f' Я друкую такий напис: {text}')
#


# a = [1, 2]
# print(*dir(a), sep='\n')

# for i in range(5):
#     for j in range(5):
#         print(i, '-', j)


# l = [1, 2, 3]
# l.append(999)
#
# l1 = l.append(999)
# print(l)
# print(l1)
#
# def my_func(text):
#     print(text)
#     return sym
#
#
#
#
# d = my_func('Hello')
# print(d)


# # Вхідні дані у вигляді рядків
# input_data = [
#     "Покупатель1 овар1 5",
#     "Покупатель2 товар1 2",
#     "Покупатель1 вар2 3",
#     "Покупатель3 товар2 1",
#     "Покупатель2 овар3 4",
# ]
#
# # Створення словника для зберігання інформації про покупателів та товари
# customer_data = {}
#
# # Розбиваємо вхідні дані на окремі записи та обробляємо кожен запис
# for line in input_data:
#     parts = line.split()
#     customer = parts[0]
#     product = parts[1]
#     quantity = int(parts[2])
#
#     # Додавання покупця та інформації про товар до словника
#     if customer not in customer_data:
#         customer_data[customer] = {}
#     if product not in customer_data[customer]:
#         customer_data[customer][product] = 0
#     customer_data[customer][product] += quantity
#
# # Сортування покупців та їхніх товарів в лексикографічному порядку
# sorted_customers = sorted(customer_data.keys())
# for customer in sorted_customers:
#     print(customer)
#     sorted_products = sorted(customer_data[customer].keys())
#     for product in sorted_products:
#         print(f"    {product}: {customer_data[customer][product]}")
#

# a = 8
#
# result = 'Ukraine' if a == 1 else 'France'
#
# print(result)


# for i in range(32, 256):
#     print(i, '->', chr(i), '->', chr(i - 32))
# #
#
# def capitalize(symbol):
#     return chr(ord(symbol) - 32)
#
#
# text = input('Введите текст с пробелами : ').split()
# # print(text)
# for i in text:
#     print(capitalize(i[0]) + i[1:], end=' ')


# raise TypeError


# l1 = [1, 2, 3]
# l2 = [1, 2, 3]
#
# print(l1 == l2)
# print(l1 is l2)
#
# print(id(l1))
# print(id(l2))
