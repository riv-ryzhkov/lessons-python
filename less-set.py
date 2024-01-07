# змінний неупорядкований набір неповторюючихся об'єктів

# НЕзмінні :
"""
1. Int
2. Float
3. Boolean
4. Tuple
5. String
при можливих змінах створюється НОВИЙ об'єкт!
"""
# a = (1, 2, 3)
# b = a
# print('a=', a, id(a))
# print('b=', b, id(b))
# b += (5,)
# print('a=', a, id(a))
# print('b=', b, id(b))

#############################################

# Змінні :
"""
1. List
2. Set
a = b создается ПСЕВДОНИМ того же самого об'єкта!
"""

# a = [1, 2, 3]
# b = a
# print('a=', a, id(a))
# print('b=', b, id(b))
# b += [5]
# print('a=', a, id(a))
# print('b=', b, id(b))

#################################################

# SET - змінний неупорядкований набір неповторюючихся об'єктів
a = {8, 11, 3, 3, 5, 'abc', True, False, 'ABC', 4, 2, 11, 11, 11, 11, 3}
# b = [8, 11, 3, 3, 5, 'abc', True, False, 'ABC', 4, 2, 11, 11, 11, 11, 3]
# c = {8, 11, 3, 5, 'abc', True, False, 'ABC', 4, 2, 11, 3}
# print("len(a) =", len(a))
# print("len(b) =", len(b))
# print("len(c) =", len(c))
print('a =', a)
# print('b =', b)
# print('c =', c)

##################################

# # a = {}
# a = dict()
# print(a, type(a))
#
# a = set()
# print(a, type(a))


##############################################

# text = input('text: ')
# print(len(text), text)
# print(len(set(text)), set(text))
# print('повторів: ', len(text) - len(set(text)))


##############################################


# a = set(range(5))
# print('a=', a, id(a))
# b = a
# a.add(3333)
# # b = a + b
# print('a=', a, id(a))
# print('b=', b, id(b))

##########################################




# s1 = {1, 2, 3, 4, 5, 6}
# s2 = {4, 5, 6, 7, 8, 9}
# s3 = set()
# print('s1 =', s1, type(s1), id(s1))
# print('s2 =', s2, type(s2), id(s2))

# .................................
# s3 = s1.union(s2)
# s3 = s1 | s2


# .................................
# s1.update(s2)
# s1 |= s2
# s1 = s1.union(s2)


# .................................
# s3 = s1.intersection(s2)
# s3 = s1 & s2


# .................................
# s1.intersection_update(s2)
# s1 &= s2


# .................................
# s3 = s1.difference(s2)
# s3 = s1 - s2


# .................................
# s1.difference_update(s2)
# s1 -= s2


# .................................
# s3 = s1.symmetric_difference(s2)
# s3 = s1 ^ s2
# s3 = (s1 | s2) - (s1 & s2)


# .................................
# s1.symmetric_difference_update(s2)
# s1 ^= s2


# .................................
# print('.' * 80)
# print('s1=', s1, id(s1))
# print('s2=', s2, id(s2))
# print('s3=', s3, id(s3))

##############################################

# s1 = set(range(5))
#
#
# s1.add(888)
# s2 = s1.add(888)
# print('s1=', s1, id(s1))
# print('s2=', s2, id(s2), type(s2))

############################################

# s1 = set(range(5))
# # s1.add(999)
# s2 = set(range(5, 10))
# print('s1 =', s1)
# print('s2 =', s2)
# print('.' * 80)


# print(s1.issubset(s2))
# print(s1 <= s2)
#................................

# print(s1.issuperset(s2))
# print(s1 >= s2)
#
#.................................


# print(s1 < s2)
# print(s1 > s2)
# print(len(s1))
#.................................

# print(1 in s2)
# print(44 in s1)
# print(55 in range(22, 55))
#.................................


# print(s1.isdisjoint(s2))
# s3 = s1
# s3 = s1.copy()
# s3 = set(s1)
#
# s3.add('ss')
# print('s3 =', s3, type(s3), id(s3))
# print('s1 =', s1, type(s1), id(s1))
# # s1[0] = 999
# # print(s1[0])

#.................................

# s1 = list(s1)
# print(type(s1), s1[0])
# s1 = set(s1)
# print(type(s1), s1)
#.................................


# s1.add(89)
# s1.remove(222)
# print(type(s1), 's1 =', s1, id(s1))
#
# s1.pop()
# print(type(s1), 's1 =',  s1, id(s1))
# # print('s1.pop() =', s1.pop())
# s4 = s1.pop()
# print('s4 =', s4)
# print(type(s1), 's1 =', s1, id(s1))
# s1.add(s4)
# print(type(s1), 's1 =', s1, id(s1))
#
# s1.discard(3333)
# print(type(s1), 's1 =', s1, id(s1))
#
# # s1.clear()
# s1 = set()
# print(type(s1), 's1 =', s1, id(s1))


###########################################

# s1 = frozenset(s1)
# s1.clear()
# s1.pop()
# s1.add(5555)
# del s1
# s1 = set()
# s1.add(5555)
# print('s1 =', s1, type(s1), id(s1))

########################################
#
# text = 'Hello, world!'
# print(list(text))
# print(tuple(text))
# print(set(text))

##############################################



