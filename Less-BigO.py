import time
import random


# def run_time(func, num):
#     def wrapper(num):
#         res = 0
#         r = 1000
#         for i in range(r):
#             start = time.monotonic_ns()
#             func(num)
#             res += time.monotonic_ns() - start
#         print(func.__name__, 'time =', res)
#         return res
#     return wrapper(num)
#
#
#
# def fact1(n):  # 1*2*3*4*5 -> 5!
#     result = 1
#     for i in range(n):
#         result *= (i+1)
#     return result
#
#
# def fact2(n):  # 5*4*3*2*1 -> 5!
#     if n == 1:
#         return 1
#     else:
#         return n * fact2(n-1)
#
#
#
# x = 200
# for i in range(5):
#     res1 = run_time(fact1, x)
#     res2 = run_time(fact2, x)
#     if res1 < res2:
#         print('time of func1 <<<< time of func2\n')
#     else:
#         print('time of func1 >>>> time of func2\n')




# ===============================================================================
#                O(1)
# ===============================================================================
import matplotlib.pyplot as plt


def my_plot(x, y):
    print('x :', x)
    print('y :', y)
    plt.plot(x, y)
    # plt.plot(x, y, 'g+')
    # plt.plot(x, y, 'o')
    # plt.plot(x, y, 'rx')
    # plt.plot(x, y, 'yo')
    # plt.plot(x, y, 'b')

    plt.xlabel('Inputs')
    plt.ylabel('Steps')
    plt.title('Function O()')

    plt.show()


# def big_o1(data: list, count=0):
#     result = data[0] # якась операція, що не залежить від довжини data
#     count += 1
#     return count
#
#
# y = []
# n = 10 #  кількість даних
# for i in range(n):
#     count = 0
#     y.append(big_o1([el for el in range(n)]))
#     print(y)
#
# x = [el for el in range(n)] #  кількість даних
# my_plot(x, y)



# ================================================================
#                    O(n)
# ================================================================
#
# def big_on(data: list):
#     global count
#     for i in data:
#         result = i
#         count += 1
#     return count
#
#
# y = []
# n = 80
#
# for i in range(n):
#     count = 0
#     y.append(big_on([el for el in range(i)]))
#
# x = [el for el in range(n)] #  кількість даних
#
# my_plot(x, y)






# # =======================================================================
# #                        O(2n)   (при n->нескінченність O(n))
# # =======================================================================
#
# def big_on(data: list):
#     global count
#
#     for i in range(len(data)):
#         result = data[i]
#         count += 1
#
#     for i in range(len(data)):
#         result = data[i]
#         count += 1
#
#     return count
#
#
# y = []
# n = 20
# for i in range(n):
#     count = 0
#     y.append(big_on([el for el in range(i)]))
# x = [el for el in range(n)] #  кількість даних
# my_plot(x, y)
# #




# =======================================================
#                   O(n^2)
# =======================================================
# def big_on2(data: list):
#     global count
#
#     for i in range(len(data)):
#         for j in range(len(data)):
#             result = data[j]
#             count += 1
#     return count
#
#
# y = []
# n = 20 #  кількість даних
# for i in range(n):
#     count = 0
#     y.append(big_on2([el for el in range(i)]))
# x = [el for el in range(n)]
# my_plot(x, y)
#
#



# ==================================================================
#                            O(1/n)  вимишлений і не реальний
# ==================================================================

#
# def big_o2_n(data: list):
#     global count
#     for i in range(len(data)):
#         result = data[i]
#         count += 1
#     return count
#
#
# y = []
# n = 20
# for i in range(n):
#     count = 0
#     y.append(big_o2_n([el for el in range(n-i)]))
# x = [el for el in range(n)] #  кількість даних
# my_plot(x, y)

#
#
#
#


# ==================================================================
#                            O(1/n^2)  вимишлений і не реальний
# ==================================================================
# def big_on2(data: list):
#     global count
#
#     for i in range(len(data)):
#         for j in range(len(data)):
#             result = data[j]
#             count += 1
#     return count
#
#
# y = []
# n = 8
# for i in range(n):
#     count = 0
#     y.append(big_on2([el for el in range(n-i)]))
# x = [el for el in range(n)] #  кількість даних
# my_plot(x, y)





