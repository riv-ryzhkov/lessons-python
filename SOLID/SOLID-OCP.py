# Open/Closed Principle - OCP

"""

Принцип відкритості/закритості (Open/Closed Principle - OCP) означає,
що класи повинні бути відкриті для розширення (додавання нового функціоналу)
і закриті для модифікації (не потребують змін у вихідному коді для внесення змін).
Основна ідея полягає в тому, що ви можете змінювати поведінку програми,
додавши новий код, а не модифікуючи існуючий.
"""



# Абстрактний клас для фігур
class Shape:
    def area(self):
        pass


# Клас круга
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


# Клас прямокутника
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height



# Клас для обчислення загальної площі фігур
class AreaCalculator:
    @staticmethod
    def calculate_area(shapes):
        total_area = 0
        for shape in shapes:
            total_area += shape.area()
        return total_area


if __name__ == "__main__":
    shapes = [Circle(2), Rectangle(4, 1)]

    total_area = AreaCalculator.calculate_area(shapes)
    print(f"Total area: {total_area}")


"""
В цьому прикладі ми маємо абстрактний клас Shape, 
який містить абстрактний метод area. 
Цей клас є закритим для модифікації, 
але відкритим для розширення.

Ми створюємо два конкретні класи, Circle і Rectangle, 
які розширюють клас Shape і реалізують метод area.

Клас AreaCalculator використовуєся для обчислення загальної площі фігур. 
Він приймає список об'єктів фігур, і ми можемо додавати нові класи фігур, 
не модифікуючи AreaCalculator.

Цей приклад відповідає принципу відкритості/закритості (OCP), 
оскільки ми можемо додавати нові класи фігур, не змінюючи код AreaCalculator.
"""