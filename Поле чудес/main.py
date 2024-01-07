# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


questions = [{'question': 'Что использовали в Китае для глажки белья вместо утюга?',
              'answer': 'СКОВОРОДА'},
             {'question': 'Самое теплое время года?',
              'answer': 'ЛЕТО'}]
q = int(input('Введите номер вопроса: '))
d = {}
b = {}
x = []
s = ''
i = 0

d = questions[q - 1]
answer = d['answer']

print('Вопрос:', d['question'])
print('Ответ:', 'x' * len(answer))

x = ['x'] * len(answer)
print(''.join(x))
while True:
    symbol = input('Введите букву: ').upper()
    for i in range(len(answer)):
        if answer[i] == symbol:
            x[i] = symbol
    s = ''.join(x)
    print(s)
    if s == answer:
        break
