print("=========================================")
word_1 = input("Введите секретное слово: ")
word = word_1.casefold()
stroka = "-" * len(word)
n = len(word)
b = 0
while n > 0:
    print("У вас осталось ",n," попытки")
    print("=========================================")
    user_1 = input("Введите букву: ")
    user = user_1.casefold()
    dop = ""
    a = 0
    for i in range(len(word)):
        if user == word[i]:
            dop = dop + user
            a = 1
        else:
            dop = dop + stroka[i]

    if a == 1:
        print("Вы угадали!")
        b += 1
    else:
        n -= 1
    stroka = dop
    print(stroka)

if b == len(word):
    print("Вы выиграли!")
else:
    print("Вы проиграли!")








