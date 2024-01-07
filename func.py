def pr(text):
    print('pr :', __name__)
    print(text.upper())
    print('=' * 30)

# pr('Hello')

def pr1(text):
    print('pr1 :', __name__)
    print('Вы только что уcпешно ввели следующий текст:', text)
    print('Длина Вашего текста составляет ', len(text), 'символов')
    print('=' * 30)


def pr3(text):
    print('pr3 :', __name__)
    print('А вот квадрат длины Вашего текста составляет:')
    print(len(text)**2)
    print('='*40)

