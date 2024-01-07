
#
# class A:
#     def __init__(self, num=0):
#         self.num = num
#
#     def add(self, num=1):
#         self.num += num
#
#
# class B(A):
#     def __init__(self, num=0):
#         A.__init__(self, num)
#         super().add(num)
#
#     def add(self, num=1):
#         self.num += 2 * num


# a = A(1)
# a.add()
# b = B(2)
# b.add(3)
#
# print(a.num+b.num)




# from faker import Faker
# import random
#
#
# fake = Faker()
# for i in range(5):
#     print(fake.name())
#     print(fake.sentences(1))
#     print(fake.sentences(3))
#     print(fake.year())
#     print(random.randint(1, 20))






# d1 = {'a': 'uykj', 'b': 'jhjhkjh'}
# # print(d1['c'])
# # print(d1.get('c'))
# print(type(d1))

# print(2+3)
# print('2'+'3')





# d1 = {'a': 'uykj', 'b': 'jhjhkjh'}
# d2 = d1.copy()
# d2['a'] = 7777
# print(d2)
# print(d1.keys())
# print(d1.values())
# print(d1.items())
# d3 = dict(d1.items())
# print(d3)









# d = {'a': 'yui', 'b': 'ytryutuy'}
# print(d.get('hgj'))








#  OR(+)           AND(*)          NOT       2 + 2 * 2 =
#  1 + 1 = 1     1 * 1 = 1       1    0
#  1 + 0 = 1     1 * 0 = 0       0    1
#  0 + 1 = 1     0 * 1 = 0
#  0 + 0 = 0     0 * 0 = 0

# if True or True and False:
#     print('YES')
# else:
#     print('NO')

# l = [678, 879]
# t = (34, l)
# print(t)
# l.append(87090)
# l = 'hjgjh'
# print(l)
# print(t)






# t = ('hello',)
# print(list(t))
# print(len(list(t)))

# t1 = ['Hello, ']
# t2 = ['world!']
# print(id(t1))
# t1 += t2
# print(id(t1))
# print(t1)



# d = {'key': 879, 'ke1': 'jhkj'}
# # print(d['l'])
# print(d['key'])
# print(d.get('l'))
# print(d.get('key'))

# a = {1, 2, 'a'}
# # b = {1, 2, 3}
# b = c = a
# c.add(999)
# print('a=', a)
# print('b=', b)
# print('c=', b)
# print(a == b)
# print(a is b)
# print(c is b)

# print(id(a))
# print(id(b))


# d = (2,)
# print(type(d))
# print(type(d) == tuple)
# print(len('https://www.figma.com/Cq4tEJDt'))
# breakpoint()
#
#
# import string
# from random import choice
#
#
# def generate_short_id(num_of_chars: int):
#     """Function to generate short_id of specified number of characters"""
#     return ''.join(choice(string.ascii_letters+string.digits) for _ in range(num_of_chars))
#
#
# num_of_chars = 7
#
# print(generate_short_id(num_of_chars))
