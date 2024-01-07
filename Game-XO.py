def screen(area):
    for i in range(3):
        print(area[i][0], area[i][1], area[i][2])
    # return


def check_col(area):
    for i in range(3):
        if len(set(area[i])) == 1 and area[i][1] != b:
            if area[i][1] == x:
                return 1
            else:
                return 2
    return -1


def check_row(area):
    for i in range(3):
        if area[0][i] == area[1][i] == area[2][i] and area[0][i] != b:
            if area[0][i] == x:
                return 1
            else:
                return 2
    return -1


def check_diag(area):
    if area[0][0] == area[1][1] == area[2][2] and area[1][1] != b:
        if area[1][1] == x:
            return 1
        else:
            return 2
    if area[0][2] == area[1][1] == area[2][0] and area[1][1] != b:
        if area[1][1] == x:
            return 1
        else:
            return 2
    return -1


def check_game(area):
    ch = 0
    for i in range(3):
        for j in range(3):
            if area[i][j] == b:
                ch = 1
    if ch == 0:
        return 0
    game = check_col(area)
    if game == -1:
        game = check_row(area)
    if game == -1:
        game = check_diag(area)
    return game


def inp_coord(area):
    global player
    while True:
        screen(area)
        if player == 1:
            print('Ход игрока Крестик !!!!!')
        else:
            print('Ход игрока Нолик !!!!!!')
        step = input('Введите через пробел координаты (например, 1 3) : ')
        if len(step) == 3 and (step[0] == '3' or step[0] == '1'
                               or step[0] == '2') \
                and step[1] == ' ' and (step[2] == '3'
                                        or step[2] == '1' or step[2] == '2'):
            step = step.split()
            step = list(map(lambda x: int(x) - 1, step))
            if area[step[0]][step[1]] == b:
                if player == 1:
                    area[step[0]][step[1]] = x
                else:
                    area[step[0]][step[1]] = o
                player *= -1
            else:
                print('ВНИМАТЕЛЬНЕЕ! Это место уже занято!!!')
                print('Введите другие координаты!!!')
            return area
        else:
            print('Будьте внимательнее! Вы неправильно ввели координаты!!!')
            print('Попробуйте еще раз!!!')


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
        print('     Player КРЕСТИК wins!')
    else:
        print('     Player НОЛИК wins!')
    print('=' * 40)


if __name__ == '__main__':
    player = 1
    b = input('Введите символ, который будет обозначать пустую клетку : ')[0]
    x = input('Введите символ, который будет обозначать крестик Х     : ')[0]
    o = input('Введите символ, который будет обозначать нолик   О     : ')[0]
    game = -1
    area = [
        [b, b, b],
        [b, b, b],
        [b, b, b],
    ]
    # Внутрішня перевірка ===============
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
    # =============================
    run_game(game, area)
