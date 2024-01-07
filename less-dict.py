# змінний неупорядкований набір даних у форматі "ключ-значення"

# l = ['b', 'b1', 'c']
# d = {True: 'a', 'key2': ['b', 1, 2], 3.14: 'c', (1, 2): {'d': 34}}
#
# print(l[2])
# print(d['key2'])
# print(d[(1, 2)])







d1 = {'name': 'Ivan', 33: 3244, 'surname': 'Pupkin', 5: {1: 'jhlkkk'}}

d2 = dict([('a', 'A'), ['UK', 'London'], [1, 'C']])

# t = list(enumerate('Hello'))
# print('t=', t)
# d2 = dict(t)
#
# d3 = dict(name='Ivan', surname='Petrov', nation='Ukrainian', age=18)
#
# print('d1=', d1, id(d1))
# print('d2=', d2, id(d2))
# print('d3=', d3, id(d3))

# print(d1['name'])
# print(d2['a'], d2[1])

# d2['foo'] = 'Function'
# print('d2=', d2, id(d2))
#
# d2['foo'] = [1, 2, 3]
# print('d2=', d2, id(d2))

# d2['foo'] = dict(enumerate('Hello'))
# d2['foo'] = dict(enumerate(range(5, 8), 10))
# print('d2=', d2, id(d2))
#
#
#
#
# print('d1=', d1, id(d1))
# # d5 = d1
# # d5 = d1.copy()
# d5 = dict(d1)
# d5['name'] = 'Gosha'
# print('d1=', d1, id(d1))
# print('d5=', d5, id(d5))

#############################################

d1 = {'name': 'Ivan', 33: 3244, 'surname': 'Pupkin', 5: {1: 'jhlkkk'}}
#..........................................

# print(d1['name'])
# print(d1.get('name11111', 'Ooops!'))
# print(d1)

#................................
# print(d1.keys())
# l = list(d1.keys())
# print(l, type(l))

#................................
# print(d1.values())
# # d1[5] = 15
# print(d1)


#................................
# print(d1.items())
# # for key, value in d1.items():
# #     print(key, value, sep='\t-> ')
#
# for k in d1.items():
#     key, value = k
#     print(k, key, value)



#................................
# print('d1=', id(d1), d1)
# val = d1.pop('name')
# # val = d1.pop('name7777', 'No key!!!!!!')
# print('d1=', id(d1), d1)
# print('val=', val)
#
# d1['name777'] = val
# print('d1=', id(d1), d1)


#................................

# it = d1.popitem()
# print('d1=', id(d1), d1)
# print(it)
# # key, val = it
# # print(key)
# # print(val[1])
#
# it = d1.popitem()
# print('d1=', id(d1), d1)
# print(it)

#................................

# v = d1['name1']
# v = d1.get('name1')
# v = d1.setdefault('name1', 'No key')
# d1['Ivanov'] = 'KH-23m'
# v = d1.setdefault('Petrov', '100')
# print(v)
# print('d1=', d1)

d11 = {1: 'a', 4: 'b', 6: 'c'}
# d11 = {}
# for i in range(1, 9):
#     d11.setdefault(i, 'XXX')
# print('d11=', id(d11), d11)

#................................
# d11.clear()
# d11 = {}
# print('d11=', id(d11), d11)


#................................
# l1 = ('rt', (4, 99))
# # print(dict(l1))
# # l1 = ['ab', 'ht']
# # l1 = [('He', 'llo')]
# print(dict(l1))


#................................

# d4 = {1: 2, 'peace': 'future', 99: {0: 5, 't': 'text'}}
# print('d4=', id(d4), d4)
# print(d4[99]['t'])



# print('d1=', d1)
# print(d1['name'])
# d1['name1'] = 'Vasya'
# d1['name2'] = 'Kolya'
# print('d1=', id(d1), d1)
# del d1['name1']
# # d1.pop('name1')
# # print(d1['name1'])
# print('d1=', id(d1), d1)
#................................


# txt = 'Hello'
# d1 = dict(enumerate(txt, 3))
# d2 = dict(enumerate(txt))
# print(d1)
# print(d2)
# print(d2[0])
#
# # d1 += d2
# d1.update(d2)
# print(d1)
#................................

# d4 = dict()
# d4 = set()
# d4 = {}
# print(d4, type(d4))


#................................
# print('name' in d1.keys())
# print('Ivan' in d1.values())
# print('Ivan' in d1)
# print('name' in d1)

# for i in d1.items():
#     print(i)


# lst = ['a', 'b', 'c', 'd']
# d3 = dict.fromkeys(lst, 'NoValue!')

# d3 = dict.fromkeys(range(1, 6), input(' value : '))
# d3[3] = '50x50'
# print('d3', d3, id(d3))

###########################


