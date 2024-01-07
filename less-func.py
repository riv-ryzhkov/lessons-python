# my_list = [1, 2, 3]
#
# summa = sum(my_list)  # function sum()
# print(summa)






############


# def my_sum(my_list):
#     summa = 0
#     for element in my_list:
#         summa += element
#     return summa
#
#
# my_list = [1, 2, 3]
# print(my_sum(my_list))


##############################

# def say_hello():
#     print('Hello!')
#
#
# say_hello()
# print(res)
# print(say_hello())  # !!!!!!!!!!!!!!!!!!!!!!!!!

#########################################


# def say_hello(name):
#     print(f'Hello, {name}! Have a nice day!')
#
#
# # name = 'Alex'
# # say_hello(name)
# say_hello('Max')
# say_hello('Everybody')
# say_hello('Everybody')
# say_hello('Everybody')
# say_hello('Everybody')
# say_hello('Everybody')

###########################################



# def say_hello(name='NoName', ask='How are you!'):
#     print(f'Hello, {name}! {ask}')
#
#
# say_hello()
# say_hello('Max')
# say_hello('Max', 'How old are you?')


# name = 'Alex'
# say_hello(name)
# say_hello(name, 'How old are you?')

###############################

# def get_name():
#     name = input('What is your name :')
#     return name
#
#
# def say_hello(name):
#     print(f'Hello, {name}!')
#
#
# # my_name = get_name()
# # # print(my_name)
# # say_hello(my_name)
#
# say_hello(get_name())

#########################################
############## LAMBDA #############


# def sum_two(a, b):
#     return a + b
#
#
# print(sum_two(4, 5))
#
#
# func1 = lambda a, b: a + b
# print(func1(4, 5))
#
#
# print((lambda a, b: a + b)(4, 5))


# say_hi = lambda name: f'Hi, {name}!'
# print(say_hi('Alex'))


#########################################################




# def my_sum(a=0, b=0, c=0, d=0):
#     return a + b + c + d
#
#
# # print(my_sum(3, 4, 7, 2))
# # print(my_sum(3, 4))
# # print(my_sum(3, 4, 5))
# print(my_sum(3, 4, 5, 6, 7, 8))




# def my_sum(*args):
#     res = 0
#     print(type(args), args)
#     for i in args:
#         res += i
#     return res
#
#
# print(my_sum(5, 6, 8, 9, 6, 7, 8, 9, 9, 0, 4, 6, 7, 9))




# def foo():
#
#     def inner_func():
#         a = 0
#         print(a)
#     inner_func()
#     return 'Hello!'
#
# # result = foo()
# # print(result)
# inner_func()

#######################################


# def my_func(var):
#     # global a
#     # a += 1
#     var += 1
#     return var
#     # print('a in my_func() =', a)
#
#
# a = 9
# a = my_func(a)
# a = my_func(a)
# a = my_func(a)
# print('a in programme =', a)

##################################################


# def my_sum(x):
#     print('Купи калькулятор!')
#     # return x
#     return sum(x)
#
#
# print(my_sum([56, 67, 89]))
# print(sum([56, 67, 89]))


###########################################

#
# def max2(a, b):
#     if a >= b:
#         return a
#     else:
#         return b
#
#
# def max3(a, b, c):
#     if c >= max2(a, b):
#         return c
#     else:
#         return max2(a, b)
#
#
# print(max2(3, 10))
# print(max3(30, 10, 3))


###########################################

# def my_func(name='Noname', age='18', city='Nocity'):
#     return [name, age, city]
#
#
# # print(my_func('Max', 'Kiev', '25'))
# # print(*my_func(name="Alex", age="23", city="Dnipro"))
# print(*my_func(city="Dnipro"))
# print(*my_func("Dnipro"))
# # print(*my_func())


####################################


# def my_func(*args, **kwargs):
#     # print(type(args), args)
#     # print(type(kwargs), kwargs)
#     for i in args:
#         print('args =>', i)
#     print('.' * 80)
#     for j in kwargs.values():
#         print('kwargs =>', j)
#     print('.' * 80)
#     for k, j in kwargs.items():
#         print('kwargs =>', k, j)
#     print('.' * 80)
#
#
# my_func(1, 'Alex', [1, 2, 3], name='Max', surname='Koval', age=25)

