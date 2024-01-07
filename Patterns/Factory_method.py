# Цей приклад ілюструє використання патерну Фабричний метод
# для створення різних видів транспортних засобів.


# Створюємо базовий клас для абстрактного продукту
# class Product:
#     def operation(self):
#         pass
#
#
# # Створюємо конкретні класи продуктів
# class ConcreteProduct1(Product):
#     def operation(self):
#         return "ConcreteProduct1"
#
#
# class ConcreteProduct2(Product):
#     def operation(self):
#         return "ConcreteProduct2"
#
#
# # Створюємо інтерфейс Фабрики
# class Creator:
#     def factory_method(self):
#         pass
#
#     def create_product(self):
#         pass
#
#     def operation(self):
#         product = self.factory_method()
#         result = f"Creator: Створено продукт - {product.operation()}"
#         return result
#
#
# # Реализуем конкретные фабрики
# class ConcreteCreator1(Creator):
#     def factory_method(self):
#         print('Створюємо ПЕРШИЙ продукт')
#         return ConcreteProduct1()
#
#
# class ConcreteCreator2(Creator):
#     def factory_method(self):
#         print('Створюємо Другий продукт')
#         return ConcreteProduct2()
#
#
# # Інтерфейс використання функції створення -> create(ConcreteCreator1())
# def create(creator):
#     print(creator.operation())
#
#
# # Пример использования
# if __name__ == "__main__":
#     print("Client: Тестуємо ConcreteCreator1")
#     create(ConcreteCreator1())
#
#     print("\nClient: Тестуємо ConcreteCreator2")
#     create(ConcreteCreator2())


# ============= Фабричний метод створення Автомобіля, Вантажівки та Велосипеду ====
#
# Абстрактний клас для транспортного засобу
class Transport:
    def deliver(self):
        pass


# Класи конкретних транспортних засобів
class Car(Transport):
    def deliver(self):
        return "Delivering by car"


class Truck(Transport):
    def deliver(self):
        return "Delivering by truck"


class Bicycle(Transport):
    def deliver(self):
        return "Delivering by bicycle"


class Boat(Transport):
    def deliver(self):
        return 'Delivering by boat'


# Абстрактний клас фабрики
class TransportFactory:
    def create_transport(self):
        pass


# Класи конкретних фабрик
class CarFactory(TransportFactory):
    def create_transport(self):
        return Car()


class TruckFactory(TransportFactory):
    def create_transport(self):
        return Truck()


class BicycleFactory(TransportFactory):
    def create_transport(self):
        return Bicycle()


class BoatFactory(TransportFactory):
    def create_transport(self):
        return Boat()


# Приклад використання
if __name__ == "__main__":

    car_factory = CarFactory()
    car = car_factory.create_transport()
    # print(car.deliver())

    truck_factory = TruckFactory()
    truck = truck_factory.create_transport()
    # print(truck.deliver())

    bicycle_factory = BicycleFactory()
    bicycle = bicycle_factory.create_transport()
    # print(bicycle.deliver())

    boat_factory = BoatFactory()
    boat = boat_factory.create_transport()

    transports = [car, boat, boat, bicycle, truck, bicycle, boat]

    for tr in transports:
        print(tr.deliver())

"""
У цьому прикладі маємо абстрактний клас Transport, 
який визначає метод deliver, а також конкретні класи Car, 
Truck і Bicycle, які успадковуються від Transport 
і реалізують власний метод deliver.

TransportFactory є абстрактною фабрикою, 
яка має метод create_transport для створення об'єкта транспорту.

CarFactory, TruckFactory і BicycleFactory є конкретними фабриками, 
які успадковуються від TransportFactory 
і реалізують метод create_transport для створення відповідного виду транспорту.

У прикладі використання ми створюємо об'єкти фабрик 
для кожного виду транспорту і викликаємо їх методи create_transport 
для створення об'єктів. Потім викликаємо метод deliver 
для кожного створеного транспорту, щоб отримати повідомлення про доставку.


"""