import json

with open('options.json', 'r') as file:
    quest = json.load(file)

# print(type(quest), quest)


list_questions = list(quest['questions'])
list_questions.sort(key=lambda x: x['id'])

print('lq=', list_questions)
for i in list_questions:
    print(i)
print()
print()
print()



def func(id=1):
    for i in list_questions:
        if i['id'] == id:
            q = i['question']
            a = i['answer']
            end = 0
            if a[0]['next_question'] == False and a[1]['next_question'] == False:
                a = a[0]['text'] + '/' + a[1]['text']
                end = 1
    return [q, a, end]



result = []
res = []

step = func(1)
res.append({step[0]: step[1][0]['text']})

next_step = step[1][0]['next_question']

if next_step:
    step0 = func(next_step)
    res.append({step0[0]: step0[1]})
result.append(res)
# print('res!=', res)
res = []

res.append({step[0]: step[1][1]['text']})
# print('res!=', res)
# print('result!=', result)


next_step = step[1][1]['next_question']
if next_step:
    step0 = func(next_step)
    # print('step:', step0)
    if step0[1][0]['next_question'] == False:
        res.append({step0[0]: step0[1][0]['text']})
        result.append(res)
    res = res[:1]
    if step0[1][1]['next_question'] == False:
        res.append({step0[0]: step0[1][1]['text']})
        result.append(res)
    else:
        next_step = step0[1][1]['next_question']
        if next_step:
            step0 = func(next_step)
            res.append({step0[0]: step0[1]})
            result.append(res)
# print('res=', res)
# print('result=', result)
result_output = {'paths': {'number': len(result), 'list': result}}

with open('answer.json', 'w') as file:
    # json.dump(result_output, file, indent=4)
    json.dump(result_output, file)







    #         if a[0]['next_question']:
    #             res.append([{q, a[0]['text']}, func(a[0]['next_question'])])
    #             return res
    #         elif a[1]['next_question']:
    #             func(a[1]['next_question']):
    #             res.append([{q: a[0]['text']}])
    #
    #             d = {q: a[0]['text'] + '/' + a[1]['text']}
    #             res.append(d)
    #             break
    #         elif a[0]['next_question'] == False:
    #             d = {q: a[0]['text']}
    #             res.append(d)
    #             break
    #         elif a[1]['next_question'] == False:
    #             d = {q: a[1]['text']}
    #             res.append(d)
    #             break
    #         else:
    #             d1 = {q: func(a[0]['next_question'])}
    #             d2 = {q: func(a[1]['next_question'])}
    #             res.append([d1, d2])
    #
    # return res

# print(func())





# def func(id):
#     for i in list_questions:
#         if i['id'] == id:
#             q = q1 = i['question']
#             a = a1 = i['answer']
#     if a[0]['next_question'] == False and a[1]['next_question'] == False:
#         return dict([(q, a[0]['text'] + '/' + a[1]['text'])])
#     elif a[0]['next_question'] == False:
#         return dict([(q, a[0]['text'])]) + func(a[1]['next_question'])
#     elif a[1]['next_question'] == False:
#         return dict([(q1, a1[1]['text']), func(a[0]['next_question'])])
#     else:
#         return dict([(q, a[1]['text']), (q, a[0]['text'])] + func(a[0]['next_question']) + func(a[1]['next_question']))
#


# def func1(id):
#     for i in list_questions:
#         if i['id'] == id:
#             q = i['question']
#             a = i['answer']
#     return [q, a[0]['text'] + '/' + a[1]['text']]
#
#
# def func2(id):
#     for i in list_questions:
#         if i['id'] == id:
#             q = i['question']
#             a = i['answer']
#     for i in 0, 1:
#         if a[i]['next_question'] == False:
#             return [q, a[i]['text']]
#
#
# def func3(id):
#     for i in list_questions:
#         if i['id'] == id:
#             q = i['question']
#             a = i['answer']
#     for i in 0, 1:
#         if a[i]['next_question'] == False:
#             return [q, a[i]['text']]
#         else:
#             res = func1(a[i]['next_question'])
#     return res
#

# result = []
# result.append(func(1))
# print(result)
#


# for i in list_questions:




    # if i['answer'][0]['next_question'] == False and i['answer'][1]['next_question'] == False:
    #     result.append(func1(i['id']))
    #     print(i, result)
    # elif i['answer'][0]['next_question'] == False:
    #     result.append([i['question'], i['answer'][0]['text'], func2(i['answer'][1]['next_question'])])
    #     print(i, result)
    # elif i['answer'][1]['next_question'] == False or i['answer'][1]['next_question'] == False:
    #     result.append([i['question'], i['answer'][0]['text'], func2(i['answer'][0]['next_question'])])
    #     print(i, result)
    # else:
    #     result.append([{i['question']: i['answer'][0]['text']}, func3(i['answer'][0]['next_question'])])
    #     print(i, result)

# print(result)







