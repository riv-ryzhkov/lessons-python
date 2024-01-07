# Упорядоченная изменяемая последовательность объектов

# l = [1, 2, 3, 4, 5]
# l = 'Hello'
# l1 = l
# print('l->', type(l), l, id(l))
# print('l1->',type(l1), l1, id(l1))
# # l1[3] = 5555
# l1 = 'h' + l1[1:]
# print('l->', type(l), l, id(l))
# print('l1->',type(l1), l1, id(l1))







# l1 = [23, 789.89, 678]
# print(max(l1))
# print(min(l1))
# print(sum(l1))
# print(len(l1))



# l1 = [23, 'sdf', True, [1, 2, [3, 4, 6]], 9999]
# print(l1, id(l1))

# l = [1, 2, 3]




# l = []                      # False  ''  []  ()   {}  0
# print(type(l), l, id(l))
#
# l = list('Hello')
# print(type(l), l, id(l))




# text = 'Hello!'
# l = list(text)
# print(type(l), l, id(l))




# l1 = [1, 2, 3]
# print(l1, id(l1))
# l1 += l1
# l1 *= 2
# l1 = l1 * 5
# l1 = l1 + [222, 333]
# l1 += [222, 333]
# l1.append(666)
# l1.append([444, 666])
# l1 += [444]
# print('l1=', l1, id(l1))


# l1.extend([444, 666])
# l1 += [444, 666]
#
# print('l1=', l1, id(l1))

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# print(l1.append(444))
# print(l1.extend([444]))
# print(l1, id(l1))







# text1 = 'Hello wolrd! jkhkj kjh khk kj kjh kjhkjh kjhk hjk'
# l1 = text1.split()
# print(l1, type(l1))
#
# text2 = ' '.join(l1)
# print(text2, type(text2))










# l1 = [1, 2, 3, 444, 5, 1, 444, 3, 1, 444, 444]
# print(l1, id(l1))
# l1.insert(5, 'XXX')
# print(l1.insert(5, 'XXX'))
# l1.remove(444)

# l1.pop()
# res = l1.pop(3)
# # # l1.pop()
# res = l1.pop(l1.index(444))
# print(l1, id(l1))
# print(res)



# print(l1.count(1111))
# s = 444
# # if l1.count(s):
# while l1.count(s):
#     l1.remove(s)
# else:
#     print('No number!')
# print(l1, id(l1))



# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# a = [1, 7, 3, 9, 1, 9, 0, 6, 4, 2, 8, 3]
# print(a)
# insert
# index
# pop
# max
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# for i in range(len(a)):
#     # a.insert(i, a.pop(a.index(max(a[i:]), i)))
#     a.insert(i, a.pop(a.index(min(a[i:]), i)))
# #     print(a)
# print(a)






# l1 = [1, 2, 3, 4, 5]
# print(l1, id(l1))
# # l1.reverse()
# # print(l1, id(l1))
# l1 = l1[::-1]
# print(l1, id(l1))





l = [-2, 1.23, 1, 1.99, 0, -5, 8]
# l.sort(reverse=True)
# l.sort(key=int)
# print(l, id(l))
# l.sort(key=abs)
# l.sort(key=abs, reverse=True)
# lll = l.sort(reverse=True)
# print('res =', lll)
# print(l, id(l))





# l1 = [1, 4, -2, 77, 0, 3, 1, -9]
# l1 = ['ab', 'h', 'W', '2', 'A', 'aaa', '22222222']
# l1.sort()
# # # l1.sort(reverse=True)
# print(l1)
# #
# for i in l1:
#     print(ord(i[0]), '->', i)










# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# a = 'aaax'
# b = 'aaaaaa'
# print(a > b)






# !!!!!!!!! Генератори Списків !!!!!!!!!!!

# l1 = list(range(10))
# l1 = [i for i in range(10) if i % 3]
# print(l1)



# l1 = ['*'*i for i in range(10) if i % 2]
# l1 = [i**2 for i in range(10) if i%2]
# print(l1)




