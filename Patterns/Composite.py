# Компонент - базовий клас
# class Component:
#     def operation(self):
#         pass
#
#
# # Клас Leaf, який представляє листок
# class Leaf(Component):
#     def operation(self):
#         return "Leaf"
#
#
# # Клас Composite, який представляє складний об'єкт, що містить декілька компонентів
# class Composite(Component):
#     def __init__(self):
#         self._children = []
#
#     def add(self, component):
#         self._children.append(component)
#
#     def remove(self, component):
#         self._children.remove(component)
#
#     def operation(self):
#         results = []
#         for child in self._children:
#             results.append(child.operation())
#         return f"Composite [{', '.join(results)}]"
#
#
# # Приклад використання
# if __name__ == "__main__":
#     leaf1 = Leaf()
#     leaf2 = Leaf()
#
#     composite = Composite()
#     composite.add(leaf1)
#     composite.add(leaf2)
#
#     composite_of_composites = Composite()
#     composite_of_composites.add(leaf1)
#     composite_of_composites.add(composite)
#
#     print("Leaf 1:", leaf1.operation())
#     print("Leaf 2:", leaf2.operation())
#     print("Composite:", composite.operation())
#     print("Composite of Composites:", composite_of_composites.operation())


# # ===== Приклад з коробками та фруктами в них для 3 рівней. Обчислення ваги. ====
#
# Компонент - базовий клас
# class Component:
#     def get_weight(self):
#         pass
#
#
# # Клас Leaf, який представляє товар
# class Product(Component):
#     def __init__(self, name, weight):
#         self._name = name
#         self._weight = weight
#
#     def get_weight(self):
#         return self._weight
#
#
# # Клас Composite, який представляє коробку, яка може містити товари та інші коробки
# class Box(Component):
#     def __init__(self, name):
#         self._name = name
#         self._children = []
#
#     def add(self, component):
#         self._children.append(component)
#
#     def get_weight(self):
#         total_weight = 0
#         for child in self._children:
#             total_weight += child.get_weight()
#         return total_weight
#
#
# # Приклад використання
# if __name__ == "__main__":
#     apple = Product("Apple", 0.1)
#     orange = Product("Orange", 0.15)
#
#     small_box1 = Box("Small Box1")
#     small_box1.add(apple)
#     small_box1.add(apple)
#     small_box1.add(orange)
#
#
#     big_box1 = Box("Big Box1")
#     big_box1.add(small_box1)
#     big_box1.add(orange)
#     big_box1.add(apple)
#
#     print("Apple weight:", apple.get_weight())
#     print("Orange weight:", orange.get_weight())
#     print("Small Box1 weight:", small_box1.get_weight())
#     print("Big Box1 weight:", big_box1.get_weight())



    # print("Big Box2 weight: {:7.1f}".format(big_box2.get_weight()))


"""
У цьому прикладі є базовий клас Component, який визначає метод get_weight.

Клас Product є листком у ієрархії, який представляє товар. 
Кожний товар має ім'я та вагу.

Клас Box представляє коробку, яка може містити товари або інші коробки. 
Він також успадковує від Component та має метод add 
для додавання компонентів (товарів або інших коробок).

У прикладі використання ми створюємо об'єкти Product для товарів (які є листками) 
та об'єкти Box для коробок (які є композитами). 
Додаємо товари до коробок, 
створюємо ієрархію коробок включаючи великі коробки з меншими.

Потім викликаємо метод get_weight для різних об'єктів, 
щоб отримати загальну вагу кожного компонента у ієрархії.

Цей приклад ілюструє використання патерну Composite 
для побудови ієрархії об'єктів, де об'єкти можуть бути листками (товари) 
або композитами (коробки), 
і здатні обчислювати агреговані значення, такі як загальна вага.
"""