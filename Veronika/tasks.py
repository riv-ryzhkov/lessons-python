# n = int(input('n = '))
# en_dic = []
# lat_dic = {}
# for i in range(n):
#     inp = input('en_word : ').split(' - ')
#     en_dic.append([inp[0].strip(), inp[1].split(', ')])
# print(en_dic)
# # en_dic = [['punishment', ['malum', 'multa']], ['fruit', ['baca', 'bacca', 'popum']], ['apple', ['malum', 'pomum', 'popula']]]
# for i in en_dic:
#     for j in range(len(i[1])):
#         if i[1][j] not in lat_dic.keys():
#             lat_dic[i[1][j]] = i[0]
#         else:
#             lat_dic[i[1][j]] += ' ' + i[0]
# # print(lat_dic)
# list_lat_dic = list(lat_dic.items())
# # print(list_lat_dic)
# for i in range(len(list_lat_dic)):
#     list_lat_dic[i] = [list_lat_dic[i][0], sorted(list_lat_dic[i][1].split())]
# # print(list_lat_dic)
# list_lat_dic.sort()
# print(len(list_lat_dic))
# for i in range(len(list_lat_dic)):
#     key = list_lat_dic[i][0]
#     vaule = list_lat_dic[i][1]
#     print(key, end=' - ')
#     print(*vaule, sep=', ')




# A = [''] * 8
# B = [''] * 8
# Answer = 'NO'
# for j in range(8):
#     A[j], B[j] = [int(i) for i in input().split()]
# print(A)
# print(B)
#
# for j in range(8):
#     for k in range(j+1, 8):
#         if abs(A[j] - A[k]) == abs(B[j] - B[k]) or A[j] == A[k] or B[j] == B[k]:
#             Answer = 'YES'
# print(Answer)




# s = input('ведите рост учеников через пробелы').split()
# print(s)
# petr = int(input('введите рост Пети'))
# index = 0
# while index < len(s) and int(s[index]) >= petr:
#     index += 1
# print(index + 1)








# number = int(input())
# before = number
# count = 0
# while number != 0:
#     if number > before:
#         count += 1
#     before = number
#     number = int(input())
# print(count)









# n = int(input())
# delitel = 2
# while n % delitel != 0:
#     print(delitel, 'не подходит!')
#     delitel += 1
# print('подходит ->', delitel)







# n = int(input())
# factorial = 1
# for i in range(2, n + 1):
#     factorial = factorial * i
#     print(factorial)
# print('factorial=', factorial)