# d3 = {}
# for i in range(int(input('number of students = '))):
#     d3[input('surname : ')] = input('name = ')
# print('d3', d3, id(d3))


###################################


d5 = {}
d5[1] = 'aaaaaaaaaa'
d5[0] = 'xxxxxxxxx'
d5['1'] = 'bbbbbb'
d5['abc'] = '00000'
d5[True] = '999999'
d5[False] = 'AAAAAA'
d5[1] = d5[0] = 0
# print('d5', d5, id(d5))

###################################

# !!!!!!! ZIP !!!!!!!!!!!
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l2 = ['a', 'b', 'c', 'd']
l1 = list(map(str, l1))
# print('l1 =', l1)
# print('l2 =', l2)




l3 = list(zip(l1, l2))
l4 = dict(l3)
# print(l3)
# print(l4)
#
#
#
#
# print(l4.items())
#
# print(list(l4.items()))
#
# dd = dict(list(zip(l4.values(), l4.keys())))
# print(list(zip(l4.values(), l4.keys())))
# print('dd =', dd)
##############################################

# print(d5)
# k = '1'
# s = d5.pop(k) # LIFO    STACK
# print(s)
# print(d5)
# d5[k] = s
# print(d5, id(d5))  # LIFO





#######################################

# dd = {x: chr(x) for x in range(97, 115)}

# dd = {x: chr(x) for x in range(97, 115) if x % 2 == 0}
#
# dd1 = {x: chr(x) for x in range(97, 115) if x % 2}
# dd.update(dd1)
#
# # # # dd = {x: chr(x) for x in range(97, 115)}
# # # # # # dd[99] = 'X'
# print('dd =', dd)
# for k, v in dd.items():
#     print(k, v, sep=' -> ')
# # print(dd[100])



#################################### VERONIKA !!!!!!!!!!!!!!!!!!!
#
#
import random


city = ['Kyiv', 'Poltava', 'Dnipro', 'Lviv']
population = [4000, 700, 1000, 850]
# # dict_ua = {x: y for x in city for y in population}  #  ???????????
# # dict_ua = {city[i]: population[i] for i in range(4)}
dict_ua = {x: y for x, y in zip(city, population)}
#
#
# print(dict_ua)
# print(list(dict_ua.values()))
# print(list(dict_ua.items()))

# ........................
# key = random.choice(list(dict_ua))
# print(key, dict_ua[key])

# # #***************** Сортировка по населению
# l1 = list(dict_ua.items())
# print('items : ', l1)
# # l1.sort()
# l1.sort(key=lambda x: x[1], reverse=True)
#
# for i in l1:
#     print(*i, sep='\t')

############################################
# ........... QUIZ
# key = random.choice(list(dict_ua.keys()))
#
# question, answer = key, dict_ua[key]
#
# print("What's population in", question, '?')
# a = int(input('population?  = '))
#
# if a == answer:
#     print('You are right!')
# else:
#     print('You are wrong!')
#
# print('right answer :', answer)



#######################################################
#******* Сортировка букв любого введенного текста
# symbols = set(['ON ', 'THE', 'TO ', 'AND'])
# print('Перелік символів:\n', *symbols)
#
# # text = input('Input any text : ').upper()
# text = '''
# Bring on advanced features like asset
# and configuration management to support ITSM practices.
# Minimize distractions with expanded, personalized support,
# and empower your admins with added controls and security
# safeguards. See value quickly with faster deployments
# compared to legacy tools.
# '''.upper()
# print('Введений текст:\n', text)
#
# set_count = dict(zip(list(symbols), list(map(text.count, symbols))))
# print('\nОбчислений текст множиною:\n', set_count)
#
# list_count = list(set_count.items())
# print('\nОбчислений текст списком:\n', list_count)
#
# list_count.sort(key=lambda x: x[1], reverse=True)
# print('\nВідсортирований список:\n', list_count)
#
# for element in list_count:
#     print(*element, sep='\t')

###################################################

# text = 'Hello, world!'
#
# a = dict(enumerate(text))
# # a = dict(zip(range(len(text)), text))
# print(a)
# # del a[5]
# # a[5.55] = 'W'
# for key, val in a.items():
#     print(key, '-', val, sep='', end='  ')
# print()

# !!!!!!!!!!!!!!!!!!!!!!!!! END



############# ФОРМИРОВАНИЕ СЛОВАРЯ ПО СПИСКУ #############3
# keys = 'ten, one, five, two, three, four'
# keys = keys.split(', ')
# # values = ['номер ' + str(i) + ' в строке' for i in range(1, len(keys)+1)]
# # dic = dict(zip(keys, values))
# dic = {}
# for i in range(len(keys)):
#     dic[keys[i]] = 'номер ' + str(i + 1) + ' в строке'
# print(dic)