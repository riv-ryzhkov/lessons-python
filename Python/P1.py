def goto(linenum):
    global line
    line = linenum
line=1
print (678)
print ("Yes!!!!!")
r = 5
t = 23
print (r+t)
C = "Да"
while C == "Да":
    A = input ("Введите число:")
    B = input ("Введите второе число:")
    Znak = input ("Введите знак + или -  :")
    if Znak == "+":
        print (float(A)+float(B))
    elif Znak == "-":
        print (float(A)-float(B))

    else:
        print ("Неправильный знак")
    C = input ("Еще? (Да/Нет)  :")
    if C == "Да": goto(1)
    
    else:
        print
        print ("Спасибо за работу!")
    input
