# import math
# from math import sin, cos
# from math import *
# from math import sin as my_sin_function


# print(my_sin_function(54))

# print(*dir(math), sep='\n')
# print(len(dir(math)), sep='\n')
# print(math.sin(23))

# print(sin(34))
# print(cos(34))
# print(tan(34))










# import json
# #####################    Module   Time  ########################
#
# import time


# print(dir(time))

# print(*dir(time), sep='\n')


#
# print('sec from 1-01-1970 :', time.time()) ###### секунды с 1.01.1970
#
# print('now :', time.ctime())
#
# t = 3  # seconds
# print("\nProgram started...")
# time.sleep(t)
# print(str(t) + " seconds passed.\n")
# result = 0
# for i in range(1, t+1):
#     start = time.time()   #### может сбоить в случае внешнего влияния на настройки системного времени
#     time.sleep(t)
#     finish = time.time()
#     result += finish - start
#     print("Program time(time.time): " + str(result) + " seconds.\n")
#


# start = time.monotonic() ### не зависит от возможных попыток изменить системное время
# time.sleep(t)
# result = time.monotonic() - start
# print("Program time(monotonic): {}".format(result) + " seconds.\n")
# ...................................

# time_ = time.strftime("%A %B %d, %Y", time.localtime())
# time_ = time.strftime("%A - %d %B %Y year", time.localtime())
#
# time_pr = f"Today is {time_}.\n"
#
# print('time.strftime :', time_pr)
#
# # print('time.localtime :', time.localtime())
#
# print('time.mktime :', time.mktime(time.localtime()))
# print('time.timezone :', time.timezone)


############## Модуль DateTime ########################
import datetime

# print(*dir(datetime.datetime), sep='\n')

# ....................................

# a = datetime.date(2021, 2, 23)
# print('a :', a, type(a))

# ....................................


# a = datetime.date.today()
# print('a today :', a)

# ....................................


# a = datetime.date(2021, 5, 29)
# # print(type(a), a)
# print(*dir(a), sep='\n')
#
#
# # ....................................
# print('year :', a.year)
# print('month :', a.month)
# print('day :', a.day)
# print('birth_day :', a.weekday())
#

# ....................................
# a = datetime.time(9, 15, 45, 345)
# print('time :', a, type(a))
#
# ....................................
# a = datetime.time(23, 7, 45)
# b = datetime.time(9, 33)
# c = datetime.time(14)
# print('time :', a)
# print('time :', b)
# print('time :', c)
#
# ....................................

# a = datetime.time(12, 31, 29, 1234)
# print('time :', a)
# print('hour :', a.hour)
# print('minute :', a.minute)
# print('seconds :', a.second)
# print('microsecond :', a.microsecond)
#

# ....................................
# a = datetime.datetime.today()
# b = datetime.datetime.now()  # faster!!!!!
# print('a(today) :', a)
# print('now :', b)

# ....................................

# a = datetime.datetime.today().strftime("%a.%d.%m.%Y")
# b = datetime.datetime.now().strftime("%A %D %M %Y: %H:%M:%S")
# print('today().strftime', a)
# print('today().strftime', b)
#
#
# ....................................
# a = datetime.datetime.now()
# print('year :', a.year)
# print('month :', a.month)
# print('day :', a.day)
# print('hour :', a.hour)
# print('minute :', a.minute)
# print('second :', a.second)
# print('microsecond :', a.microsecond)
#
# print(datetime.datetime.now().year)
# ....................................
# a = datetime.date(2019, 4, 22)
# b = datetime.time(22, 15, 30)
# c = datetime.datetime.combine(a, b)
# print('combine :', c)

#########################################################
############## DateTime.DateTime ########################
# from datetime import datetime
#
#
# a = datetime.now()
# b = datetime(2006, 7, 14)
# c = a - b
# print(type(a), a)
# print(type(b), b)
# print(type(c), c)
# d = b + c
# print(type(d), d)


