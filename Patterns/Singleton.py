import copy


class Singleton:
    _instance = None

    def __new__(cls):  # метод __new__ створює об'єкт класу!
        if cls._instance is None:
            # Тут ми викликаєм вбудований метод __new__(cls) з батьківського
            # класу Object
            # cls._instance = super(Singleton, cls).__new__(cls)
            cls._instance = super().__new__(cls)
            cls._instance.value = None  # додає атрибут value
        return cls._instance

# """
# Зверніть увагу на те, що створюється лише один(!) об'єкт класу без ім'я.
# Тому функція створення __init__() відсутня!
# """


    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value


# Приклад використання
if __name__ == "__main__":
    singleton1 = Singleton()
    singleton1.set_value("Hello from Singleton 1")
    print('singleton1 ->', id(singleton1))

    singleton2 = Singleton()
    print('singleton2 ->', id(singleton2))
    print(singleton2.get_value())  # Виведе "Hello from Singleton 1"


    # singleton3 = copy.copy(singleton1)
    singleton3 = copy.deepcopy(singleton1)
    print('singleton3 ->', id(singleton3))
    print('singleton3.get_value()', singleton3.get_value())  # Виведе "Hello from Singleton 1"

    print('singleton2 is singleton1', singleton2 is singleton1)
    print('singleton3 is singleton1', singleton3 is singleton1)

    # singleton2.set_value("Hello from Singleton 2")
    #
    # list_ = [singleton1, singleton2, singleton3]
    #
    # for el in list_:
    #     print(el.get_value())



'''
Патерн Singleton дозволяє забезпечити те, 
що в класі буде створений лише один єдиний екземпляр, 
і надає глобальну точку доступу до цього екземпляра.

У даній програмі є клас Singleton, 
в якому маємо приватний статичний атрибут _instance, 
який буде містити єдиний екземпляр класу. 
Метод __new__ перевіряє, чи _instance вже існує, 
і якщо ні, то створює новий екземпляр 
і зберігає його у _instance. 
Якщо ж _instance вже існує, повертається існуючий екземпляр.

Функції set_value і get_value дозволяють встановлювати 
і отримувати значення в екземплярі класу.

У прикладі використання ми створюємо два екземпляри класу Singleton. 
Перший екземпляр встановлює значення "Hello from Singleton 1", 
а другий отримує це значення і виводить його. 
Як бачимо, обидва екземпляри вказують на один і той же об'єкт, 
оскільки патерн Singleton гарантує, що клас має лише один екземпляр.
'''