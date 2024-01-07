######################################################################
#   ПРИМЕР  (с полиморфизмом)   ######################################
######################################################################
class Door:
    colour = 'brown'

    def __init__(self, number, status='open'):
        self.number = number
        self.status = status

    def open(self):
        self.status = 'open'

    def close(self):
        self.status = 'closed'

    def coloured(self):
        col = input('colour = ')
        self.colour = col

    def __str__(self):
        return 'The ' + self.colour + ' door number ' + str(self.number) + ' is ' + self.status
        # return 'Hello, Vasya!'

    def __add__(self, other):   #  +
        return self.number + other.number
        # return str(self.number) + '->' + str(other.number)

    def __len__(self):
        return len(str(self.number))

    if __name__ == "__main__":
        print('!!!Start our Program!!!')
        print()


door1 = Door(338990798)
door2 = Door(111)
print(*dir(door1), sep='\n')
print(door1.__class__)
print(type(door1))
print(door1)
print(door1 + door2)
print(len(door1))
print(door1.status)
door1.close()
print(door1.status)
door1.open()
print(door1.status)
print(door1.colour)
door1.coloured()
print(door1.colour)




d1 = Door(222, 'open')
d2 = Door(333, 'open')
print('d1+d2  :   ', d1+d2)
print('d1.number  :', d1.number)
print('d1.color   :', d1.colour)
print('d1.status  :', d1.status)
d1.close()
print('d1.status  :', d1.status)
d1.status = ':-)'
print('d1.status  :', d1.status)

d1 = Door(15, 'closed')
d2 = Door(16, 'open')
print('the door', d1.number, 'is', d1.colour, 'and', d1.status)
print('the door', d2.number, 'is', d2.colour, 'and', d2.status)
d1.open()
d2.close()
print('the door', d1.number, 'is', d1.colour, 'and', d1.status)
print('the door', d2.number, 'is', d2.colour, 'and', d2.status)
# print(dir(d1))
print(d1)
print(d1+d2)
print(len(d1))
print(d2.__class__)





class SecurityDoor(Door):
    colour = 'grey'

    def __init__(self, number, status='closed', locked=True):
        Door.__init__(self, number, status)
        self.locked = locked
        # self.colour = super().colour

    def open(self):
        if not self.locked:
            self.status = 'open'

    # def __str__(self):
    #     return Door.__str__(self)
    #     return 'the door ' + str(self.number) + ' is ' + self.colour + ' and ' + self.status

#
#
d3 = SecurityDoor(17, 'closed')
print(d3)
print('!!!!!!!!!!!!!!', isinstance(d3, Door))
d3.open()
print(d3)
d3.locked = False
d3.open()
d3.colour = 'white'
# print(d3.colour)
print(d3)
d3.close()
print(d3)
