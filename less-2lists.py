a = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 0], [9, 0, 1, 2, 8], [3, 4, 8, 9, 0]]

###########################################
# print('len =', len(a))
# print('a =', a)
# print()
#
#
# print(*a, sep='\n')
# print()
#
#
#
# print('a[3] =', a[3])
# print('a[3][1:3] =', a[3][1:3])
# print('a[0][1] =', a[0][1])
# print('a[1][1:3] =', a[1][1:3])

#########################################
# print('a =', a, id(a))
# print('.' * 20)
#
# a[0] = 5
# print('a =', a, id(a))
# print('.' * 20)
#
# a[0] = [9, 8, 7]
# print('a =', a, id(a))
# print('.' * 20)
#
# a[2][2] = [9] * 5
# print(*a, sep='\n')
# print('.' * 20)

##################################
# a.append(a)
# print('a =', a)
# print('a[-1][-1] =', a[-1][-1])
# print()
# print(a == a[-1][-1])
# print(a is a[-1][-1])
#
# print('------ *a -----------')
# print(*a, sep='\n')
# print()
# print('------ *a[-1][-1] -----------')
#
# print(*a[-1][-1], sep='\n')
#####################################################

# a = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 0], [9, 0, 1, 2, 8], [3, 4, 8, 9, 0]]
#
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         print(a[i][j], end='\t')
#     print()
#
# print()
# for row in a:
#     print(*row, sep='\t')

#######################################

a = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 0], [9, 0, 1, 2, 8], [3, 4, 8, 9, 0]]
######### Сумма элементов матрицы ##########
########### По индексу ####################
# sum_of_elements = 0
#
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         sum_of_elements += a[i][j]
# print(sum_of_elements)

######### По элементам ###################
#
# sum_of_elements = 0
#
# for row in a:
#     sum_of_elements += sum(row)
#     # for element in row:
#     #     sum_of_elements += element
# print('sum = ', sum_of_elements)

##############################################

a = [[1, 2, 3, 42, 5], [6, 777, 8], [9, 0, 1, 2], [3, 4]]
# ############ Печать матрицы ##################################


def my_print(x: list) -> None:
    for row in x:
        print(*row, sep='\t')
        # print(*row, sep='\t', end=' ')
        # print(id(row))



# my_print(a)

###############################################

# l1 = [1, 2, 3]
# # l2 = l1
#
# # l2 = list(l1)
# # l2 = l1.copy()
# l2 = [i for i in l1]
# l1[0] = 999
# print(l1, id(l1))
# print(l2, id(l2))


############ Заполнение матрицы ###################
# l1 = [1, 2, 3]
# l2 = [l1] * 2
# print('l1 =', l1, id(l1))
# print('l2 =', l2, id(l2))
# print()
# l1[0] = 9
# print('l1 =', l1, id(l1))
# print('l2 =', l2, id(l2))
# print()
# print('l2[0] =', l2[0], id(l2[0]))
# print('l2[1] =', l2[1], id(l2[1]))

###################################################

# n, m = 4, 5
# # a = [[0] * m] * n
# a = [[0] * m for i in range(n)]
# my_print(a)
# a[0][0] = 9
# a[2][1] = 8
# print()
# my_print(a)
# print()
# a[3][1] = 5
# a[2][2] = 98
# a[1][1] = 555
# my_print(a)

################################## X/0
# n, m = 3, 3
# # a = [['.'] * m] * n
# a = [['.'] * m for i in range(n)]
#
# my_print(a)
# print()

# for row in a:
#     print(row, id(row))
# print()

############# with MAP !!!!!!!!!!!!
a = [['.'] * 3 for i in range(3)]
#
# for i in range(5):
#     k, l = map(int, input('input coord = ').split()) # 1 2
#
#     # if i % 2:
#     #     a[k][l] = 'X'
#     # else:
#     #     a[k][l] = '0'
#
#     a[k][l] = 'X' if i % 2 else '0'
#
#     print()
#     my_print(a)
###############
# print()
# a[2][2] = 'X'
# a[2][1] = '0'
# a[0][1] = 'X'
# print()
# my_print(a)
# print(a, type(a))
# print()
# a[1][1] = 'X'
# a[0][2] = '0'
# a[0][0] = '0'
# print(*a)
# for row in a:
#     print(*row)
#
# print()
# my_print(a)
#


############# Ввiд довільної мариці ######################
# n = int(input('Number of rows = '))
# a = []
# for i in range(n):
#     print('Input ', i+1, " row of numbers with spaces : ", sep='', end='')
#     # row = list(map(int, input().split()))
#     row = input().split()
#     a.append(row)
# my_print(a)

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
########### То же в одну строчку ##############
# print(*[[j for j in input('input number with space : ').split()] for i in range(int(input('input number of rows = ')))], sep='\n')

