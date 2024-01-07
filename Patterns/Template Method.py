"""
Паттерн Template Method (Метод Шаблону) є поведінковим патерном проектування,
який дозволяє визначити загальну структуру алгоритму,
але відкладає виконання окремих кроків цього алгоритму до підкласів.
Цей паттерн використовується, коли у вас є алгоритм,
що складається з кількох кроків,
і дозволяє підкласам реалізувати ці кроки за своїми потребами,
не змінюючи загальної структури алгоритму.

Основна ідея полягає в тому,
що у базовому класі визначається абстрактний метод (або кілька методів),
які представляють кроки алгоритму.
Підкласи цього базового класу реалізують ці методи,
конкретизуючи їхню роботу.
Весь алгоритм виконується через метод у базовому класі,
який викликає ці абстрактні методи.

Отже, основні компоненти паттерна Template Method включають:

Абстрактний клас (Base Class):
Це клас, який містить загальну структуру алгоритму та абстрактні методи (кроки),
які повинні бути реалізовані в підкласах.

Конкретні підкласи (Concrete Subclasses):
Ці класи успадковують абстрактний клас і реалізують абстрактні методи таким чином,
як це відповідає їхнім потребам.

Метод шаблону (Template Method):
Це метод у базовому класі,
який визначає загальну структуру алгоритму
та викликає абстрактні методи (кроки) у правильному порядку.
"""


# Абстрактний клас з методом шаблону
# class AbstractClass:
#     def template_method(self):
#         self.common_step()
#         self.specialized_step()
#
#     def common_step(self):
#         pass
#
#     def specialized_step(self):
#         pass
#
#
# # Конкретні підкласи
# class ConcreteClassA(AbstractClass):
#     def common_step(self):
#         print("ConcreteClassA: Common step implementation")
#
#     def specialized_step(self):
#         print("ConcreteClassA: Specialized step implementation")
#
#
# class ConcreteClassB(AbstractClass):
#     def common_step(self):
#         print("ConcreteClassB: Common step implementation")
#
#     def specialized_step(self):
#         print("ConcreteClassB: Specialized step implementation")
#
#
# # Використання
# def client_code(abstract_class):
#     abstract_class.template_method()
#
#
# if __name__ == "__main__":
#     print("Client code with ConcreteClassA:")
#     client_code(ConcreteClassA())
#
#     print("\nClient code with ConcreteClassB:")
#     client_code(ConcreteClassB())


"""
У цьому прикладі є абстрактний клас AbstractClass, 
який містить метод шаблону template_method. 
Цей метод визначає загальну структуру алгоритму 
та викликає два абстрактні методи common_step і specialized_step. 
Конкретні підкласи ConcreteClassA і ConcreteClassB 
успадковують AbstractClass і реалізують ці два абстрактні методи 
відповідно до своїх потреб.

Клієнтський код демонструє використання патерна Template Method, 
створюючи об'єкти підкласів і викликаючи їхні методи template_method. 
Кожен з підкласів виконує свої власні реалізації для common_step і specialized_step, 
але загальна структура алгоритму залишається незмінною.
"""

# Абстрактний клас з методом шаблону (Template)
# class Beverage():
#     def prepare_beverage(self):
#         self.boil_water()
#         self.brew()
#         self.pour_in_cup()
#         self.add_condiments()
#
#     def boil_water(self):
#         print("Boiling water")
#
#     def brew(self):
#         pass
#
#     def pour_in_cup(self):
#         print("Pouring into cup")
#
#     def add_condiments(self):
#         pass
#
#
# # Конкретний підклас - чай
# class Tea(Beverage):
#     def __init__(self):
#         self.name = 'Tea'
#
#     def brew(self):
#         print("Steeping the tea")
#
#     def add_condiments(self):
#         print("Adding lemon")
#
#
# # Конкретний підклас - кава
# class Coffee(Beverage):
#     def __init__(self):
#         self.name = 'Coffee'
#
#     def brew(self):
#         print("Dripping coffee through filter")
#
#     def add_condiments(self):
#         print("Adding sugar and milk")
#
#
# # Використання
# if __name__ == "__main__":
#     print("Making tea:")
#     tea = Tea()
#     tea.prepare_beverage()
#
#     print("\nMaking coffee:")
#     coffee = Coffee()
#     coffee.prepare_beverage()
#
#     # print('.' * 80)
#     #
#     # drinks = [tea, coffee, coffee, tea, tea]
#     #
#     # for drink in drinks:
#     #     print(f'Preparing {drink.name}:')
#     #     drink.prepare_beverage()
#     #     print('.' * 80)



"""
У цьому прикладі Beverage є абстрактним класом з методом шаблону prepare_beverage. 
Цей метод визначає загальну структуру алгоритму приготування напою, 
але залишає деякі кроки (наприклад, brew і add_condiments) 
для реалізації у конкретних підкласах.

Tea і Coffee - це конкретні підкласи, 
які успадковують Beverage і реалізують абстрактні методи brew і add_condiments 
відповідно до рецепту приготування чаю та кави. 


В результаті виклику методу prepare_beverage 
об'єктів Tea та Coffee виконується загальний алгоритм приготування напою, 
але конкретні кроки реалізовані відповідно до рецепту для кожного напою.
"""