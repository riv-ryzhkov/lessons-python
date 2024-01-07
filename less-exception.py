# print('567' + 123)
# print(10/0)




# try:
#     for i in range(0, 5):
#         print(3/i)
# except (ZeroDivisionError, KeyError):
# # except TypeError:
# # except:
#     print("Деление на 0")
#     print("Исключение было обработано")
# else:
#     print('Hello! OK!')





# for i in range(0, 5):
#     try:
#         print(3/i)
#     except ZeroDivisionError:
#         print("Деление на 0")
#         print("Исключение было обработано")
#     else:
#         print('Hello! OK!')



#################
# a, b = 1, 0
# try:
#     print(a/b)
#     print("Это не будет напечатано")
#     print('10'+10)
# except TypeError:
#     print('10' + '10')
#     print("Вы сложили значения несовместимых типов")
# except ZeroDivisionError:
#     print("Деление на 0")
# except:
#     print('Xa!!!!!!')




##########################
# a, b = 1, 0
# try:
#    print(a/b)
# except ZeroDivisionError:
#    print("Вы не можете разделить на 0")
#
# print("Будет ли это напечатано?")



# #######################
# try:
#     # print('10'+10)
#     # print(1/0)
#     print(a)
# except (TypeError, ZeroDivisionError):
#     print("Неверный ввод")



# ####################
# try:
#     # print('1'+1)
#     # print(sum1)
#     print(1/0)
# except NameError:
#     print("sum1 не существует")
# except ZeroDivisionError:
#     print("Вы не можете разделить на 0")
# except:
#     print("Что-то пошло не так...")




# #####################
# try:
#     a = int(input('a = '))
#     if a == 0:
#         raise ValueError
#     else:
#         print(1 / a)
# except (KeyError, TypeError, ValueError):
#     print("Исключение поймано")
# finally:
#     print("Хорошо")
# print("Пока")




# ########################
# try:
#     print(1/5)
# # except (ValueError, ZeroDivisionError):
# except ZeroDivisionError:
#     print("Это ошибка значения")
# else:
#     print('Будет ли напечатан этот текст?')
# finally:
#     print("Это будет напечатано в любом случае.")




# ###################
# try:
#     print(1/0)
# except ZeroDivisionError:
#     print('1/0')
# finally:
#     print("Ничего не происходит")





# #####################
# raise ZeroDivisionError('WAW!!!')
# raise KeyError('XA!XA!XA!!!!')
# raise NameError('Слава Украине!!!!')


# #####################
# a, b = int(input()), int(input())  # вводим 1 затем 0
# a, b = 1, 0  # вводим 1 затем 0
# if b == 0:
#     raise ZeroDivisionError('b = 0 !!!!!!!!!!')
# c = a / b


###########################
# # a, b = int(input()), int(input())
# a, b = 1, 0
# try:
#     if b == 0:
#         raise ZeroDivisionError
# except:
#    print("Деление на 0")
# else:
#     print("Будет ли это напечатано?")

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


# #####################
# try:
#     # print(10/0)
#     print('1' + 1)
#     print()
# except:
#     raise KeyError('Ha-Ha-Ha!!!!')


# ###########
# raise ValueError("Несоответствующее значение")
# ######################




################################################################
# assert 2 + 2 == 5, "Ви маєте помилку в алгоритмі!"
################################################################
#
# number = ''
# while not number:
#     try:
#         symbol = input('Введіть номер вашої картки без пробілів : ')
#         assert symbol.isdigit(), 'Ви зробили помилку! Повинні бути лише ЦИФРИ!'
#         assert len(symbol) > 15, 'Ви зробили помилку! Занадто КОРОТКИЙ номер!'
#         assert len(symbol) < 17, 'Ви зробили помилку! Цифр більше 16!'
#         number = symbol
#     except AssertionError as err:
#         print(err)
# print('\nДобре! Номер вашої картки :',
#       number[:4],
#       number[4:8],
#       number[8:12],
#       number[12:])



#
# def foo(*args):
#     if args:
#         return 'Yes'
#     else:
#         return 'No'
#
#
# assert(foo(5, 7, 9, -34) == 'Yes')
# assert (2 + 2 == 4), 'Неужели?!!!!!!!!!!'
# assert(foo(-5) == 'Yes')
# assert(foo() == 'No'), 'Assert Error'
# assert(foo(8) == 'Yes'), 'Assert Error'
#
# print('ok!!!!!!!!!!!')





# # ###################################
# try:
#     print(1)
#     assert 2 + 2 == 4
#     print(2)
#     assert 1 + 2 == 4, "It's impossible!"
#     print(3)
# except:
#     print("assert False.")
#     raise
# finally:
#     print("Хорошо")
# print("Пока")




# ############################
# assert False, "Это проблема"
# #############################
#






########################################################################
####################################
# Exception with file
####################################

# try:
#     f = open("newfile.txt", 'w')
#     text = input('text = ')
#     if len(text) > 5:
#         raise ValueError
#     f.write(text)
# except:
#     print('Error of the INPUT!!!')
#     print("Length of the text must be les than 5 symbols!")
#     print("Text can not be added!")
# else:
#     print("Nothing went wrong")
# finally:
#     f.close()
#     print("The 'try except' is finished")






############################
# class MyError(Exception):
#     # def __init__(self, data):
#     #     self.data = data
#     #
#     # def __str__(self):
#     #     return repr(self.data)
#     pass
#
#
# try:
#     f = open("newfile.txt", 'w')
#     text = input('text = ')
#     if len(text) > 5:
#         raise MyError("Text must be less than 5 symbols!")
#     f.write(text)
# except MyError as err:
#     print('INPUT Error!!!!!!!!')
#     print(err)
#     # print(err.data)
# else:
#     print("Nothing went wrong")
# finally:
#     f.close()
#     print("The file is closed.")
#     print("The 'try except' is finished")