# l1 = [[j for j in input('input number with space : ').split()] for i in range(int(input('n = ')))]
# my_print(l1)

# my_print([[j for j in input('input number with space : ').split()] for i in range(int(input('n = ')))])


################# Задачи из ДЗ ###############
###############################################
# 1 0 0 0
# 2 1 0 0
# 2 2 1 0
# 2 2 2 1
###############################################

############ version 1(full)
# n = int(input('n = '))
# l1 = [['.'] * n for i in range(n)]
# # my_print(l1)
# print()
# for i in range(n):
#     for j in range(n):
#         if i < j:
#             l1[i][j] = 0
#         elif i > j:
#             l1[i][j] = 2
#         else:
#             l1[i][j] = 1
# for row in l1:
#     print(*row)


############ version 2(short)


# n = int(input('n = '))
# l1 = [[0] * n for i in range(n)]
#
# for i in range(n):
#     for j in range(i):
#         l1[i][j] = 2
#     l1[i][i] = 1
# for row in l1:
#     print(*row)


############ version 3(analitic)


# n = int(input('n = '))
# l1 = [[2] * i + [1] + [0] * (n - 1 - i) for i in range(n)]
# my_print(l1)

# l1[2][2] = 8
# print()
# my_print(l1)
########################################
# 0 0 0 0 1
# 0 0 0 1 2
# 0 0 1 2 2       СПРОБУЄМ?
# 0 1 2 2 2
# 1 2 2 2 2
########################################




#
# n = int(input('n = '))
# l1 = [[0] * n for i in range(n)]
# for i in range(n):
#     for j in range(n-i, n):
#         l1[i][j] = 2
#     l1[i][n-1-i] = 1
# for row in l1:
#     print(*row)

#
#
# n = int(input('n = '))
# # l1 = [[2] * i + [1] + [0] * (n - 1 - i) for i in range(n)]
# l1 = [[0] * (n - 1 - i) + [1] + [2] * i for i in range(n)]
# my_print(l1)


########################################3

# 0 1 2 3 4
# 1 0 1 2 3
# 2 1 0 1 2
# 3 2 1 0 1
# 4 3 2 1 0
############################

# n = int(input('n = '))
# l1 = [[0] * n for i in range(n)]
# for i in range(n):
#     for j in range(n):
#         # l1[i][n-1-j] = n - 1 - j - i
#         l1[i][n-1-j] = abs(n - 1 - j - i)
# # for row in l1:
# #     print(*row)
# my_print(l1)





################# Эта же задача ##################
# n = int(input('n = '))
# # l1 = [[abs(j - i) for j in range(n)] for i in range(n)]
# l1 = [[-(i - j) for j in range(n)] for i in range(n)]
# my_print(l1)



########################################
# Pifagor's
#    1	2	3	4	5	6	7	8	9
#    2	4	6	8	10	12	14	16	18
#    3	6	9	12	15	18	21	24	27
#    4	8	12	16	20	24	28	32	36
#    5	10	15	20	25	30	35	40	45
#    6	12	18	24	30	36	42	48	54
#    7	14	21	28	35	42	49	56	63
#    8	16	24	32	40	48	56	64	72
#    9	18	27	36	45	54	63	72	81

######  ПРОБУЕМ!!!!!!????????????????????????????




n = int(input('n = ')) + 1
# #######
# p = [[0] * n for i in range(n)]
# for i in range(n):
#     for j in range(n):
#         p[i][j] = i*j
#
# my_print(p)

#########
# p = [[i * j for j in range(1, n)] for i in range(1, n)]
# my_print(p)
# print()


# my_print([[i * j for j in range(1, n)] for i in range(1, n)])





# my_print([[i * j for j in range(1, 11)] for i in range(1, 11)])


########################### END






############ Задача SWAP #################
# def swap_columns(a, i, j):
#     for k in range(len(a)):
#         a[k][j], a[k][i] = a[k][i], a[k][j]
        # a, b = b, a
#
# n = int(input('n = '))
# a = [0] * n
# max_ = 0
# for i in range(n):
#     a[i] = input("elements with space : ").split()
# my_print(a)
# i, j = list(map(int, input('i j = ').split()))
# swap_columns(a, i, j)
# my_print(a)



#########  То же с заполнением нулями   ##########
# n = int(input('n = '))
# a = [0] * n
# max_ = 0
# for i in range(n):
#     a[i] = input("elements with space : ").split()
#     if len(a[i]) > max_:
#         max_ = len(a[i])
# for i in range(n):
#     while len(a[i]) < max_:
#         a[i].append(0)
# my_print(a)
# i, j = list(map(int, input('i j = ').split()))
# swap_columns(a, i, j)
# my_print(a)