# l1 = [str(i)+str(k) for i in range(10) if i % 2 == 0 for k in range(5) if k % 2]
# l2 = ['a', 'b', 'c']
# print(l1, type(l1))
# print(l2, type(l2))
# l3 = l1 + l2
# print(l3, type(l3))



# l2 = [i + str(k) for i in 'Hello' for k in range(4) if k % 2 != 0]
# print(l2, id(l2))




# l3 = [i for i in range(8)]
# print(l3)
# print(*l3)
# print(*l3, sep='')





import random

# print(*dir(random), sep='\n')

# for i in range(10):
#     print(random.randint(3, 10))
#     print(random.uniform(3, 10))
#     print(random.random())
#     print('='*40)


#
# n = 10
# a = [random.randrange(1, 10) for i in range(n)]
# print(a)



l = [1, 2, 'XXX', 4, True, 6]
# for i in range(10):
#     print(random.choice(l))
#
# print(*random.choices(l, k=10))


from random import randint


# l1 = list(range(36))
# print(l1, id(l1))
# for i in range(200):
#     l1.append(l1.pop(randint(0, len(l1)-1)))
# print(l1, id(l1))




# l1 = ['0'*(i+k) for i in range(1, 16) if i % 2 == 0 for k in range(1, 6) if k % 2]
# # print(['0'*(i+k) for i in range(1, 16) if i % 2 == 0 for k in range(1, 6) if k % 2])
# print(l1, id(l1))
# print([int(i) for i in l1[:6]])







# l0 = ['A', 67, 'DDD']
# print('AA' in l0)
# l0 = 'Hello'
# print('A' in l0)
# for i in l0:
#     print(i)



# l2 = ['bb', 'ttt', 888]
# l1 = [str(i) + '->' + str(k) for i in l0 for k in l2]
#
# print(*l1, sep=' ')
# for i in l1:
#     print(i)





# l1 = list('hello')
#
# symbol = input('sym = ')
#
# if l1.count(symbol):
#     l1.remove(symbol)
# else:
#     print('No symbol', symbol)
#
# # while l1.count(symbol):
# #     l1.remove(symbol)
#
# print(*l1, sep='')






############## !!!!!!!!ВАЖЛИВО!!!!!!!!!!!!!!!!!!!!!!!!!
l1 = [1, 2, 3, 4, 5]
# l2 = l1
# print(l1, id(l1))
# print(l2, id(l2))
# l2.append(999)
# print(l1, id(l1))
# print(l2, id(l2))


# l2 = l3 = l4 = l1
# print('=' * 20)
# print('L1 =>', l1, id(l1))
# print('L2 =>', l2, id(l2))
# print('L3 =>', l3, id(l3))
# print('L4 =>', l4, id(l4))
# print('=' * 20)
# l3[0] = 999
# print('L1 =>', l1, id(l1))
# print('L2 =>', l2, id(l2))
# print('L3 =>', l3, id(l3))
# print('L4 =>', l4, id(l4))
# print('=' * 20)
# l2 = l1.copy()
# l2 = l1[:]
# l2 = list(l1)
# l1[0] = 7777777
# print('L1 =>', l1, id(l1))
# print('L2 =>', l2, id(l2))
# print('L3 =>', l3, id(l3))
# print('L4 =>', l4, id(l4))





# l1 = [str(i+1) * k for i in range(8) if i%2 != 0 for k in range(1, 4)]
# # l1 = [int(str(i+1) * k) for i in range(8) if i%2 != 0 for k in range(1, 4)]
# print(l1, id(l1))
#
# l1.sort(reverse=True)
# # l1.sort()
# # l1.reverse()
# # l1 = l1[::-1]
# print(l1, id(l1))



#
#
# l = [i for i in 'Hello, world!']
# print(l, id(l))
# # del l[2:6]
# # del l
# print(l, id(l))
# l.clear()
# # l = []
# # l = list()
# print(l, id(l))



