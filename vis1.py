remember_word = []
remember_word_a = []
remeber_letter = []


def letter(err):
    while err != False:
        if '_' not in remember_word_a:
            print('<'*5,'𝔅ы 𝔬тг𝔞д𝔞ли 𝔠л𝔬𝔟𝔬!','>'*5)
            break
        l = input('Введите букву - ')
        if len(l) != 1:
            print('Введите одну букву!')
        elif not l.isalpha():
            print('Вы ввели неправильный символ!')
        else:
            check1(l)


def check1(l):
    if l not in remember_word:
        print('='*60)
        print(f'В слове нет буквы "{l}"!')
        print(*remember_word_a)
        if l not in remeber_letter:
            remeber_letter.append(l)
        print('Названные вами буквы - ', *remeber_letter)
        print('=' * 60)
    else:
        check(l)


def check(l):
    ind = 0
    while ind != len(remember_word):
        for ind, item in enumerate(remember_word):
            if item == l:
                remember_word_a[ind] = l
                ind += 1
        else:
            letter_check(l)
        print(*remember_word_a)
        break


def letter_check(l):
    if l not in remeber_letter:
        remeber_letter.append(l)
        print('Названные вами буквы - ', *remeber_letter)
        print('=' * 60)
    elif l in remeber_letter:
        print(f'Вы уже называли букву {l}')
        print('Названные вами буквы - ', *remeber_letter)
        print('=' * 60)


def start():
    full_new = input('Загадайте слово - ')
    for i in full_new:
        remember_word.append(i)
    a = ['_' for i in range(len(full_new))]
    remember_word_a.extend(a)
    print(*remember_word_a)
    err = True
    letter(err)

start()