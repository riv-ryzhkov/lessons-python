"""
Патерн Observer (спостерігач) - це патерн проектування,
який використовується для встановлення залежностей між об'єктами так,
що коли один об'єкт змінює свій стан,
всі його залежні об'єкти автоматично сповіщаються і оновлюються.
Цей патерн використовується для реалізації подійної моделі в програмуванні.
"""

# Клас Суб'єкту (Спостерігаємого об'єкта)
class Subject:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, message):
        for observer in self._observers:
            observer.update(message)


# Клас Спостерігача
class Observer:
    def update(self, message):
        pass


# Конкретні реалізації спостерігачів
class ConcreteObserver1(Observer):
    def update(self, message):
        print(f"Observer 1 received message: {message}")


class ConcreteObserver2(Observer):
    def update(self, message):
        print(f"Observer 2 received message: {message}")


class ConcreteObserver3(Observer):
    def update(self, message):
        if message == 'Hello, Ukraine!':
            print(f"Observer 3 answers message: Hello, heros!")
        else:
            print(f"Observer 3 received message: {message}")


# Приклад використання
if __name__ == "__main__":
    subject = Subject()

    observer1 = ConcreteObserver1()
    observer2 = ConcreteObserver2()
    observer3 = ConcreteObserver3()

    subject.add_observer(observer1)
    subject.add_observer(observer2)
    subject.add_observer(observer3)

    message = "Hello, observers!"
    print('Subject tell :', message)

    subject.notify_observers(message)

    message = "Hello, Ukraine!"
    print('Subject tell :', message)

    subject.notify_observers(message)

"""
Основні компоненти паттерна Observer:

Subject (Суб'єкт):
Це об'єкт, який спостерігає за змінами і володіє списком своїх спостерігачів.
Суб'єкт може додавати, видаляти та сповіщати спостерігачів про зміни.

Observer (Спостерігач):
Це об'єкт, який очікує на сповіщення від суб'єкта і реагує на них.
Спостерігачі реалізують певний інтерфейс
або мають певний метод для отримання оновлень від суб'єкта.
"""

# =========================================================
# Приклад спостерігання за Фондовим ринком
# =========================================================

# Клас Спостерігаємого об'єкта - Фондового ринку
# class StockMarket:
#     def __init__(self):
#         self._observers = []
#         self._stock_price = None
#
#     def add_observer(self, observer):
#         self._observers.append(observer)
#
#     def remove_observer(self, observer):
#         print(observer.name, 'is removed!')
#         self._observers.remove(observer)
#
#     def set_stock_price(self, price):
#         self._stock_price = price
#         self.notify_observers()
#
#     def notify_observers(self):
#         for observer in self._observers:
#             observer.update(self._stock_price)
#
#
# # Клас Спостерігача - Інвестора
# class Investor:
#     def __init__(self, name):
#         self.name = name
#
#     def update(self, stock_price):
#         print(f"Investor {self.name} received stock price update: ${stock_price}")
#
#
# # Приклад використання
# if __name__ == "__main__":
#     stock_market1 = StockMarket()
#
#     investor1 = Investor("John")
#     investor2 = Investor("Alice")
#     investor3 = Investor("Bob")
#
#     stock_market1.add_observer(investor1)
#     stock_market1.add_observer(investor2)
#     stock_market1.add_observer(investor3)
#
#     stock_market1.set_stock_price(100)
#     print('.' * 80)
#     stock_market1.set_stock_price(105)
#     print('.' * 80)
#     stock_market1.remove_observer(investor3)
#     # stock_market1.notify_observers()
#     print('.' * 80)
#     stock_market1.set_stock_price(150)