############# ПРИМЕРЫ ))))))))))))))))))))))
# n = ''
# l1 = []
# while n != 'exit':
#     l1.append(n)
#     n = input('Input new name, please : ')
#
# for name in l1:
#     print(f'Dear {name}! Happy new Year!')



# print(*[input(str(i+1) + "'s element = ") for i in range(int(input('n = ')))])


# !!!!!!!!!! Тосовка карт (білетів)!!!!!!!!!!!

# !!!!!!!!!!!  Якщо всі елементи різні !!!!!!!!!!!!!!!!!!!!!
# import random
#
# l1 = [i for i in range(10)]
# for i in range(30):
#     l2 = random.choice(l1)
#     l1.remove(l2)
#     l1.append(l2)
# print(l1)

# !!!!!!!!!!!! Для будь-яких елементів !!!!!!!!!

# l1 = [i for i in range(10)]
# for i in range(30):
#     l2 = l1.pop(randint(0, len(l1)-1))
#     l1.append(l2)
# print(l1)



################## END








# print(''.join(l1))


# class1 = input('input n with space : ').split()
# petya = int(input('Petya = '))
# count = 1
# while count <= len(class1):
#     if petya <= int(class1[count-1]):
#         count += 1
#     else:
#         print(count)
#         break



# l1 = [123, '234', -2344, '35', '-35']
# l2 = list(map(int, l1))
# # l2 = map(int, l1)
# print(max(l2), type(l2))
# l1 = [i for i in range(1, 9)]
# l2 = [i**2 for i in range(1, 6)]
# print(*l1)
# print(*l2)
# l3 = list(zip(l1, l2))
# print(l3)
# for i, k in zip(l1, l2):
#     print(i, '->', k, sep='', end=' ')


#
# l1 = [str(i) * k for i in range(100) if i%2 != 0 for k in range(1, 5) if k%3==0]
# # for i in range(100):
# #     l1.append(i+1)
# print(*l1)
# for i in l1:
#     print(i, end=' ')
# print(*l1)
# # l1.clear()
# # del l1
# # print(l1[:3])
# # l1 = []
# print(l1, id(l1))


# # l1 = l1[::-1]
# l1.reverse()
# # l2 = sorted(l1)
# print(l1, id(l1))
# print(l2, id(l2))
# symbol = int(input('num = '))
# if l1.count(symbol):
#     print(l1[l1.index(symbol):])
# else:
#     print('No symbol', symbol)
# l2 = l1.count(333)
# l2 = l1[:l1.index(33)]
# l1.append(l1.pop(3))
# l1.append(l1.pop(3))
# print(l2)

# l = ['34', '12', '89', '1222', '5']
l = [1, 2, 3, 4, 5]
# print(l, id(l))

# l = []
# l.clear()

# l1 = l
#
# l1 = l.copy()
# l1 = list(l)
# l1 = l[:]


# l1 += [7]
# print('l :', l, id(l))
# print('l1 :', l1, id(l1))




# l.reverse()
# l = l[::-1]





# for i in range(255):
#     print(i, '->', chr(i))



# import random
#
#
# l = [i for i in range(36)]
# print(l)
# for i in range(200):
#     l.append(l.pop(random.randint(0, 35)))
# print(l)





# text = 'Hello, world!'
# # print(text[:6] + ' 678678608 ' + text[7:])
# l1 = text.split()
# l1.insert(1, 'hgjghkjhk')
# print(' '.join(l1))
# l2 = ['!!!!!!', 687, 678687]
# print(l1, type(l1), id(l1))
# # l1 += l2
# # l1.extend(l2)
# l1.insert(1, '8797897-98')
# # l1 = l1[:1] + ['8797897-98'] + l1[1:]
# print(l1, type(l1), id(l1))
# print(len(l1))
# text1 = ' '.join(l1)
# print(text1, type(text1))


