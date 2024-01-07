import random


n = 21 # Кількість білетів
used = []
lst = [i for i in range(n+1)]
for i in range(n):
    print('Використано наступні білети:')
    print(*used)
    ticket = lst.pop(random.randint(1, len(lst)-1))
    used.append(ticket)
    print('='*80, '\nВаш білет номер = ', ticket, ' !\n', sep='')
    print('Залишились наступні білети:')
    print(*lst[1:])
    print('='*80)
    r = input('Press any key')



