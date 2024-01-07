# Single Responsibility Principle - SRP

"""
Принцип однієї відповідальності (SRP) вимагає,
щоб клас мав лише одну причину для зміни.
Основна ідея - кожен клас повинен мати
одну конкретну відповідальність або функцію.
"""

# Клас, який порушує SRP
# class Employee:
#     def __init__(self, name, employee_id):
#         self.name = name
#         self.employee_id = employee_id
#
#     def calculate_salary(self):
#         # Логіка для розрахунку зарплати
#         pass
#
#     def generate_report(self):
#         # Логіка для створення звіту
#         pass
#
#     def save_to_database(self):
#         # Логіка для збереження даних в базу даних
#         pass



# Клас, який дотримується SRP
class Employee:
    def __init__(self, name='Mikle'):
        self.name = name

    def __repr__(self):
        return self.name


# Клас для розрахунку зарплати
class SalaryCalculator:
    def __init__(self, name):
        self.name = name

    def calculate_salary(self, employee):
        print(f'{self.name} calculates the salary for {employee}')
        # Логіка для розрахунку зарплати
        pass

# Клас для генерації звіту
class ReportGenerator:
    def __init__(self, name):
        self.name = name

    def generate_report(self, employee):
        print(f'{self.name} generates the report for {employee}.')
        # Логіка для створення звіту
        pass

# Клас для збереження в базу даних
class DatabaseSaver:
    def __init__(self, name):
        self.name = name

    def save_to_database(self, employee):
        print(f'{self.name} saves the data about {employee}.')
        # Логіка для збереження даних в базу даних
        pass



user1 = Employee()
user2 = Employee('Jon')

buhgalter1 = SalaryCalculator('Bob')
buhgalter2 = SalaryCalculator('Andrey')

saver1 = DatabaseSaver('Ann')
saver2 = DatabaseSaver('Frank')

reporter1 = ReportGenerator('Daniel')
reporter2 = ReportGenerator('Elizabet')


buhgalter1.calculate_salary(user1)
buhgalter1.calculate_salary(user2)
buhgalter2.calculate_salary(user1)

saver1.save_to_database(user2)
saver2.save_to_database(user1)

reporter1.generate_report(user1)



"""
У першому прикладі клас Employee виконує багато різних функцій, 
таких як розрахунок зарплати, генерація звіту та збереження в базу даних. 
Це порушує SRP, оскільки клас має більше однієї відповідальності.

У другому прикладі ми розбиваємо цей клас на кілька окремих класів, 
які кожен має одну відповідальність. 
Клас Employee відповідає тільки за зберігання даних про співробітника. 
Окремі класи SalaryCalculator, ReportGenerator і DatabaseSaver 
відповідають за розрахунок зарплати, 
генерацію звіту та збереження в базу даних відповідно. 
Це полегшує розширення та зміну кожного функціонального блоку окремо, 
не впливаючи на інші.
"""