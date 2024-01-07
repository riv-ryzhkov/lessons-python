# Клас Компоненту
class Coffee:
    def cost(self):
        return 5

    # def name(self):
    #     return 'Coffee'


# Базовий клас для декораторів
class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost()

    # def name(self):
    #     return self._coffee.name()


# Конкретні декоратори
class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 4

    # def name(self):
    #     return self._coffee.name() + ' with Milk'


class SugarDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 3

    # def name(self):
    #     return self._coffee.name() + ' with Sugar'


# Приклад використання
if __name__ == "__main__":
    simple_coffee = Coffee()
    print("Simple coffee cost:", simple_coffee.cost())

    milk_coffee = MilkDecorator(simple_coffee)
    print("Milk coffee cost:", milk_coffee.cost())

    sugar_coffee = SugarDecorator(simple_coffee)
    print("Sugar coffee cost:", sugar_coffee.cost())

    sugar_milk_coffee = SugarDecorator(milk_coffee)
    print("Sugar milk coffee cost:", sugar_milk_coffee.cost())

    milk_sugar_coffee = MilkDecorator(sugar_coffee)
    print("Milk coffee with sugar cost:", milk_sugar_coffee.cost())

    print('='*80)


    # offers = [
    #     simple_coffee,
    #     sugar_coffee,
    #     milk_sugar_coffee,
    #     milk_coffee,
    #     sugar_milk_coffee,
    #     milk_coffee
    # ]
    #
    # for drink in offers:
    #     print('Вартість замовлення :', drink.name(), drink.cost())


"""
Патерн Decorator дозволяє динамічно додавати нову функціональність до об'єкту, 
обгортаючи його у об'єкти декораторів. 
Це дає можливість створювати композиції об'єктів з різною функціональністю.

У цьому прикладі є клас Coffee, який представляє базовий компонент.

CoffeeDecorator є базовим класом для всіх декораторів. 
Він містить посилання на об'єкт Coffee та визначає метод cost, 
який також викликає метод cost в базовому компоненті.

MilkDecorator і SugarDecorator - це конкретні декоратори, 
які успадковуються від CoffeeDecorator. 
Кожен декоратор додає певну функціональність до базового компонента.

У прикладі використання ми створюємо об'єкт Coffee, 
а потім обгортаємо його у декоратори MilkDecorator та SugarDecorator, 
додавши до нього функціональність молока та цукру. 
Кожен декоратор додає свій внесок до вартості кави.

Цей приклад демонструє використання патерну Decorator 
для динамічного додавання функціональності до об'єктів.

"""