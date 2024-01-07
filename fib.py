# def foo():
#     a = 1
#     print(a)
#
#
# a = 0
# print('a=', a)
# foo()
# print('a=', a)










# def maxi(*a):
#     print(a)
#     res = a[0]
#     for i in a:
#         if i > res:
#             res = i
#     return res
#
#
# print(maxi(1, 15, -7, 9, 0, 8989, 87))

# def pr(a, b='No Data'):
#     print(a, b)
#
#
# print(pr(2))









num = int(input('n= '))

def fibonacci(n):
    res = [0, 1]
    for i in range(2, n):
        res.append(res[i-1]+res[i-2])
    print(*res)
    return res

a = fibonacci(num)
print(a)
input('Thanks for running!')



#
# def fibonacci(n):
#     def fib(n):
#         if n == 0 or n == 1:
#             return n
#         else:
#             return fib(n-1) + fib(n-2)
#     return fib(n)
#
# print(fibonacci(int(input(' ведите число : '))))






# def fib(n):
#     if n < 2:
#         return n
#     else:
#         return fib(n - 1) + fib(n - 2)
#
#



# for i in range(0, int(input(' ведите число : '))+1):
#        print(fib(i), end=' ')







# print(fib(int(input(' ведите число : '))))


# num = int(input())
#
# def fibonacci(n):
#     def fib(n):
#         if n == 0 or n == 1:
#             return n
#         else:
#             return fib(n-1) + fib(n-2)
#     for i in range(0, n+1):
#         print(fib(i))
#
# fibonacci(num)
#



# #
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return factorial(n - 1) * n
#
# print(factorial(9))




# def reverse():
#     x = int(input())
#     if x != 0:
#         reverse()
#     print(x)
#
# reverse()






# multi = lambda x, y: x * y - y**2
#
# print(multi(2, 4))









# a = [1, 2, 3]
#
# print(list(map(lambda x: x**2, a)))





# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
#
# new_list = list(map(lambda x, y: x + y, l1, l2))
# print(new_list)


#
# a = [1, 2, 3, 4, 5, 8]
#
# # for i in map(lambda x: x**2, a):
# #     print(i)

# print(list(filter(lambda x: x % 2 != 0, a)))



# def foo(a, b=3):
#     print(a, b)
#
# foo(1, 6)



















# from functools import reduce
# items = [1, 2, 3, 4, 5]
# sum_all = reduce(lambda x, y: print(x, y), items)
#
# print(sum_all)