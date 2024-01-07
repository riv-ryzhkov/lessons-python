# a = 9
# b = 2
# print(a/b)  # 4.5
# print(9//2)  # 4
# print(a % b)  # 1




# ()
# **
# * / //  %
# + -

# print(7 - 4 / 2 * (7 - 5) * 3 / 2)
# print(7 - 4 / 2 * 2 * 3 / 2)
# print(7 - 2 * 2 * 3 / 2)
# print(7 - 4 * 3 / 2)
# print(7 - 12 / 2)
# print(7 - 6)

# print(5 * 6 - 2 ** 3 / 2 + 3 / 2 + 2)




# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# print(9//2, 9 % 2)
# print(-9//2, -9 % 2)  # -5 1
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# # (a // b) * b + (a % b) = a

# a = -9
# b = 2
# print((a // b) * b + (a % b))

#       -5   -10        1
# # (-9 // 2) * 2 + (-9 % 2) = -9
# print((-9 // 2) * 2 + (-9 % 2))
# ==================================================





# print(min(3, 6, 90, -4, 4.6, -7.23, 46))
# print(max(3, 6, 90, -4, 4.6, -7.23, 46))
# print(abs(-7), abs(7))
# print(int(-46.99995657868798))



# print(round(9.523435, 5))






# import math


# print(*dir(math), sep='\n')

# a = 64
# print(math.sqrt(a))
# print(a ** (1/2))


# import math
# from math import sin, pi
from math import *
# from math import sin as sinus

# print(sin(3.4))


# print(sin(pi/2))
# print(cosh(pi/2))
# print(tan(pi/4))



# print(math.sin(234))
# print(math.cos(234))


# print(sin(546))
# print(cos(546))
# print(tan(546))


# print(*dir(math), sep='\n')

# print(math.floor(32.9999975869879))
# print(math.ceil(32.0000009999975869879))
#
#
# print(math.floor(-32.9999975869879))
# print(math.ceil(-32.0000009999975869879))


# from math import floor, ceil
# from math import *
# from math import sin as s1



# print(s1(360))
# print(cos(360))
# print(math.cos(360))
# print(math.tan(360))


# print(sqrt(17))
# print(17**(1/2))

# print(log(1024, math.e))
# print(math.e)
# e = 5  # !!!!!!!!!!!!!!!!!!!!!!
# pi = 3.14  # !!!!!!!!!!!!!!!!!!!!!!
# print(log(1024, math.e))
# print(e)
# print(math.e)
# print(pi)
# print(math.pi)


# from math import *
#
# print(sin(radians(45)))
# print(radians(45)*4)
# print(degrees(2*pi))
# print(sin(radians(degrees(pi/4))))
# print(log(456, 3))
# print(pi)
# print(e)


# a = 200 #  10010111  01101011  01010110  1011010101101101111101011110101101110
# b = bin(a) # 2**8 = 256  0...255
# c = oct(a) # 1101 1011 = DB   AE = 10 14 = 1010 1110
# d = hex(a)  #  1011 0101 = 11 05  10->A  11->B  12->C  13->D  14->E  15->F   = B5
# print(a, type(a))
# print(b, type(b))
# print(c, type(c))
# print(d, type(d))


# print(bin(200))  # 0110 0100 = 8 4  1100 1000 = 12 8 = C8  1111 1111 = FF  1100 0100 = C4
# 10 - A  11 - B  12 - C   13 - D   14 - E   15 - F
# a = 218
# b = bin(a)
# c = oct(a)
# d = hex(a) # 2D   0010 1101 = 2 13        2 D       1101 1010 = D A  1111 - F 0111 1110 = 7E
# print(a)
# print(b, type(b))
# print(c, type(c))
# print(d, type(d))


# a = int(input('input number : '))
# if a % 2:
#     print('Непарне!')
# else:
#     print('Парне!')


a = 123456789
# print(a % 10)
# print(a // 1000)
# n = 6
# print(a // 1000000 % 10)



# Завдання! Зробити програму, яка виводить бажану цифру на екран

a = 576576768897095
# print(a % 100000 // 1000)
# n = int(input('n= '))
# print()

#
# n = int(input('Введіть яку цифру сзаду потрібно вивести n= '))
# print(a // 10**(n-1) % 10)


















# !!!!!!!!!!!!!!!!!!!!! 0.30000000000000004.com !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# print(0.1 + 0.2)
# a = 1 / 3
# print(a)
# print((0.1+0.2) == 0.3)
# print(a * 3)
#
# print(0.1 + 0.2 == 0.3)
# print(0.1 + 0.2 - 0.3)
# res = 0.1 + 0.2
# print(format(res, '.15f'))
# print(round(0.1 + 0.2, 15))
#
#
#
import math

print(0.1 + 0.2 == 0.3)
print(0.1 + 0.2)
print(0.2)
print(0.3)
print(math.isclose(0.1 + 0.2, 0.3))  # скругляє до 1е-9
#
# print(1/3)
# print(1/3*3)






















# 1=====================================
# x = float(input())
# print(int((x * 10) % 10))

# print(int((float(input()) * 10) % 10))


# 2======================================
# n = int(input())
# print(n // 100 + (n % 100) // 10 + (n % 10))



#3======================================
# n = int(input())
# m = int(input())
# print((m+n-1)//n)


# n = int(input())
# m = int(input())
# if m % n == 0:
#     print(m // n)
# else:
#     print(m // n + 1)



#3===========================
# import math
#
# n = int(input())
# m = int(input())
# print(math.ceil(m / n))



#4=====================================
# a = int(input())
# a = a*45 + (a//2)*5 + ((a+1)//2-1)*15
# print(a//60 + 9,  ':', a%60)



#5=====================================
# print(float(input()) % 30 * 12)
#
#
#
# alpha = float(input())
# print(alpha % 30 * 12)



#6=====================================
# a = 10
# b = 3
# c = a//b
# d = a%b
# print('a= ', a, '  b= ', b, '   a//b= ', c, '  a%b= ', d,'   ', '    a//b + a%b = ', c*b+d)
# a = 10
# b = -3
# c = a//b
# d = a%b
# print('a= ', a, '  b=', b, '   a//b=', c, '  a%b=', d,'   ', '    a//b + a%b = ', c*b+d)
# a = -10
# b = 3
# c = a//b
# d = a%b
# print('a=', a, '  b= ', b, '   a//b=', c, '  a%b= ', d,'   ', '    a//b + a%b =', c*b+d)
# a = -10
# b = -3
# c = a//b
# d = a%b
# print('a=', a, '  b=', b, '   a//b= ', c, '  a%b=', d,'   ', '    a//b + a%b =', c*b+d)


#6!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# v = int(input())
# t = int(input())
# print((v * t) % 109)



#7================================
# h = int(input())
# a = int(input())
# b = int(input())
# k = (h - a)//(a - b)
# if h <= a:
#     k = 1
# elif (h - a) % (a - b) == 0:
#     k += 1
# else:
#     k += 2
# print(k)



#7!!!!!!!!!!!!!!!!!!!!!!!
#
# import math
#
#
# h = int(input())
# a = int(input())
# b = int(input())
# print(math.ceil((h-a)/(a-b))+1)

