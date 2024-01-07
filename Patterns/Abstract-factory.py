
# Абстрактні класи продуктів
# class AbstractProductA:
#     def operation(self):
#         pass
#
#
# class AbstractProductB:
#     def operation(self):
#         pass
#
#
# # Конкретні класи продуктів, що належать до групи A
# class ConcreteProductA1(AbstractProductA):
#     def operation(self):
#         return "ConcreteProductA1"
#
#
# class ConcreteProductA2(AbstractProductA):
#     def operation(self):
#         return "ConcreteProductA2"
#
#
# # Конкретні класи продуктів, що належать до групи B
# class ConcreteProductB1(AbstractProductB):
#     def operation(self):
#         return "ConcreteProductB1"
#
#
# class ConcreteProductB2(AbstractProductB):
#     def operation(self):
#         return "ConcreteProductB2"
#
#
# # Абстрактна фабрика
# class AbstractFactory:
#     def create_product_a(self):
#         pass
#
#     def create_product_b(self):
#         pass
#
#
# # Конкретні фабрики, які створюють продукти своєї групи
# class ConcreteFactory1(AbstractFactory):
#     def create_product_a(self):
#         return ConcreteProductA1()
#
#     def create_product_b(self):
#         return ConcreteProductB1()
#
#
# class ConcreteFactory2(AbstractFactory):
#     def create_product_a(self):
#         return ConcreteProductA2()
#
#     def create_product_b(self):
#         return ConcreteProductB2()
#
#
# # Приклад використання
# if __name__ == "__main__":
#     factory1 = ConcreteFactory1()
#     productA1 = factory1.create_product_a()
#     productB1 = factory1.create_product_b()
#
#     print(productA1.operation())
#     print(productB1.operation())
#
#     factory2 = ConcreteFactory2()
#     productA2 = factory2.create_product_a()
#     productB2 = factory2.create_product_b()
#
#     print(productA2.operation())
#     print(productB2.operation())


"""
Приклад:
створюємо крісла(1) та диван(2)
в стилі модерн(А) чи класика(В).

Тобто створюємо продукт А1 чи А2 чи В1 чи В2.
"""



"""
Патерн Абстрактна фабрика дозволяє створювати сімейства пов'язаних продуктів 
без вказування конкретних класів продуктів. 
Він визначає інтерфейси для створення кількох продуктів, 
які належать до однієї сім'ї, 
тобто групи взаємодіючих або залежних продуктів.

У цьому прикладі є абстрактні класи AbstractProductA і AbstractProductB, 
які представляють групи продуктів A і B відповідно. 
Конкретні класи ConcreteProductA1, ConcreteProductA2, ConcreteProductB1 і ConcreteProductB2
наслідуються від цих абстрактних продуктів.

AbstractFactory є абстрактною фабрикою з методами create_product_a 
та create_product_b, які повинні бути реалізовані в конкретних фабриках. 
Класи ConcreteFactory1 і ConcreteFactory2 реалізують ці методи, 
створюючи конкретні продукти своєї групи.

У прикладі використання ми створюємо об'єкти ConcreteFactory1 та ConcreteFactory2, 
і використовуємо їх для створення продуктів AbstractProductA та AbstractProductB. 
Кожен продукт може бути створений за допомогою відповідної фабрики.
"""

# ======= Приклад: крісло та диван, класика та модерн ========
# Абстрактні класи меблів
class Chair:
    def sit(self):
        pass


class Sofa:
    def relax(self):
        pass



# Класи меблів у стилі модерн
class ModernChair(Chair):
    def sit(self):
        return "Sitting on a modern chair"


class ModernSofa(Sofa):
    def relax(self):
        return "Relaxing on a modern sofa"


# Класи меблів у стилі класика
class ClassicChair(Chair):
    def sit(self):
        return "Sitting on a classic chair"


class ClassicSofa(Sofa):
    def relax(self):
        return "Relaxing on a classic sofa"


# Абстрактна фабрика меблів
class FurnitureFactory:
    def create_chair(self):
        pass

    def create_sofa(self):
        pass

# Фабрика меблів у стилі модерн
class ModernFurnitureFactory(FurnitureFactory):
    def create_chair(self):
        return ModernChair()

    def create_sofa(self):
        return ModernSofa()

# Фабрика меблів у стилі класика
class ClassicFurnitureFactory(FurnitureFactory):
    def create_chair(self):
        return ClassicChair()

    def create_sofa(self):
        return ClassicSofa()

# Приклад використання
if __name__ == "__main__":
    modern_factory = ModernFurnitureFactory()
    modern_chair = modern_factory.create_chair()
    modern_sofa = modern_factory.create_sofa()

    print("Modern:", modern_chair.sit())
    print("Modern:", modern_sofa.relax())

    classic_factory = ClassicFurnitureFactory()
    classic_chair = classic_factory.create_chair()
    classic_sofa = classic_factory.create_sofa()

    print("Classic:", classic_chair.sit())
    print("Classic:", classic_sofa.relax())