# ............................

# print('days :', c.days, type(c.days))
# print('seconds :', c.seconds, type(c.seconds))
# print('microseconds :', c.microseconds, type(c.microseconds))

# # ............................
#
# print('a :', a, type(a))
# r = str(a)
# print('r :', r, type(r))
# print(r[8:10])


############## DateTime.timedelta ########################
#
# from datetime import timedelta
#
# # a = timedelta(days=7, hours=2, minutes=23, seconds=22)
# a = timedelta(days=2)
# print(a, type(a))
# b = datetime.datetime.now() + a
# print(b)

# ################################
#
# from datetime import datetime, timedelta
#
# a = datetime(2021, 10, 9)
# n = datetime.now()
# b = timedelta(weeks=3, days=5, hours=9, minutes=54, seconds=17, microseconds=234,
#               milliseconds=123,)
# print('a :', a)
# print('b :', b)
# c = a + b
# print('a + b :', c)
# print('now :', n)
# print('a - n :', a - n)
# # print('a + n :', a + n)
# delta = n - c
# print('delta :', delta, type(delta))
# print('delta * 2 :', delta * 2, type(delta))
# print('delta / 2 :', delta / 2, type(delta))
# print('delta // 3:', delta // 3, type(delta))




########################################################
######### Модуль collections ################
############## Counter #################

from collections import Counter


# c = Counter('dsadsagdsesg fbjg hggrd  jhgdhgvhljgfjhgcmjl')
# print('c : ', c, type(c))
# print('most ', c.most_common(5))



#
# lst = [5, 6, 7, 1, 3, 9, 9, 1, 2, 5, 5, 7, 7]
# c1 = Counter(lst)
# # c1 = dict(c1)
# print('lst : ', c1, type(c1))
#
# print('most ', c1.most_common(5))

# text = '''
# The Republican candidate for Virginia attorney general,
# Cuban American Jason Miyares, was also leading that vote count.
# And Republicans seemed to be closing in on control
# of the state's House of Delegates.
#
# In other elections across the US on Tuesday:
#
# Republican challenger Jack Ciattarelli had a narrow lead
# over New Jersey's Democratic Governor Phil Murphy, with 88%
# of votes reported
# Amid surging crime, Minneapolis voters rejected a proposal
# to replace the city's police department with a new Department
# of Public Safety, more than a year after the murder of George
# Floyd by an officer
# As expected, Democrat Eric Adams won New York City's mayoral
# election to replace his party colleague Bill de Blasio;
# Republican challenger Curtis Sliwa was involved in an argument
# at his polling station after turning up to vote with a pet cat
# and being told his furry friend Gizmo could not enter
# Pittsburgh picked its first black mayor, Democrat Ed Gainey
# '''
#
#
# words = text.upper().split()
# print(words)
#
#
# res = Counter(words)
# print('counter : ', type(res), res)
# words = []
# counts = []
#
# for key, vol in res.items():
#     words.append(key)
#     counts.append(vol)
# print(len(words), words)
# print(len(counts), counts)
#
# print('res.most_common : ', res.most_common(5))


# print('sorted : ', *sorted(res.items(), key=lambda x: x[1], reverse=True), sep='\n')
# print('sum : ', sum(res.values()))
# print('item : ', res.items())
# print('res : ', type(res), res)
# print(len(res))
############### end of Counter ##################


###########  defaultdict ################
from collections import defaultdict

# Устанавливает пустой элемент указанного типа в качестве
# аргумента НОВОГО(до этого не существующего) элемента словаря
# без этой команды Python выдает ошибку об отсутствии ключа.

# d = {}
# print(d['key'])