# l1 = [23, 789.89, 8798, 99999]
# l2 = l1
# l2 = l1[:]
# l2 = l1.copy()
# l2 = list(l1)
# print(l1, id(l1))
# l1.append(23234)
# print(l1, id(l1))
# print(l2, id(l2))



# l2 = [23, 789.89, 678]
# print(max(l1))
# print(min(l1))
# print(sum(l1))
# print(len(l1))

# l2 = list('Hello')
# print(l1 == l2)
# print(id(l1) == id(l2))
# print(l1 > l2)
# print(l1 < l2)
# print(l1, id(l1))
# l1 = l1 + l1
# print(l1, id(l1))
# print(l2, id(l2))
# print(l3, id(l3))

# l3 = l1
# print(l1, id(l1))
# # print(l2, id(l2))
# l3.append(9999999)
# print(l1, id(l1))
# print(l3, id(l3))




# text = 'Hello, world!'
# symbol = '='
# l1 = [i * k for i in text if i != 'l' for k in range(4) if k%2 != 0]
# l1 = [symbol*i for i in range(1, 5)] * 5
# for i in range(100):
#     l1.append(i)
# print(*[i * k for i in text if i != 'l' for k in range(4) if k%2 != 0])


# l1 = [567, '45', 48, '49', 45, 7, 48, 49]
# l1 = list('abcdefgh')
# print(l1)
# l2 = list(map(ord, l1))
# print(l2)
# l3 = list(zip(l1, l2))
# l3 = list(zip())
# for i, k in zip(list('abcdefgh'), list(map(ord, l1))):
#     print(i, '->', k, sep='', end=' ')


# print(l1)
# print(l2)
# print(l3)

# l2 = [567, 45, 'bcd']
# print(l1, id(l1))
# # l1.sort(reverse=True)
# # l1.reverse()
# l1.clear()
# del l1[:]
# print(l1, id(l1))
# if l1.count(45):
#     print(l1.index(99))
# else:
#     print('No symbol!')

# print(l1.count(999999))
# print(l1.index(49, 5, 8))
# l1.extend(l2)
# l1 += l2
# l1.insert(2, 'ABC')
# l1.remove(48)
# l3 = l1.pop(4)

# del l1[4:8]
# del l1[:]
# print(l1, id(l1))
# # del l1
# print(l1, id(l1))
# l1 = []
# print(l1, id(l1))
# l1 = l1[:2] + ['ABC'] + l1[2:]
# print(l1)

# l2 = l1.copy()
# l2 = l1[:]
# l2 = list(l1)
# l2.append(l1)

# s = input().split()
# print(s, type(s))
# s1 = '*'.join(s)
# print(s1, type(s1))


# del l1[:]
# ll = l1.index(48)
# print(l1, id(l1))
# print(ll, id(ll))
# print(l1.index(48, ll + 1))
# l1.insert(1, 'jhkjk')
# # l1[1] = 9999
# print(l1, id(l1))
# l1.remove(45)
# print(l1, id(l1))

# number = int(input('number = '))
# counter = l1.count(number)
# num_l1 = -1
# for i in range(counter):
#     num_l1 = l1.index(number, num_l1+1)
#     print(num_l1, end=' ')
# print()
# for i in range(len(l1)):
#     if l1[i] == number:
#         print(i, end='-')

# print(l1, id(l1))
# l2 = [-234, 34, 56]
# l1.extend(l2)
# # l1 += l2
# print(l1, id(l1))

# print(sum((l1 + l3)))
# print(max(l3))
# print(sum(l3))
# print(len(l3))
# # l2 = [234, 324, 67]
# # print(l1 == l3)
# print(l1 > l3)
# print(l1 < l3)
#
# for i in range(256):
#     print(i, '-', chr(i), sep='', end='  ')



# l1.append(input('Input new name, please : '))
# for name in l1:
#     print(f'Dear {name}! Happy new Year!')



# l2 = [1, 2, 3]
# print(l1, id(l1))
# print(l2, id(l2))
# print(l1 == l2)
# print(id(l1) == id(l2))



