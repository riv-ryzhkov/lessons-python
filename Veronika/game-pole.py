import random
import faker


def inp_secret_world():
    fake = faker.Faker(locale="ru_RU")
    # text = ['телефон', 'перемога', 'баскетбол', 'кішка', 'університет','школа','мама','віконце','ліжко','танці','ковзанка','шкарпетки','оселя','диван','люстерко']
    # secr_word = random.choice(text)
    secr_word = fake.word()
    # print(secr_word)
    return secr_word


def cals_attempts(secret_word: list):
    # Calculation of attempts
    attempts = len(secret_word)
    return attempts


def write_word(secret_word, symbol, word, attempts):
    mark = 0
    for i in range(len(secret_word)):
        if symbol == secret_word[i]:
            word[i] = symbol
            mark = 1
    if mark == 0:
     #   print('no!', attempts)
        attempts -= 1
     #   print('-----', attempts)
    return attempts


def screen(word: list, lst_letters: list, attempts: int):
    print('=' * 80)
    print(*word)
    print('У вас залишилось ', attempts, 'спроб')
    print('ви вже використали наступні літери:', *lst_letters)
    print('=' * 80)


def inp_symbol(lst_letters):
    symbol = input('Введіть одну літеру :').lower()
    while len(symbol) != 1 or not symbol.isalpha() or symbol in lst_letters:
        if len(symbol) != 1:
            print('Помилка! введіть саме ОДНУ літеру!')
        elif not symbol.isalpha():
            print('Помилка! Можнв вводити лише ЛІТЕРИ!')
        else:
            print('Помилка! Можнв вводити лише ЛІТЕРИ!')
        symbol = input('Введіть одну літеру :').lower()
    lst_letters.append(symbol)
    return symbol


# func(screen(word, lst_letters, attempts))

def game():
    print('*' * 80)
    print('                          Добро пожаловать в игру "Поле чудес"!')
    print('*' * 80)
    task = input('Press <ENTER>')
    secret_word = inp_secret_world()
    # print(secret_word)
    attempts = cals_attempts(secret_word)
    # print(attempts)
    word = list("_" * attempts)
    lst_letters = []
    while attempts and "_" in word:
        screen(word, lst_letters, attempts)
        symbol = inp_symbol(lst_letters)
        attempts = write_word(secret_word, symbol, word, attempts)
     #   print('m1', attempts)
    if attempts:
        print('WIN!!!!!!!')

    else:
        print('GAME OVER!!!!')






if __name__ == '__main__':
    game()


# game1.py
# Відображається "game1.py".