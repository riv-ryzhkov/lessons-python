"""
Паттерн "Visitor" (Відвідувач) - це паттерн проектування,
який дозволяє додавати нові операції до об'єктів без зміни їхньої структури.
Він розділяє алгоритми від структури об'єкту,
дозволяючи створювати нові операції, не змінюючи класи об'єктів,
які підлягають обробці.

Основна ідея полягає в тому, що ми маємо два основних компоненти:

Елементи (Elements):
Це класи об'єктів, які можуть бути відвідані (піддані операції).
Вони повинні визначити метод accept,
який приймає об'єкт відвідувача і дозволяє відвідувачу взаємодіяти з цим об'єктом.

Відвідувачі (Visitors):
Це класи, які реалізують конкретні операції або алгоритми,
які мають бути виконані над об'єктами.
Вони повинні визначити методи для обробки кожного типу елементів,
які вони відвідують.

Припустимо, ми маємо ієрархію геометричних фігур (коло, квадрат, трикутник)
і хочемо реалізувати функціональність обчислення площі кожної фігури
без зміни їхніх класів.
"""


# Базовий клас елементу (фігури)
class Shape:
    def accept(self, visitor):
        pass


# Конкретні класи елементів (фігур)
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def accept(self, visitor):
        visitor.visit_circle(self)


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def accept(self, visitor):
        visitor.visit_square(self)



# Базовий клас відвідувача
class Visitor:
    def visit_circle(self, circle):
        pass

    def visit_square(self, square):
        pass


# Конкретний відвідувач для обчислення площі
class AreaCalculator(Visitor):
    def __init__(self):
        self.total_area = 0

    def visit_circle(self, circle):
        area = 3.14 * circle.radius * circle.radius
        self.total_area += area

    def visit_square(self, square):
        area = square.side ** 2
        self.total_area += area


# Приклад використання
if __name__ == "__main__":
    shapes = [Circle(5), Square(4), Circle(6.56), Square(6)]

    calculator = AreaCalculator()

    for shape in shapes:
        shape.accept(calculator)

    print("Total Area:", calculator.total_area)
    # print("Total Perimeter:", calculator.total_perimeter)
