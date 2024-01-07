# str   неизменяемая последовательность символов
# list  изменяемая последовательность объектов
# tuple неизменяемая последовательность объектов




# l1 = (33, 555)
# l1 = ()
# l1 = tuple()
# l1 = tuple(range(5))
# print(l1, type(l1), id(l1))


# t = (1, 2, 3, 4.23, 99, 'Hello!', [2, 3, 4], (5, 6, 4), True)
# print(t, type(t), id(t))
#
#
# print(*dir(t), sep='\n')
#############################################

# t = tuple(range(10))
# t1 = t[2:5]
# print(t, type(t), id(t))
# print(t1, type(t1), id(t1))
#
# print(t[2:7], type(t[2:7]), id(t[2:7]))
###########################################



# l = [1, 2, 3, 4]
# t = tuple(l)
# print(l, type(l), id(l))
# print(t, type(t), id(t))


#############################################

# text = 'Hello, world!'
# t = tuple(text)
# print(text, type(text), id(text))
# print(t, type(t), id(t))

###################################
#

# l = [1, 2, 3, 4]
# print(l, type(l), id(l))
# l[0] = 999
# print(l, type(l), id(l))

# t = (1, 2, 3, 4)
# t[0] = 999   #  !!!!!!!!!!!!!!!!!!!!!!!!!!!
# print(t, type(t), id(t))

###################################################

#
# t1 = (1, 2, 3, 4)
# t2 = ('a', 'b', 'c', 'd')
# print(t1, type(t1), id(t1))
# # print(t2, type(t2), id(t2))
# # print(t1 + t2)
# #
# #
# # t3 = t1 + t2
# # print(t3, type(t3), id(t3))
#
# t3 = t1 * 4
# print(t3, type(t3), id(t3))

######################################################

# t1 = (1, 2, 3, 4)
# print('t1 =', t1, type(t1), id(t1))
# t1 += (9999, 8888, 7777)
# print('t1 =', t1, type(t1), id(t1))
#
# t2 = t1[:3] + ('world',)
# print('t2 =', t2, type(t2), id(t2))

#################################################


# t1 = (3)
# t2 = (3,)
# print(t1, type(t1), id(t1))
# print(t2, type(t2), id(t2))

###################################################
# l1 = [i for i in range(5)]
# # l1 = tuple(l1)
# print(l1, type(l1))
#
# l1 = list(i for i in range(5))
# print(l1, type(l1))



# t = tuple(i for i in range(5))
# print(t, type(t))
#
# t = (i for i in range(5))   ################## GENERATOR!!!!!!!!!!!!!
# print(t, type(t))

#####################################3

# t0 = (2, 9, -34, 67)
# print(max(t0))
# print(min(t0))
# print(sum(t0))
# print(len(t0))
# print('.' * 80)
#
#
# t1 = ('Hello,', 'world!', [1, 2, 3], 78, 4545.54)
# print(len(t1))
# print('.' * 80)
#
# for i in t1:
#     print(i)

#####################################################



# t1 = ['Hello,', 'world!']
# t1 = ('Hello,', 'world!')
# text1 = ' '.join(t1)
# print(text1, type(text1))

#################################################


# t2 = (15, 0, 0, 0, 'abc', 44, 56, 77, 0, 0, 0, 44, 8, 44, 0, 34)
# print(t2, id(t2))
# symbol = 44
#
# print('count :', t2.count(symbol))
# print('index :', t2.index(symbol))


#########################################

# t1 = 'Hello!'
# for el in enumerate(t1):
#     print(el, type(el))



# a, b = (777, 888)
# print(a, b)


# a, b = range(3, 5)
# print(a, b)


# t1 = 'Hello!'
# for num, el in enumerate(t1):
#     print(num, type(num), '->', el, type(el))

###################################################


# t1 = (222, 333, 2, 3, 6, 9, 0, -24)
# print(t1, type(t1), id(t1))
#
# n = int(input('index='))
# el = int(input('element='))
# t1 = t1[:n] + (el,) + t1[n:]
# print(t1, type(t1), id(t1))


#####################################

# t1 = (222, 333, 2, 3, 6, 9, 0, -24)
# print(t1, type(t1), id(t1))
#
# l1 = list(t1)
# print(l1, type(l1), id(l1))
#
# l1.insert(5, 3333333)
# # l1.sort()
# print(l1, type(l1), id(l1))
#
# t1 = tuple(l1)
# print(t1, type(t1), id(t1))


########################################################


# t1 = ('World!',)
# print('\ntuple ->', t1, id(t1))
#
# l1 = list(t1)
# print('\nto list ->', l1, id(l1))
#
# l1.append('Hello')
# print('\nappend ->', l1, id(l1))
#
# l1.sort()
# print('\nsort ->', l1, id(l1))
#
# t1 = tuple(l1)
# print('\nto tuple ->', t1, id(t1))
#
# text = ', '.join(t1)
# print('\nafter join ->', text, id(text))

#####################################################

# t1 = (1, 2, (4, 5), 88)
# print(t1, id(t1), len(t1))
# t1 = (8,) + t1[1:]
# print(t1, id(t1), len(t1))


#
# t1 = (1, 2, [4, [9, 'Hello']], 88)
# print(t1, id(t1), len(t1))
# # for el in enumerate(t1):
# #     print(el)
# print(t1[2][1][1] + ', world!')








# print(t1[2][1][1])
# t1[2][1][1] += ', world!'
# print(t1[2][1][1])
# print(t1, id(t1), len(t1))


