
# for i in range(100):  # 0, 1, 2, 3, 4   [0;5)
#     print(i)
# print('END of cycle')





# print(float(True))


# for i in 'Hello', 1.567, 2**2, True, 8/2*4+16:
#     print(i*2, type(i))
#     print('*************')
# print('================')







# for i in 2, 5, 78, 'Hello', 89-3:
#     # print(i, i*2)
#     # print(i, i*2, sep=' ', end='\n')
#     print(i, i*2, sep='', end='')






# a = range(5)  #  [0; 5)   0 1 2 3 4
# print(a)




# for i in range(33, 15, -2):  # [0; 5)
#     print(i)






# for i in range(30, 45, 2):   #  [30:45)
#     print(i, end='\t\t')
#     print(i*2, end='\t')
#     print(i*3, end='\t\t')
#     print(i*10, end='\t')
#     print()
#     # print(i, end='\t\t')



#
# i = 100
# for i in range(3):
#     for j in range(7):
#         print(i+1, j+1, sep='', end='\t')
#     print()
# print(i)

# i = 1000
# for i in range(5):
#     print('!!!!!')
# print(i)






# a, b, c, d = 2, 7.68, 'Hello', 4
#
# print(a, b, c, d)






# a, b, c, d = range(4)   # [0;4)
#
# # a, b, c, d = range(-4, -8, -1)
# print(a, b, c, d)


# 5! = 1 * 2 * 3 * 4 * 5
# a = int(input('a = '))
#
# result = 1
# for i in range(1, a+1):
#     # result = result * i
#     result *= i
# print(result)

# a = 5
# # a = a // 1
# a **= 2
# print(a)





 # sum = 1 + 2 + 3 + 4 + 5
# num = int(input('num= '))
# sum_ = 0
# for i in range(1, num+1):
#     sum_ += i
# print("Сумма чисел до: ", num, "=", sum_)
#
# print(sum(range(num+1)))






# for i in range(7):
#     if i % 2:
#         continue
#     print(i, '!!!!')
#     if i == 4:
#         continue
#     for j in range(10):
#         if j % 2:  # j%2=0    j%2=1
#             print(i, '->', j, end='\t')  # 6 * 5 = 30
#     print('\t\t', i)


# for i in range(10):
#     a = int(input('a='))
#     if a > 0:
#         continue
#     print(a, a, a, a, a)



#
# for i in range(10000000):
#     if i % 2 == 0:
#         print(i, 'Super!')
#         continue
#     elif i % 15 == 0:
#         print(i, 'Stop!')
#         break
#     print(i)
# else:
#     print('No 15 )))))))))')
#
# print('END')


# ================ ELSE in for !!!! ===============

# a = 'How are You!'
# for i in a:
#     # print(i)
#     if i == 'o':
#         print(i * 3, end='')
#         continue
#     elif i == 'y':
#         print(i * 5)
#         break
#     print(i, end='')
# else:
#     print('\nNo symbol y!!!')


#
# a = 34 - 29
# for i in range(7):
#     if i == 3:
#         print(i, i, i, i)
#         continue
#     elif i == 5:
#         print(i**2, '!!!!!!!!!!!!')
#         break
#     print(i, i**2, type(i))
# else:
#     print('No number 5!!!!')
# print('.' * 80)






# !!!!!!!!!!!!!!!!!   2 4 6 8 10 12

# !!!!!!!!!!!!!!!!!   -15 -12 -9 -6







a = [i for i in range(20) if i % 2 == 0]
# a = [i for i in 'Hello']
# a = [i for i in 'Hello' if i != 'l']
print(a)
