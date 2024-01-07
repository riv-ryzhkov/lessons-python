# text = '''
# Президент УЄФА Александер Чеферін після свого переобрання на пост президента організації заявив, що росії зараз не варто чекати повернення у великий футбол.
# Чеферін сумнівається, що російські клуби найближчим часом матимуть змогу брати участь у єврокубках, а збірні – в офіційних матчах.
# «Моя особиста думка: доки війна не завершиться, буде дуже складно змінити щось у санкціях. Поки триває війна, триває це божевілля, треба зберігати таку форму тиску», – сказав Чеферін.
# Раніше повідомлялося, що росія готова перейти в Азіатську конфедерацію футболу, щоб брати участь у відборі до ЧС-2026.
# '''
#
# print(text)
# print('='*80)
#
# t = []
# for i in text:
#     if i.isalpha() or i == ' ':
#         t.append(i)
# text = ''.join(t)
#
#
# print(text)
# print('='*80)
#
#
# text = list(set(text.upper().split()))
# print(text)
# print('='*80)







import random
# from list_of_words import word



def inp_secret_word():
    text = ['СОБАКА', 'КІШКА', 'УКРАЇНА', 'УНІВЕРСИТЕТ', 'ДНІПРО', 'ПЕРЕМОГА']
    # text = [
    #         'ВІЙНА',
    #         'ВІДБОР',
    #         'ТИСК',
    #         'ОСОБА',
    #         'У', 'ФУТБОЛУ', 'ВАРТО', 'ЗАЯВИВ', 'ЦЕ', 'ОРГАНІЗАЦІЇ', 'ПОВІДОМЛЯЛОСЯ', 'АЛЕКСАНДЕР', 'ЗБІРНІ', 'УЄФА', 'ПОВЕРНЕННЯ', 'ЧЕКАТИ', 'ПРЕЗИДЕНТ', 'ПОКИ', 'МАТИМУТЬ', 'ТАКУ', 'ПЕРЕОБРАННЯ', 'КОНФЕДЕРАЦІЮ', 'ПЕРЕЙТИ', 'ЗАВЕРШИТЬСЯ', 'ОФІЦІЙНИХ', 'АЗІАТСЬКУ', 'ФУТБОЛЧЕФЕРІН', 'ЧАСОМ', 'САНКЦІЯХ', 'ДУЖЕ', 'НАЙБЛИЖЧИМ', 'БРАТИ', 'ЩОСЬ', 'В', 'ДУМКА', 'ПРЕЗИДЕНТА', 'СКЛАДНО', 'ЩО', 'УЧАСТЬ', 'БОЖЕВІЛЛЯ', 'РОСІЯ', 'ЧС', 'ФОРМУ', 'ЗАРАЗ', 'НА', 'СВОГО', 'ПІСЛЯ', 'ПОСТ', 'МАТЧАХМОЯ', 'КЛУБИ', 'ЧЕФЕРІНРАНІШЕ', 'НЕ', 'ТРЕБА', 'ГОТОВА', 'ЧЕФЕРІН', 'РОСІЙСЬКІ', 'ЗМОГУ', 'СУМНІВАЄТЬСЯ', 'ЗБЕРІГАТИ', 'СКАЗАВ', 'ВЕЛИКИЙ', 'ТРИВАЄ', 'БУДЕ']
    secret_word = random.choice(text)
    # Validation or choose from list
    # secret_word = input('Введите секретное слово : ').upper()
    return secret_word





def calc_attempts(secret_word):
    attempts = len(secret_word)
    return attempts





def write_word(secret_word, symbol, word):
    for i in range(len(secret_word)):
        if symbol == secret_word[i]:
            word[i] = symbol
    pass
    # в__о__кн__е
#


def screen(word, lst_letters, attempts):
    print()
    print()
    print(*word)
    print('У Вас залишилось ', attempts, 'спроб.')
    print('Ви вже використали наступні літери :', *lst_letters)
#


def inp_symbol():
    symbol = input('Введіть одну букву : ')
    # Validation

    return symbol
#
#


def check_game(word, attempts):
    pass
    # if .... :
    #     result = '....'
    # return result
#
#




def run_game():

    secret_word = inp_secret_word()
    attempts = calc_attempts(secret_word)
    my_symb = '_'
    word = list(my_symb * attempts)  #  ['_', '_', '_', '_', '_', '_', '_', '_']
    while my_symb in word and attempts:
        symbol = inp_symbol()
        write_word()

    if my_symb in word:
        print('Game over')
    else:
        print('Win')



if __name__ == '__main__':
    run_game()