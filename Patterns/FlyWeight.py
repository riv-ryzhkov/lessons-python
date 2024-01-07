# Клас Легковаг
class CoffeeFlavor:  # Смак кофе
    def __init__(self, flavor_name):
        self._flavor_name = flavor_name

    def get_flavor(self):
        return self._flavor_name

    def __repr__(self):
        return self._flavor_name


# Фабрика Легковагів
class CoffeeFlavorFactory:
    _flavors = {}

    def get_flavor(self, flavor_name):
        if flavor_name not in self._flavors:
            self._flavors[flavor_name] = CoffeeFlavor(flavor_name)
        return self._flavors[flavor_name]


# Приклад використання
if __name__ == "__main__":
    flavor_factory = CoffeeFlavorFactory()

    orders = [
        ("Cappuccino", 101),
        ("Espresso", 102),
        ("Cappuccino", 103),
        ("Espresso", 104),
        ("Espresso", 104),
        ("Cappuccino", 105),
        # ('Americano', 109),
        # ('Americano', 110),
        # ('Americano', 110),
    ]

    for order in orders:
        flavor = flavor_factory.get_flavor(order[0])
        print(f"Serving {flavor.get_flavor()} to table {order[1]}")

print(CoffeeFlavorFactory._flavors)


"""
Патерн Легковес призначений для ефективного використання пам'яті, 
коли потрібно створити велику кількість об'єктів з великою кількістю спільних даних.

У цьому прикладі клас CoffeeFlavor представляє легковес, 
який містить дані про смак кави. 
Кожен об'єкт CoffeeFlavor зберігає тільки інформацію про конкретний смак кави.

Клас CoffeeFlavorFactory є фабрикою для легковесів. 
Він зберігає пул об'єктів CoffeeFlavor 
та повертає наявний об'єкт з пула, якщо він вже був створений, 
або створює новий, якщо такого об'єкта ще немає.

У прикладі використання ми створюємо фабрику CoffeeFlavorFactory 
та робимо замовлення на каву. 
Кожне замовлення містить назву смаку та номер столика. 
Фабрика використовує пул об'єктів CoffeeFlavor 
для забезпечення ефективного використання пам'яті.

Цей приклад демонструє використання патерну Легковес 
для ефективного управління об'єктами 
зі спільними даними та уникнення зайвого дублювання об'єктів в пам'яті.
"""