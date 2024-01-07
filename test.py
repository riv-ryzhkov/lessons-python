import copy

a = [1, [2], 3]
b = a
print(a[1] is b[1])



# s = {8, 1, 2, 3, 4, 'a', 'b'}
#
# n = iter(s)
# print(next(n))
# print(next(n))
# print(next(n))
# print(next(n))
# print(next(n))
# print(next(n))
# print(next(n))
# print(next(n))


#
# l = [1, 2, 3, 4]
#
# def iter(lst: list):
#     for i in lst:
#         yield i
#
#
# n = iter(l)
# print(next(n))
# print(next(n))
# print(next(n))
# print(next(n))
# print(next(n))

#
# def decor(func):
#     def inner(num):
#         print('Start')
#         func(num)
#         print("finish")
#     return inner
#
#
#
# #
# @decor
# def foo(num):
#     print('Hello, world!', num)
#
#
# # decor(foo)
# #
# foo(5)





# a = (1, 2, [3, 4])
# a[-1].append(5)
# print(a)



# d = 87
# print(*dir(d), sep="\n")




#
# def null(sv):
#     for r in range(3):
#         print(*sv[r])
#
#
# sv = []
# for r in range(3):
#     sv.append(['.', '.', '.'])
# m = -1
#
#
# def place(P):
#     for s in ['0', 'x']:
#         for r in range(3):
#             if P[r][0] == P[r][1] == P[r][2] == s or P[0][r] == P[1][r] == P[2][r] == s:
#                 return True
#         if P[0][0] == P[1][1] == P[2][2] == s or P[0][2] == P[1][1] == P[2][0] == s:
#             return True
#
#
# def checkout(d):
#     if len(d) != 3 or d[1] != " " or not d[0].isdigit() or not d[2].isdigit():
#         null(sv)
#
#         return False
#     z = int(d[0])
#     x = int(d[2])
#     if z < 1 or z > 3 or x < 1 or x > 3:
#         null(sv)
#         return False
#     if sv[z - 1][x - 1] != '.':
#         null(sv)
#         return False
#
#     return True
#
#
# def step(sv, m) -> object:
#     while True:
#         d = input('Ваш ход?')
#         if checkout(d):
#             d = d.split()
#         else:
#             continue
#         if m == 1:
#             sv[int(d[0]) - 1][int(d[1]) - 1] = '0'
#         else:
#             sv[int(d[0]) - 1][int(d[1]) - 1] = 'x'
#         return sv
#
#
# win = False
# while win == False:
#     sum = 0
#     for r in range(3):
#         sum += sv[r].count('.')
#     if sum == 0:
#         m = 0
#     if place(sv) or m == 0:
#         win = True
#         break
#     m *= -1
#     null(sv)
#     if m == 1:
#         print('0')
#     else:
#         print('x')
#     step(sv, m)
#
#
#
# # import random
# #
# # cards = [i for i in range(1, 31)]
# # print(cards)
# # command = ''
# # while command == '' and cards:
# #     n = random.randint(0, len(cards)-1)
# #
# #     # print(n)
# #     print('Ваш білет : ', cards.pop(n))
# #     print(cards)
# #     command = input('Ще білет? Натисни <Enter>')
# # print('=' * 80)
# # print('           The END !   ')
# # print('=' * 80)
# #
# # #
# # # import random
# # #
# # #
# # # def input_word():
# # #     print("Input a secret word:")
# # #     sec_word = input()
# # #     sec_word = sec_word.lower()
# # #     return sec_word
# # #
# # #
# # # def make_sec_list(size):
# # #     sec_list = []
# # #     for i in range(size):
# # #         sec_list.append(input_word())
# # #     return sec_list
# # #
# # #
# # # def start_game(sec_word, lives):
# # #     orig_word = str(sec_word)
# # #     used_letters = []
# # #     guessed_word = []
# # #     for i in range(len(sec_word)):
# # #         guessed_word.append('_')
# # #     while True:
# # #         print("Your lives: " + str(lives))
# # #         print("Your word: " + "".join(guessed_word))
# # #         if len(used_letters) > 0:
# # #             print("You used letters: " + ", ".join(used_letters))
# # #         print("input letter: ")
# # #         letter = input()[0]
# # #         letter = letter.lower()
# # #         if letter in sec_word:
# # #             while letter in sec_word:
# # #                 index = sec_word.index(letter)
# # #                 guessed_word[index] = letter
# # #                 sec_word = sec_word.replace(letter, "#")
# # #         else:
# # #             print("Wrong!")
# # #             lives = int(lives) - 1
# # #         if letter not in used_letters:
# # #             used_letters.append(letter)
# # #         if orig_word == "".join(guessed_word):
# # #             print("You win!")
# # #             break
# # #         elif int(lives) <= 0:
# # #             print("You lose!")
# # #             break
# # #     print("".join(guessed_word))
# # #
# # #
# # # if __name__ == "__main__":
# # #     print("Input secret word or choose random? (i/r):")
# # #     ans = input()
# # #     ans = ans.lower()
# # #     print("Input count of lives:")
# # #     lives = input()
# # #     if ans == 'i':
# # #         start_game(input_word(), lives)
# # #     elif ans == 'r':
# # #         print("Input count of words:")
# # #         size = input()
# # #         sec_list = make_sec_list(int(size))
# # #         word_num = random.randint(0, len(sec_list) - 1)
# # #         start_game(sec_list[word_num], lives)
# # #     else:
# # #         print("Wrong answer!")
# #
# # # list1 = [1, 2, 3, 4, 5]
# # # res = list1.append(6)
# # # print(list1)
# #
# #
# # #
# # # a = (1, 2, 3, 4)
# # # a[-1] = 5
# # # print(a)
# #
# #
# # # a = [1, 2, [3, 4]]
# # # a[-1] = 5
# # # print(a)
# # #
# # # a = {}
# # # b = {2}
# # # print(type(a), type(b))
# # #
# # # a = (1)
# # # b = (2,)
# # # print(type(a), type(b))
# # #
# # # a = {4, 1, 2, (2, 5, 3), 1, 2, 'Hello', 5, 1, '2', 3}
# # # print(len(a))
# # #
# # # a = (1, 2, [3, 4])
# # # a[-1].append(5)
# # # print(a)
# # #
# # #
# # # def sum(x, y):
# # #     return x - y
# # #
# # #
# # # print(sum(5, -10))
# #
# #
# # # text = '0123456789012345678901234567890'
# # # text1 = ''
# # # print(text, len(text))
# # # for i in range(0, len(text), 3):
# # #     text1 += text[i+1:i+3]
# # #     print(i, end='  ')
# # # print()
# # # print(text1, len(text1))
# #
# #
# # # try:
# # #     a = 10/0
# # # except ZeroDivisionError:
# # #     raise ValueError
# #
# #
# # # elem = [1, 2, 3, 4, 2, 3, 4, 1, 2, 3, 2, 3, 4, 3]
# # # res = 0
# # # for i in range(1, len(elem)-1):
# # #     if elem[i-1] <= elem[i] > elem[i+1]:
# # #         res += 1
# # #         print(elem[i])
# # # print('res =', res)
# # # text = '123456789123456789123456789'
# # # for i in range(2, len(text), 3):
# # #     print(text[i], end=' ')
# #
# #
# # # text = 'Hello'
# # # word = text.casefold()
# # # print(text)
# # # print(word)
# #
# #
# # # n = int(input('n = '))
# # # m = int(input('m = '))
# # # if n < m:
# # #     n, m = m, n
# # # x = int(input('x = '))
# # # y = int(input('y = '))
# # # print(min(x, y, m-x, n-y))
# #
# # # a = 0
# # # print('Number > 0' if a > 0 else 'Number < 0')
# #
# # # import re
# # #
# # # match = re.search(r'\d\d\D\d\d', r'Телефон 1231212')
# # # print(match[0] if match else 'Not found')
# # #
# # # match = re.fullmatch(r'\s*\d\d\D\d\d', r'12-12')
# # # print('YES' if match else 'NO')
# # #
# # # print(re.split(r'\W{2}', 'Где, скажите мне, мои очки??!'))
# # #
# # # for m in re.finditer(r'\d\d\.\d\d\.\d{4}', r'Эта строка написана 19.01.2018, а могла бы и 01.09.2017'):
# # #     print('Дата', m[0], 'начинается с позиции', m.start())
# #
# #
# # # import json
# # # print(json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]'))
# # # print(json.loads('"\\"foo\\bar"'))
# #
# #
# # # print([1] * 5)
# # #
# # # a = [1]
# # # b = a
# # # b[0] = 2
# # # print(a, b)
# # #
# #
# # #
# #
# #
# # # n = 5
# # # a = [[0] * n for i in range(n)]
# # # print(a)
# #
# # # a = [[i * j for i in range(1, 11)] for j in range(1, 11)]
# # # n = 7
# # # a = [[2] * n for i in range(n)]
# # # # for i in range(n):
# # # #     for j in range(n):
# # # #         if i < j:
# # # #             a[i][j] = 0
# # # #         # elif i == j:
# # # #     a[i][i] = 1
# # # # a = [['#'] * i + ['*'] + ['+'] * (n - 1 - i) for i in range(n)]
# # # a = [[int(j) for j in input().split()] for i in range(int(input()))]
# # # for i in a:
# # #     print(*i, sep='\t')
# # #
# # #
# # #
# #
# #
# # # a = [0, 0, 0]
# # # b = [a] * 5
# # # a[0] = 1
# # # print(b)
# #
# #
# # # a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
# # # for i in range(len(a)):
# # #     for j in range(len(a[i])):
# # #         print(a[i][j], end=' ')
# # #     print()
# #
# # #
# # # for row in a:
# # #     print(' '.join([str(elem) for elem in row]))
# #
# # # for i in a:
# # #     print(*i)
# #
# #
# # # SUMMA
# # # a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
# # # s = 0
# # # for row in a:
# # #     for elem in row:
# # #         s += elem
# # # print(s)
# #
# # # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# # # n = 3
# # # m = 4
# # # a = [[0] * m] * n
# # # a[0][0] = 5
# # # print(a[1][0])
# #
# # # ++++++++++++++++++++++++
# # # n = 3
# # # m = 4
# # # a = [0] * n
# # # for i in range(n):
# # #     a[i] = [0] * m
# #
# # # Generator
# # # n = 3
# # # m = 4
# # # a = [[0] * m for i in range(n)]
# #
# # # n = 3
# # # m = 4
# # # a = [[0] * m] * n
# # # print(a)
# # # a[0][0] = 5
# # # print(a)
# #
# #
# # # !!!!!!!!!!INPUT
# # # в первой строке ввода идёт количество строк массива
# # # n = int(input())
# # # a = [[int(j) for j in input().split()] for i in range(n)]
# # # a = [[int(j) for j in input('number = ').split()] for i in range(int(input('n= ')))]
# # # for i in a:
# # #     print(*i)
# #
# #
# # # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# # # n, m = 10, 10
# # # a = [[i * j for j in range(1, m)] for i in range(1, n)]
# # # for i in a:
# # #     print(*i, sep='\t')
# #
# #
# # # n = int(input(' input n= '))
# # # symbol = input(' input symbol = ')
# # # for i in range(n):
# # #     for j in range(n-i):
# # #         print(symbol, ' ', end='')
# # #     print()
# #
# # # def reverse():
# # #     s = input()
# # #     if s != '0':
# # #         reverse()
# # #     print(s)
# # #
# # # reverse()
# #
# # # def fact(n):
# # #     if n == 1:
# # #         return n
# # #     return fact(n-1) * n
# # #
# # # print(fact(3))
# # #
# # # def fibonacci(n):
# # #     def fib(n):
# # #         if n == 0 or n == 1:
# # #             return n
# # #         else:
# # #             return fib(n-1) + fib(n-2)
# # #     for i in range(0, n+1):
# # #         print(fib(i))
# #
# #
# # # fibonacci(6)
