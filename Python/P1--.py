def goto(linenum):
    global line
    line = linenum
line=1
print (678)
print ("Yes!!!!!")
r = 5
t = 23
print (r+t)
C = "Y"
while C == "Y":
    A = input ("1st digit")
    B = input ("2nd digit")
    Znak = input ("+-  :")
    if Znak == "+":
        print (A+B)
    elif Znak == "-":
        print (A-B)

    else:
        print (":-(")
    C = input ("Y/N? :")
    if C == "Y": goto(1)
    
    else:
        print
        print ("Thanks!")
    input