#             if i['answer'][0]['next_question'] == False and i['answer'][1]['next_question'] == False:
#                 r = dict([(q, i['answer'][0]['text'] + '/' + i['answer'][1]['text'])])
#                 # end1 = 0
#                 # end2 = 0
#                 print('='*80)
#                 print("False-False")
#                 print('r=', r)
#                 res.append([r])
#                 print('res=', res)
#             elif i['answer'][0]['next_question'] == False:
#
#                 r = dict([(q, i['answer'][0]['text'])])
#                 print('=' * 80)
#                 print("False-True")
#                 print('r=', r)
#                 res.append([r])
#                 print('res=', res)
#
#                 # res.append([r])
#                 # end1 = 0
#                 # end2 = 1
#                 # ret1 = [res, end1, end2]
#                 res = func(i['answer'][1]['next_question'])
#                 print('res=', res)
#                 res[-1].append(dict([(q, i['answer'][0]['text'])]))
#                 print('res=', res)
#                 # ret2 = cont
#                 # print('False-True')
#                 # res.append([ret1, ret2])
#                 # return res
#                 # return [ret1, ret2]
#
#             elif i['answer'][1]['next_question'] == False:
#
#                 r = dict([(q, i['answer'][1]['text'])])
#                 print('=' * 80)
#                 print("False-True")
#                 print('r=', r)
#                 res.append([r])
#                 print('res=', res)
#                 res[-1].append(dict([(q, i['answer'][0]['text'])]))
#                 print('res=', res)
#                 # end1 = 0
#                 # end2 = 1
#                 # ret1 = [res, end1, end2]
#                 # res = func(i['answer'][0]['next_question'])
#                 # ret2 = cont
#                 # print('True-False')
#                 # res.append([ret1, ret2])
#                 # return res
#                 # return [ret1, ret2]
#
#             # elif i['answer'][1]['next_question'] == False:
#             #     print('True-False')
#             #     res.append(dict([(q, i['answer'][0]['text'])]))
#             #     result.append(res[0])
#             #     print(res)
#             #     d1 = {}
#             #     d1[q] = i['answer'][0]['text']
#             #     d2 = func(i['answer'][0]['next_question'], result)[0]
#             #     res.append([d1, d2])
#                 # continue
#             else:
#                 # print("True-True")
#                 # r = dict([(q, i['answer'][1]['text'])])
#                 print('=' * 80)
#                 print("True-True")
#                 # print('r=', r)
#                 res.append([(q, i['answer'][0]['text'])])
#                 print('res=', res)
#
#                 res = func(i['answer'][0]['next_question'])
#                 print('res=', res)
#                 res.append([(q, i['answer'][1]['text'])])
#                 res = func(i['answer'][1]['next_question'])
#                 print('res=', res)
#                 # res.append([ret1, ret2])
#                 # print('res t-t ', res)
#                 # return res
#                 # return [ret1, ret2]
#     return res
#
#
# res = []
# r = func(1)
# print(r)



                # for j in range(2):
                #     d1 = {}
                #     d1[q] = i['answer'][j]['text']
                #     res.append(dict([(q, d1[q])]))
                #     print('res2222=', res)
                #     print('result222=', result)
                #     d2 = func(i['answer'][j]['next_question'], res)[0]
                #     # print(d2)
                #     print ('d1=', d1)
                #     print ('d2=', d2)
                #     res.append([d1, d2])
                # print('res=!!! ', res)
    # result += res
    # return result

# pr = func(1)
# print(type(pr), pr)
# for i in pr:
#     print(i)




#
#
# def reverse(res, list_question, id, question='', answer=''):
#     line = []
#     if id:
#         for qst in list_question:
#             if qst['id'] == id:
#                 question = qst['question']
#                 for answ in qst['answer']:
#                     if answ['next_question'] == False:
#                         answer = answ['text']
#                         line.append(dict([(question, answer)]))
#                         reverse(line, list_question, answ['next_question'])
#                     else:
#                         line.append(dict([(question, answer)]))
#                         reverse(res, list_question, answ['next_question'])
#     else:
#         res.append([dict[(question, answer)]])
#     return res
#
#
#
# with open('options.json', 'r') as file:
#     quest = json.load(file)
#
# list_questions = list(quest['questions'])
# list_questions.sort(key=lambda x: x['id'])
# print('lq=', list_questions)
# for i in list_questions:
#     print(i)
#
#
# #
# #
# #
# # mark = 1
# # list_answer = []
# # list_result = []
# #
# # while mark:
# #     mark = 0
# #
# #     for question in list_questions:
# #         if question['answer']:
# #             next_question = question['id']
# #             mark = 1
# #             break
# #
# #     print('next : ', next_question)
# #     while next_question and mark:
# #         print('n=', next_question)
# #
# #         for q in list_questions:
# #             if q['id'] == next_question:
# #                 if q['answer'] and not q['answer'][0]['next_question'] and not q['answer'][1]['next_question']:
# #                     list_answer.append(dict([(q['question'], q['answer'][0]['text'] + '/'+ q['answer'][1]['text'])]))
# #                     next_question = q['answer'][0]['next_question']
# #                     list_result.append(list_answer)
# #                     q['answer'].pop(0)
# #                 else:
# #                     list_answer.append(dict([(q['question'], q['answer'][0]['text'])]))
# #                     next_question = q['answer'][0]['next_question']
# #                     # list_result.append(list_answer)
# #                     q['answer'].pop(0)
# #
# #                 break
# #         print('list_answer :', next_question, list_answer)
# #         list_result.append(list_answer)
# # list_result = list_result[0]
# # num = len(list_result)
# # answer_result = {'paths': {'number': num, 'list': list_result}}
# # print('='*80)
# # print('='*80)
# # print(answer_result)
# #
# res = []
#
# reverse(res, list_questions, 1)
#
# print(res)
# # with open('answer.json', 'w') as file:
# #     json.dump(answer_result, file, indent=4)
#
#
#
#
#
