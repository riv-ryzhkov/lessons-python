#
#
# a = [[0] * 5] * 5
# print(a)
# a[0][0] = 3
# print(a)
#
#
#
#
# # a = [[0] * 5 for i in range(5)]
# # print(a)
# # a[0][0] = 3
# # print(a)
#
#


#
# # n = int(input('number of lines = '))
# # a = [[int(j) for j in input().split()] for i in range(n)]
# #
# # for i in a:
# #     print(*i)
#
#
# n = 5
# a = [[1] * n for i in range(n)]
# for i in range(n):
#     for j in range(n):
#         if i < j:
#             a[i][j] = 0
#         elif i > j:
#             a[i][j] = 2
# for row in a:
#     print(*row)
#     # print(' '.join([str(elem) for elem in row]))
#
#
#
#
# a = [[i * j for j in range(1, 11)] for i in range(1, 11)]
# for i in a:
#     print(*i, sep='\t')
    # print(*i)

# a = input().split()
# print(a)



# n = 3
# a = []
# for i in range(n):
#     a.append([j for j in input().split()])
# print(*a)
# for i in a:
#     print(*i, sep='\t')






# for i in range(1, 11):
#     for j in range(1, 11):
#         print(i * j, end="\t")
#     print()