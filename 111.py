from alive_progress import alive_bar
import time

for x in 3000, 4000, 2000, 0:
    with alive_bar(total=x) as bar:
        for i in range(3000):
            time.sleep(.0002)
            bar()




# print(5 < 10)
# print('t' < 'bcdgjlkhlkjhklj')
# print([1, 2, 3] < [0, 45, 788, 999, 333, 6666])



# print(5 + 10)
# print('5' + '10')
# print([5] + [10])




# def inp_():
#     pass
#
#
# def screen():
#     pass
#
#
# def pr_():
#     pass









# print(__name__)


# lst = [0, 1, 2]
# l1 = reversed(lst)
# l2 = sorted(lst)
# print(type(l1))
# print(type(l2))
# print(next(l1))
# print(next(l1))
# print(next(l1))
# print(reversed(lst))
# print(lst.reverse())
# print(lst[::-1])
# print(reversed(lst) == lst[::-1])
# print(list(reversed(lst)) == lst[::-1])


# lst1 = (1, [2, 3])
# # lst2 = (1, [2, 3])
# lst2 = lst1
# print(lst1 == lst2)
# lst2[1].append(4)
# print(lst1 == lst2)
# print(lst1, lst2)



# # lst = (22, 33, 44, 55, 66, 77)
# # lst = [22, 33, 44, 55, 66, 77]
# lst = range(10)
# a, b, *c = lst
# print(a)
# print(b)
# print(c)



# a = [15]
# b = [33]
# print(a + b)


# t = 555.2334
# t1 = 'Hello'
# print('text : %f' % t)
# print('text : %i' % t)
# print('text : %d' % t)
# print('text : %s' % t1)
