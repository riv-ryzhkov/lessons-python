#========================================
# import copy
#
#
# # Абстрактний Клас прототипу
# class Prototype:
#     def clone(self):
#         pass
#
#
# # Конкретний клас прототипу
# class ConcretePrototype(Prototype):
#     def __init__(self, value):
#         self.value = value
#
#     def clone(self):
#         return copy.copy(self)
#
#
# # Приклад використання
# if __name__ == "__main__":
#     prototype = ConcretePrototype("Initial version")
#     clone = prototype.clone()
#     # clone = prototype
#
#     print(id(prototype))
#     print(id(clone))
#
#     print("Original:", prototype.value)
#     print("Clone:", clone.value)
#
#     prototype.value = 'Change1'
#     clone.value = 'Change2'
#
#     print("Original:", prototype.value)
#     print("Clone:", clone.value)

# ==============================================
#  Приклад з адресами (1 version)
# ==============================================
# import copy
#
#
# class Adress:
#     def __init__(self, build=0, street='NoStreet', city='NoCity', country='NoCountry'):
#         self.build = build
#         self.street = street
#         self.city = city
#         self.country = country
#
#
#     def __str__(self):
#         return f'{self.build}, {self.street}, {self.city}, {self.country}'
#
#
# class Person:
#     def __init__(self, adress='NoAdress', name='NoName'):
#         self.name = name
#         self.adress = adress
#
#     def clone(self, obj1):
#         self.name = copy.copy(obj1.name)
#         self.adress = copy.deepcopy(obj1.adress)
#
#     def __str__(self):
#         return f"{self.name}'s adress is {self.adress} "
#
#     def __repr__(self):
#         return
#
#
#
# adress = Adress('28', 'Shevchenko street', 'Dnipro', 'Ukraine')
#
# Mark = Person(adress, 'Mark')
# print('->', Mark)
#
#
#
# # 1й варіант ---!
# # Anna = Mark
# # Anna.name = 'Anna'
# # print(id(Mark))
# # print(id(Anna))
#
#
# # 2й варіант     -+-+-+-+!
# # Anna = copy.copy(Mark)
# # Anna = copy.deepcopy(Mark)
# # print(id(Mark))
# # print(id(Anna))
# # Anna.name = 'Anna'
# # # Anna.adress = copy.copy(adress)
# # Anna.adress.build = 88
# # Anna.adress.street = "Koganovs'kogo street"
#
#
#
#
# # 3й варіант ++++++!
# # Anna = Person(copy.copy(Mark.adress), 'Anna')
# # Mark.adress.city = 'Kiev'
# # Anna.adress.build = 11
#
#
#
# # Варіант клонування +++++++++++++++!
# Anna = Person()
# Anna.clone(Mark)
# # Anna = copy.deepcopy(Mark)
# Anna.name = 'Anna'
# Anna.adress.build = 55
# # #
# # #
# print(Mark)
# print(Anna)
#

# ===================================================
# 2nd version
# ===================================================
#
# import copy
#
#
# class Adress:
#     def __init__(self, build=0, street='NoStreet', city='NoCity', country='NoCountry'):
#         self.build = build
#         self.street = street
#         self.city = city
#         self.country = country
#
#
#     def __str__(self):
#         return f'{self.build}, {self.street}, {self.city}, {self.country}'
#
#
# class Person:
#     def __init__(self, name='NoName', adress='NoAdress'):
#         self.name = name
#         self.adress = adress
#
#     def clone(self):
#         return copy.copy(self)
#         # return copy.deepcopy(self)
#
#
#     def __str__(self):
#         return f"{self.name}'s adress is {self.adress} "
#
#     def __repr__(self):
#         return
#
#
# adress = Adress('28', 'Shevchenko street', 'Dnipro', 'Ukraine')
#
# Mark = Person('Mark', adress)
#
#
# print(id(Mark), Mark)
# Anna = Mark.clone()
# print(id(Anna), Anna)
#
# Anna.name = 'Anna'
# Anna.adress.build = 77
# Anna.adress.street = 'Yavornyzkogo street'
#
# print(Mark)
# print(Anna)




"""
Патерн Прототип дозволяє створювати копії об'єктів, 
зберігаючи їхні властивості та структуру, 
ініціюючи створення нового об'єкта на основі існуючого прототипу.

У даному прикладі є базовий клас Prototype, 
який має метод clone. 
Клас ConcretePrototype є конкретною реалізацією прототипу, 
який має поле value.

Метод clone в класі ConcretePrototype використовує функцію copy.copy(self) 
для створення поверхневої копії об'єкта. 
Це дозволяє нам створювати новий об'єкт, 
який має ті ж властивості, але не впливає на оригінальний об'єкт.

У прикладі використання ми спочатку створюємо об'єкт ConcretePrototype 
зі значенням "Initial version". 
Потім ми створюємо його клон за допомогою методу clone, 
і виводимо значення об'єкта і його клону.

Патерн Прототип дозволяє зменшити кількість дублювання коду 
при створенні об'єктів, а також дозволяє змінювати структуру об'єкта 
без необхідності змінювати код створення.
"""
