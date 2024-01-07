# Liskov Substitution Principle - LSP

"""
Принцип заміщення Лісков (Liskov Substitution Principle - LSP)
говорить про те, що об'єкти підкласів можуть замінювати об'єкти базового класу
без зміни бажаної коректної роботи програми.
"""

#
# class Bird:
#     name = 'Bird'
#
#     def carry_eggs(self):
#         print(f'{self.name} carry eggs.')
#
#     # def fly(self):
#     #     print('      Error!!!!!! Bird is a parent class!')
#     #     pass
#
#
# class Ostrich(Bird):
#     name = 'Ostrich'
#
#     def fly(self):
#         # Острич(Страус) не летять, тому ми перевизначаємо метод
#         print(f', but CAN NOT fly!')
#         pass
#
#
#
#
# class Eagle(Bird):
#     name = 'Eagle'
#
#     def fly(self):
#         print(f' and CAN fly!')
#         pass
#
#
# class Make_Fly:
#     @staticmethod
#     def make_bird_fly(bird):
#         bird.fly()
#
#
# # Приклади використання
# eagle = Eagle()
# ostrich = Ostrich()
# bird = Bird()
#
#
# bird.carry_eggs()
# eagle.carry_eggs()  # eagle легко замінює bird в батьківському класі.
# ostrich.carry_eggs()  # ostrich легко замінює bird в батьківському класі.
#
# animals = [eagle, ostrich, bird]  # eagle та ostrich спрацьовує
# # а bird не може замінити інстанс дочірнього класу
#
#
# for animal in animals:
#     print(animal.name, end=' is a bird')
#     Make_Fly.make_bird_fly(animal)
#
#



"""
У цьому прикладі є базовий клас Bird з методом fly(), 
який описує можливість польоту для всіх птахів.

Потім ми маємо підклас Ostrich, який також успадковує від Bird. 
Проте, оскільки страуси не можуть летіти, 
ми перевизначаємо метод fly() в підкласі Ostrich, 
якщо спробуємо викликати цей метод для страуса.

Важливою рисою цього прикладу є те, 
що ми можемо передавати як об'єкт базового класу Bird, 
так і об'єкт підкласу Ostrich до функції make_bird_fly(), 
і це має бути можливо без зміни бажаної коректної роботи програми. 
Тобто, принцип заміщення Лісков дотримується.
"""