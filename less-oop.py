


# from func import pr, pr1, pr3
# from func import *
# import func
# from func import pr as f1


# pr('Hello, world!')
# pr1('Hello, world!')
# pr3('Hello, world!')

# f1('Hello!')


# print('run :', __name__)
#





##################################################################
############ Атрибуты и методы Class ##################################
#################################################################
################# Методы __init__, __str__, __repr__ ############
#################################################################
#
# class Human: #  StudentUniversity
#     hands = 2
#     foots = 2
#     head = 1
#
#
#     def __init__(self,  age=18, sex='man', name='Mikola'):
#         self.sex = sex
#         self.age = age
#         self.name = name
#
#
#     def __str__(self):  # print()
#         # hum1.age += 100
#         # return f'Hello, {self.name}!'
#         return f'Human: {self.sex} {self.name} {str(self.age)} years old has {self.foots} foots'
#
#
#     def __repr__(self):
#         return 'Human(' + self.sex + ',' + self.name + ',' + str(self.age) + ')'
#
#
#
# hum1 = Human(22, 'boy', 'Oleg')
# print(hum1)
# hum2 = Human()
# print(hum2.name, hum2.age)
# print(hum1.name, hum1.age, hum1.foots)
# hum1.name = 'Petro'
# print(hum1.name, hum1.age, hum1.foots)
# hum1.age += hum2.age
# print(hum1.age)
#
# print(hum1)
# print(hum2)
#
# list1 = {hum1, hum2}
# print(type(list1))
# print(list1)


# print(*dir(hum1), sep='\n')




#
# hum1 = Human(25, 'boy')
# hum2 = Human()
# # print(hum1.name, hum1.hands, hum1.age)
# # print(hum2.name, hum2.hands, hum2.age)
# # # hum1.age += hum2.age
# # print(hum1.name, hum1.hands, hum1.age)
#
# print(hum1)
# print(type(hum1))
#
# list1 = (hum1, hum2)
# print(list1)
# print(type(list1))
#
#
#
# a = 1
# print(type(a))


# print(dir(hum1))
#
#

#
#
# hum1 = Human(21, 'woman', 'Olena')
# # print(hum1)
# # hum2 = Human(18, 'man', 'Alex')
# # hum3 = Human()
# # print([hum1, hum2, hum3])
# print(hum1.__class__)
# print(type(hum1))
# print(*dir(hum1), sep='\n')
# # t = 'Hello'
# # l = [1,2]
# # print(t.__class__)
# # print(l.__class__)
# # print(hum2.name + hum1.name)
# # print(hum1.name)
# # print(hum3.name)
# # print(hum1.age + hum2.age)
# # print(hum1.sex)
# # print(hum1.foots)
# # print(hum1.hands)
# #
# # print(*dir(Human), sep='\n')

#
# ######################################################################
# #   ПРИКЛАД  (з поліморфізмом та успадкуванням)   ######################################
# # ######################################################################
# class Door:
#     colour = 'white'
#
#     def __init__(self, number=0, status='open'):
#         self.number = int(number)
#         self.status = status
#
#     def __str__(self): # print()
#         return f'The {self.colour} door number {str(self.number)} is {self.status}'
#         # return 'The ' + self.colour + ' door number ' + str(self.number) + ' is ' + self.status
#
#     def open(self):
#         self.status = 'open'
#
#
#     def close(self):
#         self.status = 'closed'
#
#     def colouring(self):
#         col = input('input new colour = ')
#         self.colour = col
#
#     def numbering(self):
#         num = int(input('input new number = '))
#         self.number = num
#
#     def nock(self):
#         print('Nock-Nock-Nock!!!')
#         # self.numbering()
#
#
#     def __add__(self, other):  # +
#         # return self.number + other.number
#         return str(self.number) + '+' + str(other.number) + '=' + str(self.number + other.number)
#
#     def __len__(self):
#         return len(str(self.number))
#
# # door1 = Door(123)
# # door2 = Door(444)
# # print(door1)
# # door1.close()
# # print(door1)
# # door1.open()
# # print(door1)
# # # door1.colouring()
# # print(door1)
# # # door1.numbering()
# # print(door1)
# # door1.nock()
# # print(door1)
# # print(door2)
# # print('len=', len(door1))
#
# # print(door1 + door2)
#
#
# #
# class SecurityDoor(Door):
#     colour = 'grey'
#
#     def __init__(self, number=0, status='closed', locked=True):
#         Door.__init__(self, number, status)
#         self.locked = locked
#
#
#     def __str__(self):
#         lock = 'locked' if self.locked else 'unlocked'
#         return f'the door {str(self.number)} is {self.colour}, {self.status} and {lock}'
#         # return f'the door {str(self.number)} is {self.colour}, {self.status} and {self.locked}'
#
#     def open(self):
#         if self.locked == False:
#             self.status = 'open'
#
#     def close(self):
#         self.status = 'close'
#         self.locked = True
#
#
#
#
#
# d1 = SecurityDoor()
# d2 = Door()
# print(d1)
# d1.open()
# print(d1)
# d1.locked = False
# d1.open()
# d2.open()
# print(d1)
# print(d2)
# d1.close()
# d2.close()
# print(d1)
# print(d2)
#
# print(*dir(d2), sep='\n')
#

