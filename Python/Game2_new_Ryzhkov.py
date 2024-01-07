
PLAYER = 1
B = input('Введите символ, который будет обозначать пустую клетку : ')[0]
X = input('Введите символ, который будет обозначать крестик Х     : ')[0]
O = input('Введите символ, который будет обозначать нолик   О     : ')[0]
GAME = -1
area = [
    [B, B, B],
    [B, B, B],
    [B, B, B],
]

def screen(area):
    for i in range(3):
        print(area[i][0], area[i][1], area[i][2])
    return

def check_line(area):
   for i in range(3):
       if len(set(area[i])) == 1 and area[i][1] != B:
           if area[i][1] == X:
               return 1
           else:
               return 2
   return -1

def check_row(area):
    for i in range(3):
       if area[0][i] == area[1][i] == area[2][i] and area[0][i] != B:
           if area[0][i] == X:
               return 1
           else:
               return 2
    return -1


def check_diag(area):
    if area[0][0] == area[1][1] == area[2][2] and area[1][1] != B:
        if area[1][1] == X:
            return 1
        else:
            return 2
    if area[0][2] == area[1][1] == area[2][0] and area[1][1] != B:
        if area[1][1] == X:
            return 1
        else:
            return 2
    return -1


def check_game(area):
    ch = 0
    for i in range(3):
        for j in range(3):
            if area[i][j] == B:
                ch = 1
    if ch == 0:
        return 0
    GAME = check_line(area)
    if GAME == -1:
        GAME = check_row(area)
    if GAME == -1:
        GAME = check_diag(area)
    return GAME



def inpt(area):
    global PLAYER
    while True:
        screen(area)
        if PLAYER == 1:
            print('Ход игрока Крестик !!!!!')
        else:
            print('Ход игрока Нолик !!!!!!')
        step = input('Введите через пробел координаты : ')
        if len(step) == 3 and (step[0] == '0' or step[0] == '1' or step[0] == '2') and step[1] == ' ' \
            and (step[2] == '0' or step[2] == '1' or step[2] == '2'):
            step = step.split()
            step = list(map(int, step))
            if area[step[0]][step[1]] == B:
                if PLAYER == 1:
                    area[step[0]][step[1]] = X
                else:
                    area[step[0]][step[1]] = O
                PLAYER *= -1
            else:
                print('ВНИМАТЕЛЬНЕЕ! Это место уже занято!!!')
                print('Введите другие координаты!!!')
            return area
        else:
            print('Будьте внимательнее! Вы неправильно ввели координаты!!!')
            print('Попробуйте еще раз!!!')


while GAME == -1:
    area = inpt(area)
    GAME = check_game(area)
screen(area)
print('===============================')
print('           GAME OVER')
if GAME == 0:
    print('         DRAW!!!')
elif GAME == 1:
    print('     Player КРЕСТИК wins!')
else:
    print('     Player НОЛИК wins!')
print('================================')


assert check_game([
    [B, B, B],
    [B, B, B],
    [B, B, B],
]) == -1
assert check_game([
    [B, X, B],
    [B, X, O],
    [B, X, O],
]) == 1
assert check_game([
    [B, B, B],
    [X, X, X],
    [B, O, O],
]) == 1
assert check_game([
    [O, B, B],
    [X, O, B],
    [X, X, O],
]) == 2
assert check_game([
    [X, X, O],
    [O, O, X],
    [X, X, O],
]) == 0
assert check_game([
    [B, O, B],
    [X, B, B],
    [B, B, B],
]) == -1