# ==========================================================
#                   O(log(n))  вимишлений
# ==========================================================
# import random
#
#
# def func(num):
#     count = 0
#     my_list = []
#     for i in range(num):
#         el = random.randint(1, 100)
#         if el not in my_list:
#             my_list.append(el)
#             count += 1
#     # print(*my_list)
#     return count
#
#
# y = []
# n = 1000
# x = [el for el in range(n)]
# for i in range(n):
#     y.append(func(i))
# my_plot(x, y)


# ========================================================
#  Складні комплексні алгоритми
# ========================================================
# def big_on_cmpl(data: list):
#     global count
#
#     for i in (1, 2, 3): #   O(3)
#         result = i
#         count += 1
#
#     for i in range(len(data)): #   O(n)
#         result = data[i]
#         count += 1
#
#
#     for i in range(len(data)): #   O(2n)
#         result = data[i]
#         count += 1
#     for i in range(len(data)):
#         result = data[i]
#         count += 1
#
#
#     for i in range(len(data)):  #   O(n^2)
#         for j in range(len(data)):
#             result = data[j]
#             count += 1
#
#     return count
#
#
# y = []
# n = 10
# for i in range(n):
#     count = 0
#     y.append(big_on_cmpl([el for el in range(i)]))
# x = [el for el in range(n)] #  кількість даних
# my_plot(x, y)





# '''
# O(?) = O(3) + O(n) + O(2n) + O(n^2) = O(n^2 + 3n + 3) ---> O(n^2)
# '''


# ==============================================================
#      Найкращій і найгірший
# ==============================================================
# def my_search(number: int, data: list):
#     global count
#     while data:
#         el = data.pop(random.randint(0, len(data)-1))
#         count += 1
#         print(el, number)
#         if el == number:
#             return count
#     return count
#
#
# data_run = [el for el in range(36)]
# n = 4 # Найкращій результат О(1), найгірший О(n), середньовипадковий O(n/2) -> O(n)
# y = []
# x = [el for el in range(len(data_run))]
# for i in x:
#     count = 0
#     data = data_run.copy()
#     y.append(my_search(n, data))
# my_plot(x, y)


# ==============================================================
#      Просторова складність алгоритму
# ==============================================================
# '''
# Просторова складність харектиризує задіяність пям'яті та нових змінних
# Наприклад, якщо для виконання алгоритму вам прийдеться створити 1 нову змінну,
# то така просторова складність буде О(1).
# Якщо вам потрібно дублювати всі вхідні дані, то це вже буде O(n).
# Дивись приклад:
# '''

#
# import sys
# from memory_profiler import memory_usage, profile
#
#
#
# @profile
# def my_func(data: list):
#     result = []
#     for el in data:
#         result.append(el * el)
#     print('my_func :', sys.getsizeof(my_func) + sys.getsizeof(el)+ sys.getsizeof(result) + sys.getsizeof(data))
#     return result
#
# # # @profile
# def my_func1(data: list):
#     result = []
#     for i in range(len(data)):
#         result.append(data[i] * data[i])
#     print('my_func1 :', sys.getsizeof(my_func1)+sys.getsizeof(data)+sys.getsizeof(result))
#     return result
#
# # # @profile
# def my_func2(data: list):
#     print('my_func2 :', sys.getsizeof(my_func2))
#     return [el * el for el in range(n1, n2, step)]
#
#
# data = [2, 4, 6, 8, 10]
# n1, n2, step = 2, 1111, 2
# data = [i for i in range(n1, n2, step)]
# print(data)
# my_func(data)
# # print(my_func(data))
# my_func1(data)
# # print(my_func1(data))
# my_func2([])
# # print(my_func2(data))
# #
# # print(memory_usage())





################# END ##############
# import os, psutil
# process = psutil.Process(os.getpid())
# print(process.memory_info().rss)
# befor = process.memory_info().rss

# print(process.memory_info().rss)
# now = process.memory_info().rss
# print(befor-now)