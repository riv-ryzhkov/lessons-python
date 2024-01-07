import json

with open('options.json', 'r') as file:
    quest = json.load(file)

list_questions = list(quest['questions'])
list_questions.sort(key=lambda x: x['id'])
print('lq=', list_questions)
for i in list_questions:
    print(i)





mark = 1
list_answer = []
list_result = []

while mark:
    mark = 0

    for question in list_questions:
        if question['answer']:
            next_question = question['id']
            mark = 1
            break

    print('next : ', next_question)
    while next_question and mark:
        print('n=', next_question)

        for q in list_questions:
            if q['id'] == next_question:
                if q['answer'] and not q['answer'][0]['next_question']:
                    list_answer.append(dict([(q['question'], q['answer'][0]['text'])]))
                    next_question = q['answer'][0]['next_question']
                    list_result.append(list_answer)
                    q['answer'].pop(0)
                else:
                    list_answer.append(dict([(q['question'], q['answer'][0]['text'])]))
                    next_question = q['answer'][0]['next_question']
                    # list_result.append(list_answer)
                    q['answer'].pop(0)

                break
        print('list_answer :', next_question, list_answer)
        list_result.append(list_answer)
list_result = list_result[0]
num = len(list_result)
answer_result = {'paths': {'number': num, 'list': list_result}}
print('='*80)
print('='*80)
print(answer_result)

with open('answer.json', 'w') as file:
    json.dump(answer_result, file, indent=4)