# door3 = SecurityDoor()
# door3.locked = False
# print(door3)
# door3.open()
# print(door3)
# door3.close()
# print(door3)


#

#
#










# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#                УСПАДКУВАННЯ (Inheritance)
#############################################

# class Human:
#
#     def __init__(self, name='NoName', surname='NoSurname', age=18):
#         self.age = age
#         self.name = name
#         self.surname = surname
#
#
#
#     def __repr__(self):
#         return '=repr=' + self.name + ' ' + self.surname + ' ' + str(self.age)
#
#     def __str__(self):
#         return '=str=   ' + self.name + ' ' + self.surname + ' ' + str(self.age)
#
#
#
# class Student(Human):
#
#     def __init__(self, name='NoName', surname='NoSurname', age=18, group=222):
#         Human.__init__(self, name, surname, age)
#         self.group = group
#
#     def __str__(self):
#         return f'group {self.group} includs student {self.name} {self.surname}, {self.age} years old.'
#         # return super.__str__(self) + ' group ' + str(self.group)
#
#
# n2 = Student()
# n3 = Student('Petya', "Pupkin", 21, 555)
# print(n2)
# print(n3)
#
# print(isinstance(n3, Human), type(n3))
#
# print(n2.group, n2.name, n2.surname, n2.age)
# print('!!!', n2)
# print(n3.group, n3.name, n3.surname, n3.age)
# print(n3)
# # # # breakpoint()
# # #
# # n3.name = 'John'
# # n3.surname = 'Kozlov'
# # n3.age = 55
# # print('+++', n3)
# n3 = Student(name='John1', group=123, surname='Kozloff')
# print(n3)
# print(n3.group, n3.name, n3.surname, n3.age, type(n3))
# n3.group = 9999
#
# print(n3.group, n3.name, n3.surname, n3.age)
# print(f'group {n3.group} includs student {n3.name} {n3.surname}, {n3.age} years old.')
# print(n3)
############################################################


######################################################
############ Stack (LIFO) ############################
######################################################

# !!!!!!!!!!!!!!!!!!!!!!!!! KH-23m !!!!!!!!!!!!!!!!!!!!!

#
# class Stack:
#
#     def __init__(self):
#         self.number = None
#
#     def inp(self, x):
#         self.number = [x, self.number]
#
#     def pop(self):
#         assert self.number is not None, 'Stack is empty'
#         x = self.number[0]
#         self.number = self.number[1]
#         return x
#
#
# a = Stack()
# a.inp(input('Input element : '))
# a.inp(input('Input element : '))
# a.inp(input('Input element : '))
# a.inp(input('Input element : '))
#
# print(type(a))
# print(a.number)
#
# print(a.pop())
# print(a.pop())
# print(a.pop())
# print(a.pop())
# print(a.pop())

# breakpoint()

#
# class Stack:
#
#     def __init__(self):
#         self.number = None
#
#     def inp(self, x):
#         if self.number:
#             self.number = [x] + self.number
#         else:
#             self.number = [x]
#
#     def pop(self):
#         if not self.number:
#             return 'Stack is empty'
#         x = self.number[0]
#         self.number = self.number[1:]
#         return x
#
#
# a = Stack()
# b = Stack()
# a.inp(input('Input element : '))
# b.inp(input('Input element : '))
# a.inp(input('Input element : '))
# b.inp(input('Input element : '))
# a.inp(input('Input element : '))
#
#
# print(type(a))
# print(a.number)
# print(b.number)
#
# print(a.pop())
# print(a.pop())
# print(a.pop())
# print(b.pop())
# print(b.pop())




#######################################################################
#############     ІНКАПСУЛЯЦІЯ (Encapsulation)     ####################
#######################################################################

