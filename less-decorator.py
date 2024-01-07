# def list0():
#     l = [x for x in range(10)]
#     print('l0 : ', *l)
#
#
# def list1():
#     l = [x for x in range(15)]
#     print('l1 : ', *l)
#
#
# # list0()
# # list1()
#
#
# print('=' * 50)
# list0()
# print('+' * 30)
#
# print('=' * 50)
# list1()
# print('+' * 30)
#



####################### Decorator with def ###########
# import time
#
#
# def pr_run(func):
#
#     def wrapper():
#         print('=' * 80)
#         start = time.monotonic()
#         print(func.__name__)
#
#         func()
#
#         print('time of running :', time.monotonic() - start)
#         print('*' * 80)
#
#     return wrapper()
#
#
#
# def pr_run1(func):
#
#     def wrapper():
#         print('0' * 80)
#         print(func.__name__)
#         func()
#         print('0' * 70)
#
#     return wrapper()
#
#
# def list0():
#     l = [x for x in range(10)]
#     time.sleep(1)
#     print('l0 : ', *l)
#
#
# def list1():
#     l = [x for x in range(15)]
#     time.sleep(2)
#     print('l1 : ', *l)


# list0()
# list1()



# print()
#
# pr_run(list0)
# pr_run(list1)
#
# print()
#
# pr_run1(list0)
# pr_run1(list1)


############## with args #################################

#
# def pr_run(func, n, k, s, m):
#
#     def wrapper():
#         print(s * k)
#         print(func.__name__)
#         func(n)
#         print(m * k)
#
#     return wrapper()
#
#
# def list0(n):
#     l = [x for x in range(n)]
#     print('l0 : ', *l)
#
#
# list0(7)
# print()
# print()
# pr_run(list0, 35, 80, '$', '&')




##################################################################
##### Decorator with  @.....  ###################################

# def pr_run(func):
#
#     def wrapper(n):
#         print('*' * 50)
#         print(func.__name__)
#         func(n)
#         print('.' * 50)
#
#     return wrapper
#
#
#
# @pr_run
# def list1(n):
#     l = [x for x in range(n)]
#     print('l1 : ', *l)
#
#
#
#
#
# @pr_run
# def list2(n):
#     l = [x for x in range(n)]
#     print('l2 : ', *l)
#
#
# list1(5)
# list2(7)


####### With 2nd args ########

# def pr_run(func):
#
#     def wrapper(n, k=30):
#         print('*' * k)
#         print(func.__name__)
#         func(n)
#         print('*' * k)
#
#     return wrapper
#
#
# @pr_run
# def list0(n, k):
#     l = [x for x in range(n)]
#     print('l0 : ', *l)
#
# @pr_run
# def list1(n, k):
#     l = [x for x in range(n)]
#     print('l1 : ', *l)
#
#
# list0(7, 10)
# list1(5, 80)


#######################################################
######### time ########################################
#######################################################
# import time
#
#
# def run_time(func):
#
#     def wrapper(n):
#         start = time.time()
#         func(n)
#         print(func.__name__, time.time() - start)
#
#     return wrapper
#
#
# # @pr_run
# @run_time
# def list1(n):
#     l = []
#     for i in range(n*2):
#         l.append(i)
#     print('l1 append:')
#
#
# # @pr_run
# @run_time
# def list2(n):
#     l = [x for x in range(n*2)]
#     print('l2 generator:')
#
#
# # @pr_run
# @run_time
# def list3(n):
#     l1 = []
#     l2 = []
#     for i in range(n*2):
#         if i % 2:
#             l1.append(i)
#         else:
#             l2.append(i)
#     l = l1 + l2
#     print('l3 append+append:')
#
#
# n = int(input('n = '))
# # list1(n)
# # list2(n)
# # list3(n)
#
#
#
# @pr_run
# @pr_run
# @run_time
# def count_(n, k=40):
#     s = [x*4-x**2+7 for x in range(n*2)]
#     print('x*4-x*2+x*7 :', sum(s))
#
# count_(n)
# ############################################################













# from datetime import datetime
#
# def time_run(func):
#
#     def wrapper(*args, **kwargs):
#         start = datetime.now()
#         func(*args, **kwargs)
#         result = datetime.now() - start
#         return result
#
#     return wrapper
#
# @time_run
# def list_app(n):
#     l = []
#     for i in range(n):
#         l.append(i)
#     return l
#
# @time_run
# def list_gen(n):
#     l = [x for x in range(n)]
#     return l
#
# print(list_app(100000))
# print(list_gen(10**5))


