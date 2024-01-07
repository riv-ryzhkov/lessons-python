# ########### GENERATORS LIST-TUPLE-SET-DICT #############

# for i in range(256):
#     print(i, '->', chr(i))





list1 = [chr(i) for i in range(97, 110)]
# print(list1)
#
tuple1 = tuple(i for i in range(15, 0, -1))
# # print(type(tuple1))
# print(tuple1)
#
#
set1 = {chr(i) for i in range(97, 110)}
# print(set1)
#
#
dict1 = {x: y for x, y in zip(set1, tuple1)}
#
# # print(set1)
# print(dict1)


gn = (chr(i) for i in range(97, 110))

# print(next(gn))
# print(next(gn))
# print(next(gn))
# print(next(gn))
# print(next(gn))
# print(list(gn))
# print(list(gn))

# breakpoint()


# print(set(gn))

# print(type(gn), gn)


gn = (x for x in range(5))
# print(next(gn))
# print(next(gn))
# print(list(gn))
# gn = (x for x in range(5))
# print(list(gn))


# print(next(gn))
# print(next(gn))
# print(next(gn))
# print(next(gn))







# # print(next(gn))
# # print(set(gn))
# # gn = (chr(i) for i in range(97, 110))


# gn = (chr(i) for i in range(97, 110))
# var = next(gn)
# print('var=', var)
# print(next(gn))
# print(next(gn))
# print(next(gn))
# print(list(gn))
# print(list(gn))
# print(next(gn))

# gn = (i for i in range(97, 1111110))
# print(sum(gn))
# print(sum(i for i in range(97, 110)))


# l = []
# gen = (i for i in range(15, 0, -1))
# print(gen, type(gen))
# l.append(next(gen))
# l.append(next(gen))
# l.append(next(gen))
# print(l)
# l = list(gen)
# print(l)
# l = list(gen)
# print(l)
# gen = (i for i in range(15, 0, -1))
# print(list(gen))


gen = (i for i in range(15, 0, -1))
# print('gen:', type(gen))
# print(list(gen))
# print(list(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(list(gen))
# print(next(gen))
# print(list(gen))


######################## Examples #############
# def even_numbers(n):
#     for i in range(n):
#
#         yield i ** 2  # ->>>>>
#         # print('!!!!!!!', i)
#         # yield i ** 3
#         # return i ** 2  # ->>>>>
#         print(':-)', i)
#
#
# gen1 = even_numbers(5)
#
#
# # print(gen1)
# # print(gen1)
# # print(gen1)
# # print(gen1)
# # print(type(gen1))
# print('1 step =(i=0)', next(gen1))
# print('2 step =(i=1)', next(gen1))
# print('3 step =(i=2)', next(gen1))
# print('4 step =(i=3)', next(gen1))


# print(next(gen1))
# print(next(gen1))
# print(next(gen1))


def fibonacci(n):
    a, b = 0, 1     #   0,1,1,2,3,5,8,13,21,34,....
    for i in range(n):
        yield a
        a, b = b, a + b

#
# n = 10
# fib = fibonacci(n)
#
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(list(fib))

# print('fib:', next(fib))
# print('numbers:', next(numbers))
# print('fib:', next(fib))
# print('numbers:', next(numbers))
# print('fib:', next(fib))
# print('numbers:', next(numbers))

#
# # for num in numbers:
# #     print(num)
#
# for i in range(n):
#     print(i, '->', next(numbers), 'fib =', next(fib))

#################### EXMPL 2

#
# def divisible_by(divisor, n):
#     for i in range(1, n+1):
#         if i % divisor == 0:
#             yield i
#
#
# m, n = 4, 60
# numbers = divisible_by(m, n)
# # print(numbers)
# while True:
#     try:
#         print(next(numbers))
#         input()
#     except:
#         print('The Generation over!')
#         break

#########################################





# ########## Generator on base of Factorial ###########
def factorial(n: int):
    res = i = 1
    while i <= n:
        res *= i
        i += 1
        yield res
    return res # 1*2*3*4*5


# print(factorial(5))

# fact = factorial(7)
#
# # print(fact, type(fact))
# # print(next(fact))
# # print(next(fact))
# # print(next(fact))
# # print(next(fact))
# # print(next(fact))
# # print(next(fact))
# # print(next(fact))
# #
# # # print(list(fact))
# # print(list(fact))
# #
# fact = factorial(9)
# print(list(fact))
# # # print(next(fact))
# # # print(next(fact))
# #
# fact = factorial(7)
# print(fact)
# print('1: ', next(fact))
# print('2: ', next(fact))
# print('3: ', next(fact))
# print('4: ', next(fact))
# # print('5: ', next(fact))
# # print('6: ', next(fact))
# fact1 = list(fact)
# print('fact1 = ', fact1, type(fact1))
# fact = factorial(7)
# fact5 = factorial(8)
# fact2 = list(fact)
# print('fact2 = ', fact2, type(fact2))
# # ###################################################

# n = 7
# fact = factorial(n+1)
# for i in range(1, n+1):
#     print(i, '! =', next(fact))


# # #################################################
# n = 5
# fact = factorial(n)
# f = factorial(n)
# print(id(fact), list(fact))
# print(id(f), list(f))
# f = factorial(n)
# print(id(f), list(f))