#
# d = defaultdict(int)
#
# d['key'] = 'Hello'
#
# print(d['key'])
# print(d)
#
# print(d['key1'])
# print(d['key2'])
# print(d)
#
# # d = defaultdict(int)
# # print('d=', d)
# # # # d = defaultdict(list)
# # print("d['key']=", d['key'], type(d['key']))
# # print('d=', d)
# # print("d['A']=", d['A'], type(d['A']))
# # print("d['rrrrr']=", d['rrrrr'], type(d['rrrrr']))
# # print('d=', d)
# ##############################################


######### namedtuple ----------  ##################
                # from collections import namedtuple
                #
                # fruit = namedtuple('fruit', 'number variety color')
                #
                # print(fruit)
                #
                # guava = fruit(number=2, variety='HoneyCrisp', color='green')
                # apple = fruit(number=5, variety='Granny Smith', color='red')
                #
                # print(guava.color)
                # print(guava.number)
                # print(guava)
                # print(apple.variety)


############### end of Collections ##################


from faker import Faker
import csv



# fake = Faker()
# fake = Faker(locale='ru')

# print(fake.name())

# print(*dir(fake), sep='\n')


# print(fake.name())
# print(fake.address())
# print(fake.email())
####################################################

# fake = Faker(locale="en_GB")
# fake = Faker("zh_CN")
# fake = Faker(locale="ru_RU")
# print(fake.name())
# print(fake.address())


##############################################################

fake = Faker()
# #
# # print(*dir(fake), sep='\n')
# #
# print('prefix :', fake.prefix())
# print('name :', fake.name())
# print('id :', fake.ssn())
# print('country :', fake.country())
# # print(fake.state())  # USA
# print('city :', fake.city())
# # print(fake.zipcode())  # USA
# print('address :', fake.address())
# print('job :', fake.job())
# print('company :', fake.company())
# print('phone number :', fake.phone_number())
# print('email :', fake.email())
# print('url :', fake.url())
# print('date :', fake.date())
# print('time :', fake.time())
# print('word :', fake.word())
# print('sentences :', fake.sentences())
# print('text :', fake.text())
# print('year :', fake.year())
# print('month :', fake.month())
#######################################################################


# print('% num 1-9 :', fake.bothify('%%%%%%%%%%%%%%%%%%%%%%'))  #   % -num w/o 0


# print('# numbers :', fake.bothify('#################'))  #   # - number

# print('? letters :', fake.bothify('??????????????????????'))  #   ? - letters


# print('phone :', fake.numerify(text='+##(###)###-##-##'))


# print('ISBN :', fake.bothify(text='ISBN ????-%%%%-####-##-##'))

#################################################

# p = fake.simple_profile()
# print('#' * 80)
# print(*p, sep=' : ')
# print('#' * 80)
#
# print('username  :', p['username'])
# print('name      :', p['name'])
# print('sex       :', p['sex'])
# print('address   :', p['address'])
# print('mail      :', p['mail'])
# print('birthdate :', p['birthdate'])
# print('='*80)


# print('birthdate :', fake.simple_profile()['birthdate'])

###########################################################


# fake = Faker()
# # fake = Faker(locale="ru_RU")
#
# name = []
# for i in range(670):  # 401(ru)   670(en)
#     name.append(fake.unique.first_name())
# print(*name)
# print(len(name))
# print(len(set(name)))

############################################################

# with open('faker.csv', 'w') as f:
#     wr = csv.writer(f, delimiter=';')
#     wr.writerow(['Name',
#                  'Surname',
#                  'job',
#                  'address',
#                  'phone',
#                  'email',
#                  'credit_card_number',
#                  'credit_card_expire',
#                  'credit_card_security_code'])
#     for i in range(50):
#         f1 = fake.unique.name().split()
#         print(f1, type(f1))
#         fake_name = f1[0]
#         fake_surname = f1[1]
#         wr.writerow([fake_name, fake_surname, fake.job(),
#                      fake.unique.address(), fake.numerify(text='+##(###)###-##-##'),
#                      fake.unique.email(), fake.unique.credit_card_number(),
#                      fake.credit_card_expire(), fake.credit_card_security_code()])

########################## END




