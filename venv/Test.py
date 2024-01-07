# def decor(func):
#     def inner():
#         print('=======')
#         func()
#         print('!!!!!!!!!!!')
#     return inner()
#
# @decor
# def func():
#     print('Hello World!')
#
# dR =1
# AXby = 1
# # R&B = 1
# # 4Wheel = 1
# Вася = 1
# # “PesBarbos” = 1
# TU154 = 1
# # [QuQu] = 1
# _ABBA = 1
# # A+B = 1
#
# import copy
# n = 3
# m = 4
# a = [[0] * m] * n
# # a = [0] * m
# b = copy.deepcopy(a)
# print(a, b)
# a[0][0] = 1
# print(a, b)
# a[0][0] = 5
# a[0][1] = 6
# a[2][2] = 6
# print(a, b)

# x = 1/30000
# print("{:e}".format(x))
# x = 12345678
# print("{:e}".format(x))

# x = 123.456
# print("{:e}".format(x))
# print("{:10.2e}".format(x))

# d = input().split()
# print('d=', d)
# a, b = map ( str, d )
# print('a=', a, 'b=', b)
# print(*d)
# a, b = map ( int, d )
# print('a=', a, 'b=', b)
# b, a = a, b
# print('a=', a, 'b=', b)
#
# n, m = map(int, input().split())
# a = [0] * n
# max_ = ['*'] * n
# for i in range(n):
#     a[i] = input().split()
#     max_[i] = max(map(int, a[i]))
# max = max(max_)
# for i in range(n):
#     for j in range(m):
#         if int(a[i][j]) == max:
#             break
#
# x = 4
# y = 15.67
# z = 20
# # print("%02d;%02d-%02d" % (x,y,z))
# print("{1:8f};{1:8f}-{2:8f}".format (x,y,z))
#
# print(3**3**3)
print(3**27)
print(27**3)