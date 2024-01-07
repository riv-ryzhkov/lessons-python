############# print('1 or 1 and 0 = ', 1 or 1 and 0)

#  >    <     ==    <=    >=   !=  ')

# print(2 > 0)
# print(2 > 4)
# print(2 == 4)
# print(2 != 4)
# print(2 <= 4)
# print(2 >= 4)

# print('A' == 'a')
# print('Hello' == 'hello')



# if 2 * 2 != 4:
#     print('True')
# else:
#     print('False')




# x = int(input('x = '))
#
# if 2 * x == 4:
#     print('2 *', x, '= 4', True)
# else:
#     print('2 *', x, '= 4', False)





# Визначити чи знаходиться х в межах відрізка [0;4]
#  ---------------0-----------4---------->

# x = int(input('x = '))

# if x > 4:
#     print(x, '->   x > 4')
# else:
#     if x == 4:
#         print(x, '->   x = 4')
#     else:
#         if x > 0:
#             print(x, '->   0 < x < 4')
#         else:
#             if x == 0:
#                 print(x, '->   x = 0')
#             else:
#                 print(x, '->   x < 0')



#  ---------------0-----------4---------->

# if x > 4:
#     print(x, '->   x > 4')
# elif x == 4:
#     print(x, '->   x = 4')
# elif x == 0:
#     print(x, '->   x = 0')
# elif x > 0:
#     print(x, '->   0 < x < 4')
# else:
#     print(x, '->   x < 0')



# !!!!!!!!!!!!!!!!!!!!????
# 3000-> 20%   1000-> 10%   500-> 5%

s = 5000

# if s >= 500:  #   500...999
#     p = '5%'
# elif s >= 1000:  #   1000...2999
#     p = '10%'
# elif s >= 3000:    # > 3000...
#     p = '20%'
# else:
#     p = '0%'   # < 500
#
# print(p)


# a = -0.0
#
# if a:
#     print(True)
# else:
#     print(False)


# text = ''
# i = 0
# f = 0.0
# b = False
# l = []
# t = ()
# d = {}
# print(text, 'text ->', bool(text))
# print(f, 'f ->', bool(f))
# print(b, 'b ->', bool(b))
# print(l, 'l ->', bool(l))
# print(t, 't ->', bool(t))
# print(d, 'd ->', bool(d))








# print('=' * 5, '  AND  ', '=' * 5)
# print('0 and 0 and 0 = ', 0 and 0 and 0)
# print('1 and 0 and 0 = ', 1 and 0 and 0)
# print('1 and 1 and 0 = ', 1 and 1 and 0)
# print('1 and 1 and 1 = ', 1 and 1 and 1)
#
# print('=' * 5, '  OR  ', '=' * 5)
# print('0 or 0 or 0 = ', 0 or 0 or 0)
# print('1 or 0 or 0 = ', 1 or 0 or 0)
# print('1 or 1 or 0 = ', 1 or 1 or 0)
# print('1 or 1 or 1 = ', 1 or 1 or 1)
# print('=' * 20)

# 1 * 1 * 1 = 1
# 1 * 1 * 0 = 0



# print('1 and 1 or 0 --->', bool(1 and 1 or 0))
# print('0 and 1 or 0 --->', bool(0 and 1 or 0))
# print('0 and 0 or 1 --->', bool(0 and 0 or 1))
# print('1 and 0 or 1 --->', bool(1 and 0 or 1))
# print('1 and 0 or 0 --->', bool(1 and 0 or 0))
# print('1 and 1 or 1 --->', bool(1 and 1 or 1))

# print()
# print()
# print('1 or 1 and 0 ---> ', bool(1 or 1 and 0))


# if True or True and False:
#     print(True)
# else:
#     print(False)






# c = 0
# b = 1
# a = True
# if (a or c) and (b or a):
#     print('OK')
#     print('OK')
#     print('OK')
# elif 2 == 2:
#     print('*' * 20)
# elif 2 < 5:
#     print('@' * 20)
# elif 2 > 1:
#     print('!' * 20)
# else:
#     print('='*60)



#

# --------- sensors ------------
a = 1
b = 0
c = 1
d = 1
e = 1

# a, b, c, d, e = 1, 1, 1, 1, 1

# if (a or b) and c and (d or e):





# if a and b and c and d and e:
#     print('Works')
# elif a and not b and d and e:
#     print('Alarm!')
# else:
#     print('STOP!!!!!!!')









# s = 2000
#
# if s <= 500:  #   <= 500
#     p = '0%'
# elif s < 1000:  #   501...999
#     p = '5%'
# elif s < 3000:    # 1000...2999
#     p = '10%'
# else:
#     p = '20%'   # >2999
#
# print(p)









# ?????????????????
# a = 4
# b = - a
# c = b + a * 2
# d = 0
# e = c - a
# f = not 0
# if a and b and c and d and not e and f:
#     print('YES')
# else:
#     print('NO')


###########################################
# Тернарний оператор IF
###################################

# a = int(input('a='))
# result = 'Hello!' if a > 0 else 'Buy-buy!'
#
#
# if a > 0:
#     result = 'Hello!'
# else:
#     result = 'Buy-Buy!'



print(result)





# a = -7
# print('Hello!' if a > 0 else 'Bye!')


# x = input('x : ')
# x = float(input('x : '))
# a = 'Hello!(True)' if x else 'Bye!(False)'
# print(a)







# l1 = []
# for i in range(10):
#     l1.append(i if i % 2 else 0)
# print(l1)

# l2 = [i for i in range(10) if i % 2] # else не використовується, тому що існує в FOR
# print(l2)
#
#!!!!!!!!!!!!!!*********************** Others
# # (if_elem_is_false, if_elem_is_true)[elem]
# l3 = [(0, i)[i % 2] for i in range(10)]
# print(l3)
#