text = '''While The Python Language Reference describes the exact syntax and semantics of the Python language, this library reference manual describes the standard library that is distributed with Python. It also describes some of the optional components that are commonly included in Python distributions.
Python’s standard library is very extensive, offering a wide range of facilities as indicated by the long table of contents listed below. The library contains built-in modules (written in C) that provide access to system functionality such as file I/O that would otherwise be inaccessible to Python programmers, as well as modules written in Python that provide standardized solutions for many problems that occur in everyday programming. Some of these modules are explicitly designed to encourage and enhance the portability of Python programs by abstracting away platform-specifics into platform-neutral APIs.
The Python installers for the Windows platform usually include the entire standard library and often also include many additional components. For Unix-like operating systems Python is normally provided as a collection of packages, so it may be necessary to use the packaging tools provided with the operating system to obtain some or all of the optional components.
In addition to the standard library, there is a growing collection of several thousand components (from individual programs and modules to packages and entire application development frameworks), available from the Python Package Index.
'''




# l1 = text.split()
# print('len(l1) =', len(l1))
# print('l1 =', l1)
# print('.' * 80)
#
# s1 = set(l1)
# print('len(s1) =', len(s1))
# print('s1 =', s1)
# print('.' * 80)
#
# l2 = list(s1)
# l2.sort()
# print('len(l2) =', len(l2))
# print('l2 =', l2)
# print('.' * 80)

#############################################
########### аналіз тексту ###################

# l1 = text
# print('len(l1) =', len(l1))
# print('l1 =', l1)
# print('.' * 80)
# l2 = []
# for letter in l1:
#     if letter.isalpha() or letter == ' ' or letter == '’' or letter == '-' or letter == '\n':
#         l2.append(letter.lower())
#
# print('len(l2) =', len(l2))
# print('l2 =', l2)
# print('.' * 80)
#
# text = ''.join(l2)
# print('len(text) =', len(text))
# print('text :', text)
# print('.' * 80)
#
# list_text = text.split()
# print('list_text =', list_text)
# print('len(list_text) =', len(list_text))
# print('.' * 80)
#
# print('len(set(list_text))', len(set(text.split())))
#
# list_set_text = list(set(text.split()))
# print('list_set_text =', list_set_text)
# print('.' * 80)
#
# result = []
# for word in list_set_text:
#     result.append((word, list_text.count(word)))
# print('result =', result)
# print('.' * 80)
#
# result.sort(key=lambda x: x[1], reverse=True)
# print('result(sort) =', result)
# print('.' * 80)
#
# for word in result:
#     print(*word, sep='\t')

########################################################



################ 1 - True, 0 - False ##################

# d = set([1, 0, True, True, False, 1, 0, False])
# # d = set([1, 0, True, True, False, 1, 0, False])
# print(len(d))
# print(d)

################################################
############ парадокс "заморозка-разморозка" ##############

# a = frozenset([2, 3, 4, 5, 6, 6, 6])
# print('a =', type(a), a, id(a))
# b = set(a)
# print('b =', type(b), b, id(b))
# b.add(99)
# print('b =', type(b), b, id(b))
# b.remove(99)
# c = frozenset(b)
# print('c =', type(c), c, id(c))
# print('c is a ->', c is a)
# print('c = a ->', c == a)

#######################################################

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!! end !!!!!!!!!!!!!!!!!!!!!!!!!!!












#### ЗАДАЧА - Угадай число-2##################
# num_list = set(str(x) for x in range(1, int(input('n = '))+1))
# while True:
#     beatr = set(input().split())
#     if 'HELP' in beatr:
#         break
#     if len(beatr & num_list) > len(num_list - beatr):
#         print('YES')
#         num_list &= beatr
#     else:
#         print('NO')
#         num_list -= beatr
# num_list = list(map(int, num_list))
# print(' '.join([str(x) for x in sorted(num_list)]))
##################################################

########## задача ПОЛИГЛОТЫ#############
# n = [[] for i in range(int(input('к-во шк = ')))]
# for i in range(len(n)):
#     n[i] = [int(input('к-во яз = '))]
#     for j in range(1, n[i][0]+1):
#         n[i] += [input('яз = ')]
# all_lang = set()
# all_pup = set()
# for i in range(len(n)):
#     all_lang = all_lang | set(n[i][1:])
# for i in range(len(n)):
#     all_pup = all_lang & set(n[i][1:])
# all_pup = list(sorted(all_pup))
# print(len(all_pup), *all_pup, sep='\n')
# # for i in all_pup:
# #     print(i)
# all_lang = list(sorted(all_lang))
# print(len(all_lang), *all_lang, sep='\n')
# # for i in all_lang:
# #     print(i)
################################# ЗАДАЧА ДЗ ####################

# students = [{input('Language = ') for j in range(int(input('Number of languages = ')))} for i in range(int(input('Number of students = ')))]
# everyone, someone = set.intersection(*students), set.union(*students)
# print(len(everyone), *sorted(everyone), sep='\n')
# print(len(someone), *sorted(someone), sep='\n')
########################

################## Задача ЗАБАСТОВКИ ##################
# n, k = map(int, input('number of days = ').split())
# zab = set()
# for i in range(k):
#     a_i, b_i = [int(s) for s in input('a_i b_i = ').split()]
#     while a_i <= n:
#         zab.add(a_i)
#         a_i += b_i
# print(len(zab - set(range(0, n+1, 7)) - set(range(6, n+1, 7))))
# s1 = set(d)
# s2 = set(range(0, n+1, 7))
# s3 = set(range(6, n+1, 7))
# print(set(s1), len(s1))
# print(set(s2), len(s2))
# print(set(s3), len(s3))
# print(set(d), len(d))
# s = s1 - s2 - s3
# print(s, len(s))