#
# class StudentUniver:
#     animal = 'Human'
#
#     def __init__(self, height, age):
#         self.height = height
#         self.age = age
#         self.health = '50x50'
#
#     def __str__(self): # PRINT
#         return f'{self.animal} Student {self.age} years old {self.height} сm fills {self.health}.'
#
#
#     def _health_change(self, health='good'):
#         self.health = health
#         return self.health
#
#     def __ill(self, health='bed'):
#         self.health = health
#         return self.health
#
#     def fill_bed(self, state):
#         self.__ill(state)
#
#     def __average__(obj1, obj2):
#         return (obj1.height + obj2.height)/2
#
#     @classmethod
#     def anim(cls, anim):
#         cls.animal = anim
#
#     @staticmethod
#     def get_hello(text):
#         print('Hello!', text)
#
#
# s1 = StudentUniver(200, 18)
# s2 = StudentUniver(180, 18)
# print(s1)
# print(s2)
# # s1._health_change('Very nice!')
# # print(s1)
# # print(*dir(s1), sep='\n')
# s1._StudentUniver__ill('bed!!!!')
# # s1.fill_bed('very bed!')
# # print(s1)
# s1.animal = 'Got'
# # print(StudentUniver.__average__(s1, s2))
# StudentUniver.anim('Robot')
# print(s1)
# print(s2)
#
# StudentUniver.get_hello('Vasya')
#


######################################################
### School ###########################################
###     ПОЛІМОРФІЗМ (Polymorphism)    ################
######################################################

class SchoolMember:
    count_members = 0

    def __init__(self, name='Noname', age=18, surname='NoSurname'):
        self.name = name
        self.surname = surname
        self.age = age
        SchoolMember.count_members += 1
        print(f'(Створено SchoolMember: {self.name}). Тепер нас {SchoolMember.count_members}.', end=' ')


    def tell(self):
        print(f'Ім\'я:"{self.name}" Призвище:"{self.surname}" Вік:"{self.age}"', end=" ")


# s1 = SchoolMember()
# s2 = SchoolMember('Jon', 19)
# s3 = SchoolMember('Ann', 21)
# # print(s1)
# # print(s2)
# # print(s3)
# s1.tell()
# s2.tell()
# s3.tell()


class Teacher(SchoolMember):

    def __init__(self, name='Noname', age=25, surname='NoSurname', salary=1000):
        SchoolMember.__init__(self, name, age, surname)
        self.salary = salary
        self.status = '<викладач>'
        print(f'(Створено Teacher: {self.name}).')

    def tell(self):
        SchoolMember.tell(self)
        print(self.status, 'Зарплатня: "{0:d}" грн.'.format(self.salary))


# t1 = Teacher(name='Ben', age=45, salary=1000)
# t2 = Teacher(name='Nick', surname='Koval', salary=5500, age=35)
# t1.tell()
# t2.tell()



class Student(SchoolMember):

    def __init__(self, name, age, surname='NoSurname', marks='100'):
        SchoolMember.__init__(self, name, age, surname)
        self.marks = marks
        self.status = '<слухач>'
        print('(Створено Student: {0})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print(self.status, 'Оцінка: "{0:d}"'.format(self.marks))

    def __eq__(self, other):
        return self.marks == other.marks



t1 = Teacher(name='Vasiliy', surname='Mr. Shevchenko', age=35, salary=20000)
print(SchoolMember.count_members)
t2 = Teacher(name='Oleg', surname='Dr. Koval', age=40, salary=30000)
print(SchoolMember.count_members)
s1 = Student(name='Mykola', surname='Petrov', age=20, marks=95)
print(SchoolMember.count_members)
s2 = Student(surname='Hmara', name='Petro', marks=95, age=19)
# s2 = s1
# print(SchoolMember.count_members)
# sm1 = SchoolMember(name='Olena', surname='Grineva', age=17)
# print(SchoolMember.count_members)
#
#
# print()
# print('='*80)
#
members = [t1, s2, s1, t2]

for member in members:
    member.tell()
    print('.'*80)
#
#
#
# print(*dir(s1), sep='\n')
print(s1==s2)
print(id(s1))
print(id(s2))

############### END


# a = [4, 5]
# t = ['Hello, ', 'Vasya']
# b = ['-34.56', '88.23']
# t1 = ['How do You', ' Do!']
#
# list1 = [a, b, t, t1]
#
# for el in list1:
#     print(el[0]+el[1])







# class A:
#     def __init__(self, num=0):
#         self.num = num
#
#     def add(self, num=1):
#         self.num += num
#
#
# class B(A):
#     def __init__(self, num=0):
#         A.__init__(self, num)
#         super().add(num)
#
#     def add(self, num=1):
#         self.num += 2 * num
#
#
# a = A(2)
# print(a.num)
# a.add(3)
# print(a.num)
# b = B(4)
# print(a.num, b.num)
# b.add(5)
# print(a.num, b.num)
# print(a.num + b.num)