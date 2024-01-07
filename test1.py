# n = int(input())
# for j in range(1, n + 1):
#     for i in range(1, j + 1):
#         print(i, end="")



# print(range(5)) # [0, 1, 2, 3, 4]  [0; 5)

# print(1, 2, 3, sep='-', end='\n')
# print(1, 2, 3, sep='+', end='\t')
# print(1, 2, 3, sep='=', end='')

a = int(input())
b = int(input())
l = int(input())
N = int(input())
print(a*(2*(N-1)+1) + b*2*(N-1) + 2*l)

# n = int(input('n = '))
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(j, end='')
#     print()









# a = 'информатика' # --> тортик












# a, b = map(int, input().split())
# print(a, type(a))
# print(b, type(b))
#
# from random import *
#
# n = int(input('n = '))
# text = ''
# k, m = n, n
# while k > 0 or m > 0:
#     i = randint(1, 2)
#     if i == 1 and k:
#         text += '1 '
#         k -= 1
#     elif i == 2 and m:
#         text += '2 '
#         m -= 1
# print(text)


# from random import *
#
# n = int(input('n = '))
# l = []
# k, m = n, n
# while k > 0 or m > 0:
#     i = randint(1, 2)
#     if i == 1 and k:
#         l.append(1)
#         k -= 1
#     elif i == 2 and m:
#         l.append(2)
#         m -= 1
# print(l)


# p = int(input())
# x = int(input())
# y = int(input())
#
# start = 100 * x + y
#
# res = int(start * (100 + p) / 100)
#
# print(res // 100, res % 100)






# n = int(input('n='))
# m = int(input('m='))
# x = int(input('x='))
# y = int(input('y='))
#
# if n > m:
#     n, m = m, n
# if x > m - x:
#     x = m - x
# if y > n - y:
#     y = n - y
# if x < y:
#     print(x)
# else:
#     print(y)




# minuts = int(input())
# clock = minuts % (24 * 60)
# h = clock // 60
# m = clock % 60
#
# print(h, m)

# a, b, c, d = 'Hello', 35, True, 67-89/2
# a, b = b, a
# print(a, b, c, d)










# import random
# import os
# from random import randint
# import math
#
#
# a = 4
# b = math.sqrt(a)
# print(type(a), b, type(b))
# print(random.randint(0, 6))
# print(randint(0, 6))
# if random.randint(0, 6) == 1:
#     os.remove()


#
# for i in range(10):
#     if i % 2 != 0:
#
#         print(i, '==========')
# else:
#     print('cycle completed!!!')








# import random
#
# print(int(random.random()*6)+1)
# print(int(random.random()*6)+1)
# print(int(random.random()*6)+1)
# print(int(random.random()*6)+1)
# print(int(random.random()*6)+1)

# a = 0.8
# if 1 or 0:
#     print(True)
# else:
#     print(False)

# print(bool((0 or 0) and (1 or 1) and 1 and (1 or 0)))













# a = '34'
# b = -7687687.435
# c = 0.0
# print(bool(a))
# print(bool(b))
# print(bool(c))






# import random
#
# print(random.randint(1,10))


# a = 3
# name = 'Vasya'
# b = 2
# c = a + b
# print('{} ghjhgjhgj {} {name}'.format(a, b, name=name))


# x = ()
# print(bool(not 1 or not 1))
# print(bool(1 or 0))
# print(bool(0 or 0))
# print(bool(0 or 1))




# print(bool(x))
# print(str(bool(x)))
# print(bool(str(bool(x))))

# x1 = [('a',1),('b',2),('c',0),('d',-1)]
# print(x1)
# for i in sorted(x1, key=lambda x1: x1[0]):
#     print(i)

# n = int(input())
# text = []
# count = []
# for i in range(n):
#     line = input().split()
#     text += line
# words = set(text)
# for i in words:
#     count.append((text.count(i), i))
# count1 = sorted(count, reverse=True)
# for i in count1:
#     print(i[1])
#
# n = int(input())
# text = []
# count = []
# # for i in range(n):
# #     line = input().split()
# #     text += line
# text = '''
# hi
# hi
# what is your name
# my name is bond
# james bond
# my name is damme
# van damme
# claude van damme
# jean claude van damme'''.split()
# words = set(text)
# for i in words:
#     x = (text.count(i), i)
#     count.append(x)
# # count.sort(key=lambda x: x[1])
# # count.sort(key=lambda x: x[0], reverse=True)
# count.sort(key=lambda x: (-x[0], x[1]))
# for i in count:
#     print(i[1])