# a = int(input('a = '))
# l2 = list(str(a))
#
# print(l1, id(l1))
# l2.append(999)
# print(l1, id(l1))
# print(l2, id(l2))



# text = 'Hello'
# print(text, id(text))
# text = text[1:]
# print(text, id(text))



# l1 = ['a', 4.56, [4, 76, 89]]
# l2 = [0, 1, 45/23]
#
# print(l1)
# print(l2)
# l1 = l1.append(99999)
# print(l1)
# print(l1, id(l1))
# l1.extend(l2)
# l1 += l2
# print(l1, id(l1))
# print(l1, id(l1))
# l1.append(l2)
# print(l1, id(l1))
# l2.append(9)
# print(l1, id(l1))
# print(len(l1))

# print(min(l1))
# print(max(l1))
# print(len(l1))
# print(sum(l1))

# text = 'Hello, world!'
# l1 = list(range(15, 25, 2))

# l2 = []
# for i in text:
#     l2.append(i)

# # print(len(l1))
# print(l1, 'l1', id(l1))
# # print(l2, 'l2')
# l1[0:3] = range(4)
# print(l1, 'l1', id(l1))
#
# for i in range(len(l1)):
#     l1[i] = str(l1[i])
#
# print(l1)
# t2 = 'How are you!'
# l2 = t2.split()
# print(t2)
# print(l2)
# print('***'.join(l1))

# text = 'fg546567 uyf6r76 tjk 087687 u'
# l1 = text.split()
# print('-'.join(l1))





#
# l2 = list(l1)
# l2 = l1.copy()
# l2 = l1[:]

# print(l1 == l2)
# print(id(l1) == id(l2))
# print(id(l1))
# print(id(l2))

# print(l1, 'l1->', id(l1))
# print(l2, 'l2->', id(l2))
# print(l3, 'l3->', id(l3))












#
# print(len(a))
# print(a)
# for i in range(len(a)):
#     if i % 2 == 0:
#         print(a[i], end=' -> ')


# a = [1, 2, 3, 4]
# a.append(a)
# print(a)
# print(a[-1])


# print(*['=' * (i+1) for i in range(int(input('n = ')))], sep='\n')

# a = [[i] for i in range(5)]
# print(*a)
# for i in a:
#     i += [1111]
# print(*a)




# print()
# a = [str(i) + '+' + str(j) + '=' + str(i + j)
#      for i in range(5) if i % 2 == 0
#      for j in range(9) if j % 3 == 0]
# print(*a)

# print()
# a = [input('Введите ' + str(i+1) + '-й элемент : ') for i in range(int(input('n= ')))]
# print('\n' * 3)
# print(a)
# print('=' * 30)
# print(*a)

# a = list(range(5))
# print(a)



# a = []
# n = int(input('n= '))
# for i in range(n):
#     a += ['*' * i]
# print(a)

# a = ['*' * (i+1) for i in range(int(input('n= ')))]
# # a = [i**2 for i in range(15) if i % 2]
# print(a)
# for i in a:
#     print(i, end=' ')
# print()
# print(*a, sep='|')





# a = ['ivan', '26', '260', 'Popov', '26', 'man']
# b = a
# print(a)
# a.sort()
# print(a)
# print(b, 'b')
# c = a.sort()
# print(a)
# print(c)


# a = [1, 2, 3, 4]
# b = a         # СВЯЗАНЫ

# b = a.copy()  # НЕ СВЯЗАНЫ
# b = a[:]      # НЕ СВЯЗАНЫ
# b = list(a)   # НЕ СВЯЗАНЫ


# a[0] = 999999999
# print('a=', a, id(a))
# print('b=', b, id(b))


# a = [1, 2, 3]
# b = [5, 6, 7, 7, 7, 7]
#
# # b.reverse()
# b.sort()
#
# print(a)
# print(b)
#
# res = 0
# for i in range(1, 5):
#     for j in range(1, 8):
#        res += i * j
# print(res)


