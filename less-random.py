# import random
#
# # Генерируем случайное целое число от 1 до 10
# random_number = random.randint(1, 10)
# print(random_number)


# import random
#
# # Генерируем случайное число с плавающей точкой от 0 до 1
# random_float = random.random()
# print(random_float)
#
# # Генерируем случайное число с плавающей точкой от 0 до 10
# random_float = random.uniform(0, 10)
# print(random_float)


# import random
#
# my_list = ["apple", "banana", "cherry"]
# # random_element = random.choice(my_list)
# random_element = random.choices(my_list, k=10)
# print(random_element)


import random
# import string
#
#
# print(*dir(string), sep='\n')
# print(string.ascii_uppercase)
# print(string.ascii_lowercase)
# print(string.digits)
# print(string.hexdigits)
# print(string.punctuation)
# print(string.printable)
# # Генерируем случайную строку из 10 символов, состоящую из цифр и букв в верхнем и нижнем регистре
# random_string = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=10))
# print(random_string)







# import random
# from collections import Counter
#
# words = ["кошка", "собака", "слон", "бегемот", "кавалерист"]
# list_of_words = []
# for i in range(20):
#     word = random.choice(words)
#     list_of_words.append(word)
#     print(word)

#################################
# print('=' * 60)
# print('STATISTIC :')
# print('=' * 60)
# c = Counter(list_of_words)
# print('c : ', c, type(c))
# prn_res = list(c.items())
# prn_res.sort(key=lambda x: x[1], reverse=True)
# for row in prn_res:
#     print(*row, sep='\t')


#
# lst = [5, 6, 7, 1, 3, 9, 9, 1, 2, 5, 5, 7, 7]
# c = Counter(lst)
# print('lst : ', c, type(c))


# operators = ['+', '-', '/', '*']
# a = input('первое число: ')
# b = input('второе число: ')
#
# q = random.choice(operators)
#
# r = eval(a + q + b)
# print('Выполняем операцию <', q, '> :', sep='')
# print(a + q + b, '=', r)
# print('Результат ', r)


# print(eval(str(4+2)))