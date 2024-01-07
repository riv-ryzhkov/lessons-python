# map-zip-lambda-filter-sort




def my_func(x):
    return abs(int(x))


# print(my_func(-465.9008))

# l1 = [2, '-3', -45, '67', '-99']
# print(l1, id(l1))
#
# l2 = []
# for i in l1:
#     l2.append(my_func(i))
#
# print(l1, id(l1))
# print(l2, id(l2))


################################ map

# l2 = list(map(my_func, l1))
# l2 = list(map(my_func, [1, "-2", -3, 5]))
# print(l2, id(l2))

# def pwd(num):
#     return num ** 2


# l = list(range(-5, 5))
# print(l)
# l2 = list(map(pwd, l))
# print(l2)




# l2 = list(map(lambda x: x ** 2, l))
# print(l2, id(l2))



# l1 = list(map(lambda x: abs(int(x)), l1))
#
# print(l1, id(l1))



############################################## filter

# l1 = [2, '-3', -45, '67', '-99']
#
# l2 = list(filter(lambda x: int(x) < 0, l1))
#
# l3 = list(filter(lambda x: type(x) == str, l1))
#
# l4 = list(filter(lambda x: type(x) == int, l2))
#
# l5 = list(filter(lambda x: type(x) == str and int(x) < 0, l1))
#
# print(l1, id(l1))
# print(l2, id(l2))
# print(l3, id(l3))
# print(l4, id(l4))
# print(l5, id(l5))

# ................................

# webs = [
#     'google.com',
#     'sport.ua',
#     'mail.ru',
#     'snn.com',
#     'yandex.ru'
# ]
#
# symbols = '.ru'
# my_webs = list(filter(lambda x: not x.endswith(symbols), webs))
# print(my_webs)

####################################### ZIP



# text = 'Hello'
# l1 = list(text)
# l2 = list(range(10))
#
# l3 = list(zip(l2, l1))
#
# print(l1)
# print(l2)
# print(l3)
#
# print(list(enumerate(l1)))

# ................................................ sort

#
# l3 = [422, '373', 145, '867', '18899']
# print('l3 ->', l3)
#
# # l3 = list(map(int, l3))
# # l3 = list(map(str, l3))
# # print('map ->', l3)
#
# l3.sort(key=lambda x: str(x), reverse=True)
# # l3.sort()
# # # print(l1)
# print('sort ->', l3)




# .........................................


# city = ['Dnepr', 'Kiev', 'Lviv', 'Odessa', 'Rivno']
# population = [1000000, '4500000', 9000000, '850000', 200000]
# pop = list(map(int, population))
# print('population = ', population)
# print('pop = ', pop)
#
# population = list(map(lambda x: int(x/1000), pop))
# print(*population)
#
# res = list(zip(city, population))
# # res = list(zip(range(1, 30), city, population))
# print(res)
#
# res.sort(key=lambda x: x[1], reverse=True)
# print(*res)
#
# res = list(filter(lambda x: x[1] > 800, res))
# print(*res)
#
# print(*res, sep='\n')
# #
# for i in res:
#     print(*i, sep='\t')


#############################################################

# l1 = [2, '-3', -45, '67', '-99']
# # l2 = list(filter(str, l1))   # !!!!!!!!!!!!!!!!!!!!!!NOT WORK!!!!!!!!!!!
# l2 = list(filter(lambda x: type(x) == str, l1))
# l3 = list(map(lambda x: (int(x)+2) ** 2, l1))
# l4 = list(map(int, l1))
# print('l1 =', l1)
# print('l2 =', l2)
# print('l3 =', l3)
# print('l4 =', l4)
# print('max =', max(l4))


############################################## Напоминание!


# l1 = [1, 2, 3, 4, 5]
# l2 = [chr(i) for i in range(97, 108)]
# print(l1)
# print(l2)

# .................................




# l1 = 'Hello, world!'
# l2 = list(zip(range(len(l1)), list(l1)))
# print(*l2)
#
# print(*list(enumerate(l1)))

#############################################


# def pwr(x):
#     return int(x) ** 2
#
#
# l1 = [2, '3', 45, '67', '99']
# print(l1)
#
# l2 = list(map(lambda x: int(x) ** 2, l1))
# print(l2)
# print(list(map(pwr, l1)))
#
# l3 = list(filter(lambda x: int(x) > 40, l1))
# print(l3)
#
# l4 = list(map(pwr, l1))
# print(l4)

#############################################

# print(pow(3, 3))
# print(pow(2, 3))
#
#
#
# #.............................
base_numbers = [2, 3, -4, -5, 0, 8, 10, 12, 14, 16]
# print('filter ->', list(filter(lambda x: x % 2 == 0, base_numbers)))
#
# print('filter None ->', list(filter(None, base_numbers)))
#
#
powers = [1, 2, 3, 4, 5]
#
# numbers_powers = list(map(pow, base_numbers, powers))
# #
# print('pow=', numbers_powers)
#
#
# z = list(zip(base_numbers, powers))
# print('z1 =', z)
#
# z = zip(base_numbers, powers)
# print('z2 =', z)


###################

# for k, n in zip(base_numbers, powers):
#     print(k, '**', n, '=', k**n)


########################################
# a = [1, 3, 5, 7]
# print(a)
# b = list(map(lambda x: x**2, a))
# print(b)
# c = list(zip(a, b))
# for k, l in c:
#     print(k, '*', k, '=', l)

