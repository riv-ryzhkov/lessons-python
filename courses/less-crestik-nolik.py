def display(space):
    for i in range(3):
        print(*space[i])

def valid(s):
    if len(s) != 3 or s[1] != " " or not s[0].isdigit() or not s[2].isdigit():
        display(space)
        print('=' * 80)
        print('Ви ввели некорректні координати! Спробуйте ще раз.')
        return False
    a = int(s[0])
    b = int(s[2])
    if a < 1 or a > 3 or b < 1 or b > 3:
        display(space)
        print('=' * 80)
        print('Такого рядка чи стовбца не існує! Введіть числа від 1 до 3')
        return False
    if space[a-1][b-1] != '.':
        display(space)
        print('=' * 80)
        print('Це місце вже зайнято! Оберіть іншу клітинку!')
        return False
    return True

def step(space, pl) -> object:
    while True:
        print('=' * 80)
        s = input('Введіть координати Вашого ходу через пробіл (рядок стовбець) : ')
        if valid(s):
            s = s.split()
        else:
            continue
        if pl == 1:
            space[int(s[0])-1][int(s[1])-1] = 'x'
        else:
            space[int(s[0])-1][int(s[1])-1] = '0'
        return space

def check(l):
    for k in ['x', '0']:
        for i in range(3):
            if l[i][0] == l[i][1] == l[i][2] == k or l[0][i] == l[1][i] == l[2][i] == k:
                return True
        if l[0][0] == l[1][1] == l[2][2] == k or l[0][2] == l[1][1] == l[2][0] == k:
            return True
    return False


space = []
for i in range(3):
    space.append(['.', '.', '.'])
pl = -1
vin = False
while vin == False:
    sum = 0
    for i in range(3):
        sum += space[i].count('.')
    if sum == 0:
        pl = 0
    if check(space) or pl == 0:
        vin = True
        break
    pl *= -1
    display(space)
    if pl == 1:
        print('Черга 1-го гравця ("х")')
    else:
        print('Черга 2-го гравця ("0")')
    step(space, pl)

print('=' * 40)
if pl == 1:
    print('Перемога 1-го гравця ("х")')
elif pl == 0:
    print('Мої вітання! Бойова нічия!')
else:
    print('Перемога 2-го гравця ("нолик")')
print('=' * 40)
display(space)

