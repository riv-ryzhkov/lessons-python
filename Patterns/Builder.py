# Клас продукту
# class Product:
#     def __init__(self):
#         self.parts = []
#
#     def add_part(self, part):
#         self.parts.append(part)
#
#     def list_parts(self):
#         return ', '.join(self.parts)
#
#
# # Інтерфейс будівельника
# class Builder:
#     def build_part_a(self):
#         pass
#
#     def build_part_b(self):
#         pass
#
#     def build_part_c(self):
#         pass
#
#     def get_product(self):
#         pass
#
#
# # Конкретний будівельник
# class ConcreteBuilder(Builder):
#     def __init__(self):
#         self.product = Product()
#
#     def build_part_a(self):
#         self.product.add_part("Part A")
#
#     def build_part_b(self):
#         self.product.add_part("Part B")
#
#     def build_part_c(self):
#         self.product.add_part("Part C")
#
#     def get_product(self):
#         return self.product
#
#
# # Архітектор
# class Architect:
#     def __init__(self, builder):
#         self.builder = builder
#
#     # Варіанти будівництва А -> B -> C
#     def construct1(self):
#         self.builder.build_part_a()
#         self.builder.build_part_b()
#         self.builder.build_part_c()
#
#     # Варіанти будівництва C -> B -> A
#     def construct2(self):
#         self.builder.build_part_c()
#         self.builder.build_part_b()
#         self.builder.build_part_a()
#
#
#
# # Приклад використання
# if __name__ == "__main__":
#     builder1 = ConcreteBuilder()
#     builder2 = ConcreteBuilder()
#     client1 = Architect(builder1)
#     client2 = Architect(builder2)
#
#
#     client1.construct1()
#     client2.construct2()
#     product1 = builder1.get_product()
#     product2 = builder2.get_product()
#
#     print("Product1 parts:", product1.list_parts())
#     print("Product2 parts:", product2.list_parts())


"""
Патерн Будівельник використовується для створення складних об'єктів крок за кроком. 
У цій програмі ми маємо клас Product, який представляє об'єкт, який ми будуємо. 
Клас Builder визначає інтерфейс для будівельників, 
які повинні реалізувати методи для побудови частин об'єкта.

ConcreteBuilder є конкретною реалізацією будівельника, 
яка створює об'єкт Product і додає до нього частини. 
Клас Architect визначає порядок будівництва об'єкта 
і використовує заданий будівельник для його створення.

У прикладі використання ми створюємо ConcreteBuilder, 
передаємо його в Architect, викликаємо метод construct для побудови об'єкта 
крок за кроком, і, нарешті, отримуємо готовий об'єкт Product 
за допомогою builder.get_product() і виводимо його частини.

Патерн Будівельник дозволяє відділити процес створення складного об'єкта 
від його представлення, що робить код більш читабельним і зручним для редагування.
"""


# ================ Будівництво Будинку ================

# Клас, який представляє будинок
class House:
    def __init__(self):
        self.foundation = 'W/O foundation'
        self.structure = 'W/O structure'
        self.roof = 'W/O roof'

    def __str__(self):
        return f"House with {self.foundation}, {self.structure}, and {self.roof}"


# Абстрактний Будівельник
class HouseBuilder:
    def build_foundation(self):
        pass

    def build_structure(self):
        pass

    def build_roof(self):
        pass

    def get_house(self):
        pass

# Конкретний будівельник
class ConcreteHouseBuilder(HouseBuilder):
    def __init__(self):
        self.house = House()

    def build_foundation(self):
        self.house.foundation = "Concrete Foundation"

    def build_structure(self):
        self.house.structure = "Concrete Structure"

    def build_roof(self):
        self.house.roof = "Concrete Roof"

    def get_house(self):
        return self.house


# Директор, який керує будівництвом
class Director:
    def __init__(self, builder):
        self.builder = builder

    def construct_house1(self):
        self.builder.build_foundation()
        self.builder.build_structure()
        self.builder.build_roof()

    def construct_house2(self):
        self.builder.build_structure()
        self.builder.build_roof()

    # def construct_house3(self):
    #     self.builder.build_foundation()
    #     self.builder.build_structure()


# Приклад використання
if __name__ == "__main__":
    concrete_builder1 = ConcreteHouseBuilder()
    concrete_builder2 = ConcreteHouseBuilder()

    director1 = Director(concrete_builder1)
    director2 = Director(concrete_builder2)

    # constr = input('Оберіть номер конструкції (1/2/3) :')
    # if constr == '1':
    #     director1.construct_house1()
    # elif constr == '2':
    #     director1.construct_house2()
    # else:
    #     director1.construct_house3()


    director1.construct_house1()
    director2.construct_house3()

    house1 = concrete_builder1.get_house()
    house2 = concrete_builder2.get_house()

    print(house1)
    # print(house2)
