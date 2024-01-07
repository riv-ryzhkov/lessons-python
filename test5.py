# player = -1
#
#
# player *= -1
#
#
#
# if player == -1:
#     print('Игрок 2')
# elif player == 0:
#     print('Ничья')
# else:
#     print("Игрок 1")
#
#
#
#
#
#
#
#
# # def validator(symbol):
# #     if symbol:
# #         return True    #  45.129.1  192.168.104   255.255.255  0.0.0
# #     else:
# #         return False  # 128.23  267.1.23  234.122.45.123  1..127  192.-168.1 a.23.F4
# #                       #  25. 127.56    126.*.234    .127.234
# #
# #
# # text = input('Введите IP : ')
# # if validator(text):
# #     print('Проверка пройдена! \nВаш IP ', text)
# # else:
# #     print('Такого IP  не бывает!!!')
#
#
# # #
# # def display(array):
# #     print()
# #     for i in range(3):
# #         print(*array[i])
#
# #
# # array = []
# # for i in range(3):
# #     array.append(['.', '.', '.'])
#
#
# # display(array)
# # print(array)
# # array[1][2] = 'X'
# # display(array)
# # array[2][2] = '0'
# # display(array)
# # array = [
# #     ['0', '0', '0'],
# #     ['X', 'X', 'X'],
# #     ['0', '.', '.']
# # ]
# # display(array)
# #
# #
# def check(array):
#     for symbol in 'X', '0':
#         for i in range(3):
#             if array[i][0] == array[i][1] == array[i][2] == symbol:
#                 # if symbol == 'X' or symbol == '0':
#                 return symbol
# #     sum = 0
# #     for i in range(3):
# #         sum += array[i].count('.')
# #     if sum:
# #         return 'Играем дальше!!!!!!!'
# #     else:
# #         player = 0
# #         return 'stop'
# #
# #
# # if check(array) == 'X':
# #     print('Победил 1-й игрок')
# # elif check(array) == '0':
# #     print('Победил 2-й игрок')
# # elif check(array) == 'stop':
# #     print('Ничья!!!!!!')
# # else:
#
#
# # print(check(array))
# #
# # #
# # # print(check([
# # #     ['X', 'X', '0'],
# # #     ['.', 'x', '0'],
# # #     ['.', '.', '0']]))
# #
# #
# # #
# #
# #
# #
# # ###############################################
# # def validate(num):
# #     n = num.split('.')
# #     if len(n) != 3:
# #         print('IP должен содержать три блока по трехзначному числу 0...255')
# #         return False
# #     for i in n:
# #         if not i.isdigit():
# #             print('Буквы в IP недопустимы!')
# #             return False
# #         if int(i) < 0 or int(i) > 255:
# #             print('Адрес должен быть в диапазоне 0...255')
# #             return False
# #     return True
# #
# #
# # valid = False
# # while valid == False:
# #     num = input('Введите IP : ')
# #     valid = validate(num)
# # print('Прекрасно!\n Ваш IP  ', num)
# # #
#
#
# #
# # ####################################################
# # # l = ['x..', '0x.', '000']
# # # for k in ['x', '0']:
# # #     for i in range(3):
# # #         if l[i][0] == l[i][1] == l[i][2] == k or l[0][i] == l[1][i] == l[2][i] == k:
# # #             print('!' * 20)
# # #     if l[0][0] == l[1][1] == l[2][2] == k or l[0][2] == l[1][1] == l[2][0] == k:
# # #         print('************************')
# # # print('=====')
# #
#
#
# #
# # from less_Decorator import pr_run
# #
# # def foo():
# #     print('1111111111111111111111')


