text = list(input('Input text : '))
attempt = len(text)
n = 60
pole = "*" * len(text)
print(pole)

while attempt:
    symbol = input('Input symbol: ')
    attempt -= 1
    if text.count(symbol):
        print('\n' * 3, '!' * n)
        print('Great!!!'.center(n, ' '))
        print(('The symbol "' + symbol + '" is in the text !').center(n, ' '))
        print('!' * n)
        attempt +=1
        #for num in range(len(text)):
            #if symbol==text[num]:
                #dop=dop+symbol
            #else:
                #dop=dop+pole[num]
        print(pole)
        print()
    else:#################################
        print(('No symbol "'+ symbol + '" is in the text !').center(n, ' '))
        print('Try again! You have ', attempt, 'attempts.')
else:  #####################
    print('=' * n)  ##################
    print("Sorry, you don't have any attempts...") ##############
    print('='*n) ##############3
    
    
while "*" in pole:
    #user=input("Угадайте букву ")
    user = symbol ###################
    dop = "" ######################## what's  dop ?????
    dop += user #######################################
    for num in range(len(text)):
        if user == text[num]:
            # dop = dop + user #############
            pole[num] = user #################3
        # else: #########################
        #     dop = dop + pole[num] ###########??????
    # pole = dop ####################
    print(pole)


print('You win !!!!!!!!!!!') ######################
