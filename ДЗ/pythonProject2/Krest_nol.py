
pole_igry = [['.'] * 3 for i in range(3)] #створюємо поле для гри

print('=' * 20, "Гра Хрестики-нулики", '=' * 20, end='\n')
print("Перший гравець грає за 'X'", "Другий гравець грає за 'O'", 'ХАЙ ЩАСТИТЬ!', sep='\n', end='\n')

def print_game(x):
    for i in range(len(x)):
        for j in range(len(x[i])):
            print(x[i][j], end='\t')
        print()

def game(x, а): # х - елемент, яким буде заповнена комірка, а - текст в input
    try:
        riadok, stovb = list(map(int, input(а).split()))
        if pole_igry[riadok - 1][stovb - 1] == '.':
            pole_igry[riadok - 1][stovb - 1] = x
        else:
            print('Ця комірка вже зайнята! ')
            game(x, 'Спробуйте ще раз: ')
    except ValueError:
        print('Неправильний формат!')
        game(x, 'Спробуйте ще раз: ')


def check_win(x: list):
    for i in range(3):
        if x[i][0] == x[i][1] == x[i][2] != '.': #заповнений рядок
            return x[i][0]
        if x[0][i] == x[1][i] == x[2][i] != '.': #заповнений стовбчик
            return x[0][i]
        if x[0][0] == x[1][1] == x[2][2] != '.' or x[0][2] == x[1][1] == x[2][0] != '.': #заповнена діагональ
            return x[1][1]
    return 0

def run_game(a):
    i = 0 #рахуємо ходи гравців
    win_check = False
    while not win_check:
        i += 1
        if i % 2:
            game('x', "Оберіть комірку для 'x': ")
        else:
            game('о', "Оберіть комірку для 'o': ")
        print_game(a)
        if i >= 5:
            check = check_win(a)
            if check:
                print('Вітаю! Перемога за гравцем:', "'", check, "'")
                win_check = True
                break
        if i == 9:
            print('Нічия!')
            break
print_game(pole_igry)
run_game(pole_igry)




#