# # ###############################################
#  GENERATORS : MAP-ZIP-ENUMERATE  RANGE   ITEMS  #

l1 = [str(i) for i in range(10)]
# print(l1)
m = map(int, l1)
# print(m, type(m))
# print(next(m))
# print(next(m))
# print(next(m))
# print(next(m))
# print(tuple(m))
# print(list(m))

# en = range(100)
# z = zip(en, l1)
z = zip(l1, l1)
# # print(z, type(z))
# print(next(z))
# print(next(z))
# print(next(z))
# print(next(z))
# print(list(z))
# print(list(z))




e = enumerate(l1)
# print(e, type(e))
# print(next(e))
# print(next(e))
# print(next(e))
# print(next(e))
# print(list(e))
# print(list(e))





r = range(10)
# print(r, type(r))
# # print(next(r))
# # print(next(r))
# # print(next(r))
# print(list(r))
# print(list(r))
# print(list(r))
# print(tuple(r))
# print(set(r))

###############
r = range(10)
# r = (i for i in range(10))
# for i in r:
#     print(i, end=' ')
#
# for i in r:
#     print(i, end=' ')
#
# for i in r:
#     print(i, end=' ')

##########
#
# print(dict1)
# # # # d = (i for i in dict1.items())
# # d = dict1.items()
# # d = dict1.keys()
# d = dict1.values()
# # # # # # d = [1, 2, 3]
# # print(next(d))
# # print(next(d))
# print(list(d))
# print(list(d))
# print(list(d))
# print(list(d))
#
#
# ###################
import sys


# print('map : ', sys.getsizeof(m), m)
# print('zip : ', sys.getsizeof(z), z)
# print('enumerate : ', sys.getsizeof(e), e)
# print('range : ', sys.getsizeof(r), r)
# print('gen : ', sys.getsizeof(gen), gen)
# # #########################
#
#
#
# # # ############# GENERATORS ####################
### сравним размеры объеков и скорость доступа ################
import sys
import time


n = 10000000
start = time.time()
g = (i * 2 for i in range(n))
print('Memory of generator =', sys.getsizeof(g))
print('time of creating GENERATOR = ', time.time() - start)
print()


start = time.time()
l = [i * 2 for i in range(n)]
print('Memory of list = ', sys.getsizeof(l))
print('time of creating LIST = ', time.time() - start)


start = time.time()
i = next(g)
print()
print('time of "NEXT" = ', time.time() - start)
print()

start = time.time()
h = l[0]
print()
print('time of "L[0]" = ', time.time() - start)
print()


start = time.time()
for i in g:
    h = i
print('time of "ALL GENERATOR" = ', time.time() - start)
print()

start = time.time()
for i in l:
    h = i
print('time of "i in L" = ', time.time() - start)
print()

start = time.time()
for i in range(len(l)):
    h = l[i]
print('time of "RANGE(LEN(L))" = ', time.time() - start)



################# END #########################
# # ##########################################################################
# #
# #
# # def restart_gen():
# #     return (i**2 for i in range(n))
# #
# # gen = (i**2 for i in range(n))
# # # g = gen
# # # print(g)
# # print(gen)
# # # print(gen, '---', type(gen))
# # print(next(gen), '===')
# # print(next(gen), '===')
# # print(next(gen), '===')
# # print(next(gen), '===')
# # # l = list(map(lambda x: x, gen))
# # # print(l)
# # g = restart_gen()
# # print(g, type(g))
# # for i in g:
# #     print(i, '!!!!!!!!')
# #
# #
# #
# # def gen():
# #     i = 0
# #     while True:
# #         val = yield i
# #         if val == 'restart':
# #             i = 0
# #         else:
# #             i += 1
# #
# # g = gen()
# # next(g)
# # print(next(g))
# # print(next(g))
# # g.send('restart')
# # print(next(g))
# # print(next(g))
# # print(next(g))
# # ############################# Ganerators ZIP, MAP, ENUMERATE and RANGE ########
# # base_numbers = [2, 4, 6, 8, 10, 12, 14, 16]
# # powers = [1, 2, 3, 4, 5]
# # z = list(zip(base_numbers, powers))
# # z = zip(base_numbers, powers)
# # e = enumerate('Hello, world!')
# # m = map(str, range(1, n))
# # r = range(1, n) # Выдает всю последовательность сразу и много раз!!!!
# #
# # print('z: ', list(next(z)))
# # print('z: ', list(next(z)))
# # print('z: ', list(z))
# # print('z: ', list(z))
# # print('z: ', list(z))
# # print('z: ', list(z))
# # print('e: ', next(e))
# # print('e: ', next(e))
# # print('e: ', next(e))
# # print('e: ', list(e))
# # print('e: ', list(e))
# # print('e: ', list(e))
# # print('m: ', next(m))
# # print('m: ', next(m))
# # print('m: ', next(m))
# # print('m: ', list(m))
# # print('m: ', list(m))
# # print('m: ', list(m))
# # print('r: ', r)
# # # print('r: ', next(r)) # ОШИБКА!!!!
# # print('r: ', list(r))
# # print('r: ', list(r))
# # print('r: ', list(r))


