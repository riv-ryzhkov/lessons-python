def screen(area):
    # Виводить на екран ігрове поле
    pass


def check_columns(area):
    #  Перевіряє колонки і повертає результат перевірки:
    #  продовжуємо   -1
    #  гравець  1
    #  гравець  2
    pass


def check_rows(area):
    #  Перевіряє рядки і повертає результат перевірки:
    #  продовжуємо   -1
    #  гравець  1
    #  гравець  2
    pass


def check_diag(area):
    #  Перевіряє діагоналі і повертає результат перевірки:
    #  продовжуємо   -1
    #  гравець  1
    #  гравець  2
    pass


def check_game(area):
    #  Перевіряє всю гру (кол/рядки/діагоналі) і повертає результат перевірки:
    #  продовжуємо                  -1
    #  гравець  Х                    1
    #  гравець  О                    2
    #  закінчились порожні клітинки  0
    pass


def inp_coord(area):
    # input('Введіть через пробіл координати (наприклад, 1 3) : ')
    # Валідація:
    # - ввели "цифру пробіл цифру" (3 символа, з яких другий - пробіл)
    # - ввели цифри від 1 до 3
    # - місце зайняте

    # якщо все гаразд, змінити Ігрове поле і передати хід іншому гравцю
    pass


def run_game(game, area):
    while game == -1:
        area = inp_coord(area)
        game = check_game(area)
    screen(area)
    print('=' * 40)
    print('           GAME OVER')
    if game == 0:
        print('         DRAW!!!')
    elif game == 1:
        print('     Player XРЕСТИК wins!')
    else:
        print('     Player НОЛИК wins!')
    print('=' * 40)


if __name__ == '__main__':
    player = 1  # Маркер гравця
    b = input('Введіть символ, що буде позначати пусту клітинку : ')[0]
    x = input('Введіть символ, що буде позначати хрестик  Х     : ')[0]
    o = input('Введіть символ, що буде позначати нолик    О     : ')[0]
    game = -1  # Маркер стану гри
    area = [
        [b, b, b],
        [b, b, b],
        [b, b, b],
    ]  # Ігрове поле

    # Внутрішня перевірка за допомогою assert
    assert check_game([
        [b, b, b],
        [b, b, b],
        [b, b, b],
    ]) == -1

    assert check_game([
        [b, x, b],
        [b, x, o],
        [b, x, o],
    ]) == 1

    assert check_game([
        [b, b, b],
        [x, x, x],
        [b, o, o],
    ]) == 1

    assert check_game([
        [o, b, b],
        [x, o, b],
        [x, x, o],
    ]) == 2

    assert check_game([
        [x, x, o],
        [o, o, x],
        [x, x, o],
    ]) == 0

    assert check_game([
        [b, o, b],
        [x, b, b],
        [b, b, b],
    ]) == -1

    run_game(game, area)

