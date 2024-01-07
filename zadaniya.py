#
#
# ############# Engl-Latin Dictionary
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
# for i in range(len(list_lat_dic)):
#     key = list_lat_dic[i][0]
#     value = list_lat_dic[i][1]
#     print(key, end=' - ')
#     print(*value, sep=', ')
# ##################################################
#

# from collections import defaultdict
#
# latin_to_english = defaultdict(list)
# for i in range(int(input())):
#     english_word, latin_translations_chunk = input().split(' - ')
#     latin_translations = latin_translations_chunk.split(', ')
#     for latin_word in latin_translations:
#         latin_to_english[latin_word].append(english_word)
#
# print(len(latin_to_english))
# for latin_word, english_translations in sorted(latin_to_english.items()):
#     print(latin_word + ' - ' + ', '.join(english_translations))

#####################################
########## zad. ПРОДАЖИ ##################
# dic = {}
# inp = 'text'
# while inp:
#     inp = input()
#     if not inp:
#         break
#     key, value, quant = inp.split()
#     if key in dic.keys():
#         if value in dic[key].keys():
#             dic[key][value] += int(quant)
#         else:
#             dic[key][value] = int(quant)
#     else:
#         dic[key] = {value: int(quant)}
# # print(dic)
# list_dic = list(dic.items())
# list_dic.sort()
# # print(list_dic)
# for i in list_dic:
#     print(i[0], ':', sep='')
#     for j in sorted(i[1].items()):
#         print(*j)
############################################
########## zad. УДАРЕНИЯ ###################
#
# n = int(input('к-во слов словаря = '))
# dic = []
# dic_l = []
# err = 0
# for i in range(n):
#     ii = input()
#     dic.append(ii)
#     dic_l.append(ii.lower())
# text = input('text : ').split()
# for i in text:
#     if i in dic:
#         continue
#     elif i.lower() in dic_l:
#         err += 1
#     else:
#         count = 0
#         for k in list(i):
#             if k.isupper():
#                 count += 1
#         if count != 1:
#             err += 1
# print(err)
###################################

