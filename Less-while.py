
# n = int(input('Input number of steps in cycle : '))
# sum_ = 0
# for i in range(n):
#     num = int(input('input number : '))
#     if num == 0:
#         break
#     sum_ += num
#     print('step No.', i, sum_)
# else:
#     print('number of the cycle over')
# print('===== Sum =', sum_, 'Finish!!!!')




# sum_ = 0
# count = 0
# n = int(input('Input number of steps in cycle : '))
# num = 1
# while True:                          # 0  0.0    False  ''  []  ()
#     num = input('input number : ')
#     count += 1
#     if num == ' ':
#         print('break!!!!!!!!!!!!!!!')
#         break
#     sum_ += int(num)
#     if not num:
#         print('FINISH')
#     else:
#         print(num, end=' ')
# print('sum =', sum_, 'count=', count, '===FINISH====')


# i = 0
# s = input('Введите символ :')
# text = 'Hello, world!'
# while i < len(text):
#     print(text[i])
#     if text[i] == s:
#         print('break')
#         break
#     i += 1
# else:
#     print('No break!!!!!!!!!')
# print('!!!!!!!!!!Alarm!!!!!')



# n = int(input('Input number of cycles : '))
# sum_ = 0
# num = True
# while n and num:
#     num = int(input('Input symbol : '))
#     sum_ += num
#     n -= 1
# print('='*60)
# print(sum_)
# print('='*60)



# text = 'Hello, world!'
# n = len(text)
# for i in text:
#     if i == 'o':
#         break
#     print(i, end='-')
# while n:
# while n and text[-n] != 'o':
#     print(text[-n], end='-')
#     n -= 1






# n = int(input('Input number of steps in cycle : '))
# a = n
# while a > 0:
#     print('step No.', n - a + 1)
#     a -= 1
#     if a < 0:
#         break
# # print('Finish!!!!')
# else:
#     print('Finish!!!!')




# sum_ = 0
# n = True
# # while True:
# while n != 0:
#     n = input('Input number or "0"(for count sum) : ')
#     if n == '' or not n.isdigit():
#         print('Input only numbers, please!')
#         continue
#     n = int(n)
#     # if n == 0:
#     #     break
#     sum_ += n
# print('Sum = ', sum_)


# text = 'Input integer number or "0"(for count sum) : '
# number = '0'
# count = 0
# count1 = 0
# err = 0
# sum_ = int(number)
# while number:
#     count += 1
#     number = input('Input number :')
#     if not number or not number.isdigit():
#         print('Input only integer numbers, please!')
#         number = '0'
#         err += 1
#         continue
#     count1 += 1
#     number = int(number)
#     sum_ += number
# print('The cycle took', count, 'steps. And ', count1, 'but', err, 'of them is ERROR!')
# print('Sum = ', sum_)








# text = input('Input word, please : ')
# attempt = len(text)
# n = 40
# while attempt:
#     symbol = input('Input a symbol, please: ')
#     if text.count(symbol):
#         print('\n' * 3)
#         print('!' * n)
#         print('You win!!!'.center(n, ' '))
#         print(('The symbol "' + symbol + '" is in the text !').center(n, ' '))
#         print('!' * n)
#         break
#     print()
#     attempt -= 1
#     print('No symbol "' + symbol + '" in the word!')
#     print('Try again, please! You have', attempt, 'attempts.')
# else:
#     print('=' * n)
#     print("Sorry, You don't have any attempt...")
#     print('=' * n)




import random

text = 'abcdefg'
for i in range(10):
    print(random.choice(text))
    print(int(random.random()*100))
    print(random.randint(0, 100))

# print(*dir(random), sep='\n')
# !!!!!!!!!!!!!!!! 21
# total = 0
# cont = 'y'
# a = random.randint(1, 10)
# while cont == 'y':
#     a = random.randint(1, 10)
#     total += a
#     print(a, total)
#     if total > 21:
#         print('You lost! Total sum is', total)
#         break
#
#     cont = input('play? (y/n) :')
# else:
#     print('You win! Total sum is less than 21 and is equal to', total, '.')
#

# for i in range(10):
#     print(random.randint(1, 100))



# найменший дільник 289

# n = int(input())
# i = 2
# while n % i != 0:
#     i += 1
# print(i)






# my_text = input('text :')
# i = 0
# for i in my_text:
#     if i == 3:
#         break
#     print(i)
# while i < len(my_text):


# while (i < len(my_text)) and (i != 3):
#     print(my_text[i])
#     i += 1


# password = "qwerty123"
# user_input = ""
# while user_input != password:
#     user_input = input("Введіть пароль: ")
# print("Доступ відкрито.")



# while True:
#     user_input = input("Введіть команду для виходу: ")
#     if user_input == "exit":
#         print('Вірно!')
#         break
#     else:
#         print("Команда не вірна.")


import random

# for i in range(10):
#     print(random.randint(1, 2))


# print(*dir(random), sep='\n')



# lst = ['Bob', 'Jon', 'Ann']
# for i in range(10):
#     print(random.choice(lst))


# number = random.randint(1, 10)
# while True:
#     guess = int(input("Вгадай число від 1 до 10: "))
#     if guess == number:
#         print("Вітаю! Ви вгадали число.", guess)
#         break
#     else:
#         print("Помилка. Спробуй ще раз.")


# n = 85
#
#
# binary = ''
# while n > 0:
#     binary = str(n % 2) + binary
#     # print(binary)
#     n //= 2
# print(binary)



# Завдання
# Надрукуйте таблицю множення за допомогою циклу while


# i = 1
# while i <= 10:
#     j = 1
#     while j <= 10:
#         print(i, "*", j, "=", i*j)
#         j += 1
#     i += 1


# for i in range(1, 11):
#     for j in range(1, 11):
#         # print(f"{i} * {j} = {i*j}")
#         print(i, "*", j, "=", i*j)





#  0 1 1 2 3 5 8

#   a, b = b, a+b