# a = [i**2 for i in range(5) if i % 2 == 0]



#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# print(*[input(str(i+1) + "'s element = ") for i in range(int(input('n = ')))])
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# b = ''
# n = int(input('n='))
# for i in range(n):
#     if not (i % 2):
#         a = input(('el'))
#         b += a + ' '
# print(b)


# a = ['Ivan', 'Popov', '26', 'man']
# b = ' '.join(a)
# print(a, type(a))
# print(b, type(b))
#
# # split()   ''.join(l)

#
# n = int(input('Сколько вас? '))
# res = []
# for i in range(n):
#     txt = input('введите через пробел Имя и Фамилию : ')
#     a = txt.split()
#     res.append(a)
# print('\nВас реально ', len(res), ':')
# for i in res:
#     print(res.index(i) + 1, '->', i[0], i[1])
# print('\n', *res)

# from random import randint
#
# a = [1, 2, 3] * 3
# for i in range(len(a)):
#     a.append(a.pop(randint(0, len(a)-1)))
# print(a)




# b = [5, 6, 7]
# c = a * 3
# c = []
# a.append(44444)
# a.append('ghjk')
# c = a.append('00000')
# b[0] = 7
# b = list(a)
# b = a.copy()
# print('a=', a)
# print('b=', b)
# print('c=', c)


#
# a = [1, 2, 3, 4]
# print(a[:])# [1;3)


# a = [1, 2, 3]
# b = a.copy()
# b[0] = 0
# print(a)
# print(b)
# c = a + b + [5]
# # c.reverse()
# print('c=', c)
# # print('d=', d)


# n = 7
# a = [i+1 for i in range(n)]
# b = [(i+1)**2 for i in range(n)]
# c = [(i+1)**3 for i in range(n)]
# d = [list(k) for k in zip(a, b, c)]
# print('=' * 30)
# print('x', 'x^2'.center(4, ' '), 'x^3', sep='\t\t')
# print('=' * 30)
# for i in d:
#     print(*i, sep='\t\t')
# print('=' * 30)
# for i in d:
#     i = map(lambda w: ('<'+str(w)+'>').center(8, ' '), i)
#     print(*i)
# print('=' * 30)
# print(d)


# a = ['W', 222, 300, 4, 5]
# b = ['w', 222, 300, 4, 5, 6]
# print(a.index(222))
# print(f'{b+a} hjkh kjhjkb')
# print(min(a))
# print(max(a))
# print(sum(a+b))
# print(id(a), id(b))
# print(a > b)
# l2 = 'Hello'
# l1 = [ord(i) + k + m
#       for i in l2 if ord(i) < 100
#       for k in range(4) if k % 2
#       for m in range(4) if m % 2 == 0]
# l1 = [i**2 for i in range(1, 10) if i % 2]
# l1 = list(range(1, 7))
# l2 = [i**2 for i in l1]
# print(l1)
# print(l2)
# def sqr(x):
#     return x**2
#
# def foo(x):
#     return type(x) == int


# l1 = [1, '2', 3, '4', '34', 23]
# l2 = list(map(int, l1))
# n = 5
# l3 = list(map(lambda x: x*n, l2))
# l4 = list(filter(lambda x: type(x) == str, l1))
# l4 = list(filter(foo, l1))
#
# print(l1)
# print(l2)
# print(l3)
# print(l4)

# l1 = [i for i in range(1000)]
# l2 = list(filter(lambda x: x % 2 == 0, l1))
# l3 = list(zip(l1, l2, l1, range(20)))
# print(l1)
# print(l2)
# print(l3)
# print(list(map(lambda x: x ** 2, l1)))
# text = 'Hello'
# l1 = list(text)
# print(l1)
# print(list(enumerate(l1)))
# print(list(zip(range(len(l1)), l1)))
# l1 = ['Dnepr', 'Kiev', 'Lviv']
# l2 = [1000000, 4500000, 900000]
# print(list(zip(l1, l2)))