words = ['БАЙРАКТАР', 'ДЖАВЕЛІН', 'ОКУПАНТ', 'ЗСУ', 'ГЕРОЙ', 'ПРЕЗИДЕНТ', 'ПРИВИД', 'ЧОРНОБАЇВКА', 'ПЕРЕМОГА', 'УКРАЇНА', 'КРЕЙСЕР', 'СИРЕНА']

import random

vykoristani = list()
secret_word = list(random.choice(words))
kil_sprob = len(secret_word)
pole_igry = list('_' * kil_sprob)

def printing() :
    print('=' * 100)
    print(*pole_igry)
    print('=' * 100)
    print('Ви використали такі літери: ', end='')
    print(*vykoristani, sep=', ')
    print('У вас залишилось', kil_sprob, 'спроб')
    print('=' * 100)
printing()

def sproba():
    global kil_sprob
    global vykoristani
    kil_sprob -= 1
    vykoristani.append(letter.upper())

def right_answer():
    indeks = secret_word.index(letter.upper())
    pole_igry[indeks] = letter.upper()
    return indeks

while kil_sprob != 0 and pole_igry.count('_') != 0: #гра триватиме, поки не закінчаться спроби або поки не буде вгадано слово
    letter = input('Введіть літеру: ')
    if len(letter) == 1 and letter.isalpha(): #перевірка на правильність формату введеної строки
        if secret_word.count(letter.upper()) == 1: #якщо літера трапляється у слові 1 раз
            sproba()
            right_answer()
            print('ВІТАЮ! ВИ ВГАДАЛИ ЛІТЕРУ!')
            printing()
        elif not letter.upper() in secret_word :
            sproba()
            print('ТАКОЇ ЛІТЕРИ У СЛОВІ НЕМА! СПРОБУЙТЕ ЩЕ РАЗ')
            printing()
        elif secret_word.count(letter.upper()) > 1: #якщо літера трапляється у слові декілька раз
            for i in secret_word:
                if letter.upper() == i:
                    right_answer()
                    secret_word[right_answer()] = '*' #замінюємо одну з літер у слові на *, аби перейти до наступної
            print('ВІТАЮ! ВИ ВГАДАЛИ ЛІТЕРУ!')
            sproba()
            printing()
    else:
        print('Неправильний формат! Будь ласка, введіть одну літеру')
        continue

if '_' in pole_igry and kil_sprob == 0:
    print('На жаль, ви програли. Спробуєте ще раз? ')
elif not '_' in pole_igry:
    print('УРА! ПЕРЕМОГА!')