##################################################





#
# def my_max(*args):
#     res = args[0]
#     for i in args[1:]:
#         if i > res:
#             print(i, '>', res, '!!!')
#             res = i
#     return res
#
#
# print('max =', my_max(12, 45, 78, 489, 56, 723, -34, 34))
#

############## Change name (псевдоним) !!!!!!!!!!!!!!
# my_sum = sum
# your_sum = my_sum
#
# print(my_sum([1, 2, 3]))
# print(sum([1, 2, 3]))
# print(your_sum([1, 2, 3]))


#
# def say_hello():
#     print('Hello')
#
#
# say_hi = say_hello
#
# say_hi()
# say_hello()

# ...............................

#
# def pwr(x, n):
#     return x ** n
#
#
# print(pwr(2, 3))
# power = pwr
#
# print('pwr :', pwr(2, 3))
# print('power :', power(2, 3))


# .............................

# def pwr(x=2, n=3):
#     return x ** n
#
# power = lambda x, y: x**y
# print(power(4, 2))
#
# power = lambda x=3, y=3: x**y
# print(power())
#
# power = lambda *args: list(str(i)*i for i in args if i % 2)
# print(power(2, 3, 4, 5, 6, 1, 12, 16, 8, 9))





#########################################

# def my_prn(n: int, symbol: str, a=0) -> int:
#     print('symbol * n =', symbol * n)
#     print('a =', a)
#     return n**2
#
#
# result = my_prn(4, '$', 777)
# print('result=', result, type(result))

#############################################


# 5! = 1 * 2 * 3 * 4 * 5

def factorial(n: int) -> int:
    res = 1
    for i in range(1, n + 1):
        res *= i
    # print(n, '! = ', res)
    return res


# print(factorial(3))
# print(factorial(5))
# print(factorial(7))
# print(factorial(10))
# print(factorial(20))



# for i in range(1, int(input('n = '))+1):
#     print(f'factorial {i}=', factorial(i))


# !!!!!!!!!!!!!!! RECURTION !!!!!!!!!!!!!!!!!!!!!

# def short_story(i=0):
#
#     print("У попа была собака, он ее любил.")
#     print("Она съела кусок мяса, он ее убил,")
#     print("В землю закопал и надпись написал:")
#     i += 1
#     if i < 5:
#         short_story(i)
#
#
# short_story()

###########################################

# def factorial(n: int): # 1 * 2 * 3 * 4 * 5 = res
#     res = 1
#     for i in range(1, n + 1):
#         print(i-1, '! =', res)
#         res *= i
#     return res




# def factorial(n: int):                  # 5 * (4 * (3 * (2 * (1)))) = res
#     print('n = ', n)
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)     #(  5 * 4! # (4 * 3! # (3 * 2! #(2 * 1! #
#     #                                     120     24      6        2        1
#
#
# n = int(input('n = '))
# print('factorial', n, '! =', factorial(n))


# !!!!!!!!!!!!!! HomeWork REVERS !!!!!!!!!!!!!!!!


def reverse():
    symbol = int(input('x= '))
    if symbol:
        reverse()
    print(symbol)


reverse()


############################# END





############## Change name !!!!!!!!!!!!!!
# def pwr(x, n):
#     return x ** n
#
#
# print(pwr(2, 3))
# power = pwr
#
# print('pwr :', pwr(2, 3))
# print('power :', power(2, 3))




# def pwr(x=2, n=3):
#     return x ** n

# power = lambda x, y: x**y
# print(power(4, 2))



# power = lambda x=3, y=3: x**y
# print(power())

# power = lambda *args: list(str(i)*i for i in args if i % 2)
# print(power(2, 3, 4, 5, 6))


# def foo(n):
#     return n**2
#
#
# l = [1, 2, 3, 4]
# # l1 = list(map(str, l))
# l1 = list(map(lambda x: x**3, l))
# # l1 = list(map(foo, l))
# # l2 = list(map(foo, l))
# # l3 = list(map(foo, l))
# l2 = list(map(lambda x: x**4, l))
# l3 = list(map(lambda x: x**5, l))
# print(l1)
# print(l2)
# print(l3)