choic = 'O'


def check_win(board):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if board[each[0] + 1] == board[each[1] + 1] == board[each[2] + 1]:
            return board[each[0] + 1]
    return None


diction = {'X': True, 'O': False}

xo_list = {
    1: '1',
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    6: '6',
    7: '7',
    8: '8',
    9: '9'
}


def check_finish(xo_list):
    global diction
    check_info = {}
    for val in xo_list:
        if xo_list[val] in diction:
            check_info[val] = diction[xo_list[val]]
        else:
            check_info[val] = None

    if None not in check_info.values():
        return None

    return check_info


def cycle(xo_list):
    print('-' * 13)
    for i in range(3):
        print(f'| {xo_list[1 + i * 3]} | {xo_list[2 + i * 3]} | {xo_list[3 + i * 3]} |')
        print('-' * 13)


def choice():
    global choic
    if choic == 'X':
        choic = 'O'
        return choic
    choic = 'X'
    return choic


print(f"Зараз ходить '{choice()}'")
cycle(xo_list)
while True:
    value = input()
    try:
        value = int(value)
    except:
        print(f"'{value}' не є числом")

    try:
        int(xo_list[value])
    except:
        try:
            print('ПОПЕРЕДЖЕННЯ')
            print(f"На точці '{value}' вже є '{xo_list[value]}'")
            input('enter для продовження:\n')
            print(f"Зараз ходить '{choic}'")
            cycle(xo_list)
            continue
        except:
            print(f"'{value}' має бути числом від 1 до 9")
            print(f"Зараз ходить '{choic}'")
            cycle(xo_list)
            continue
    xo_list[value] = choic
    if check_finish(xo_list) == None:
        print('НИЧІЯ')
        cycle(xo_list)
        break

    spisok = check_finish(xo_list)
    if check_win(spisok) == None:
        pass
    else:
        winner = 'O'
        if check_win(spisok):
            winner = 'X'

        print(f"Виграв '{winner}'")
        cycle(xo_list)
        break
    print(f"Зараз ходить '{choice()}'")
    cycle(xo_list)
