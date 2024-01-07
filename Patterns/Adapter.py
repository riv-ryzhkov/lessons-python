# Існуючий клас (клас, який буде адаптований)
# class Adaptee:
#     def specific_request(self):
#         return "Adaptee's specific request"
#
#
# # Інтерфейс для адаптера
# class Target:
#     def request(self):
#         pass
#
#
# # Клас адаптера, який використовує композицію для адаптації
# class Adapter(Target):
#     def __init__(self, adaptee):
#         self._adaptee = adaptee
#
#     def request(self):
#         return f"Adapter: {self._adaptee.specific_request()}. Done."
#
#
# # Приклад використання
# if __name__ == "__main__":
#     adaptee = Adaptee()
#     adapter = Adapter(adaptee)
#
#     print("Adaptee:", adaptee.specific_request())
#     print("Adapter:", adapter.request())


"""
Патерн Адаптер дозволяє забезпечити взаємодію між класами з несумісними інтерфейсами, 
шляхом створення проміжного об'єкта-адаптера, 
який перетворює інтерфейс одного класу на інтерфейс іншого.

У цьому прикладі маємо клас Adaptee, 
який має свій власний метод specific_request, 
який ми хотіли б використовувати через інтерфейс Target. 
Клас Target описує інтерфейс, 
який ми хочемо використовувати для взаємодії.

Adapter - це клас адаптера, який реалізує інтерфейс Target, 
але використовує композицію з об'єктом Adaptee 
для перетворення викликів інтерфейсу Target на виклики інтерфейсу Adaptee.

У прикладі використання ми створюємо об'єкт Adaptee 
і викликаємо його метод specific_request. 
Потім ми створюємо об'єкт Adapter, який викликає метод request, 
який перетворює виклик на метод specific_request об'єкта Adaptee.

Таким чином, ми використовуємо патерн Адаптер, 
щоб забезпечити взаємодію між існуючим класом Adaptee 
і очікуваним інтерфейсом Target.
"""


#  =============== DIC -> JSON ===================

# import json
#
#
# # Клас, який має інтерфейс, сумісний з JSON
# class JSONAdapter:
#     def __init__(self, dictionary):
#         self.dictionary = dictionary
#
#     def to_json(self):
#         return json.dumps(self.dictionary)
#
#
# # Словник, який ми хочемо перетворити в JSON
# data = {
#     "name": "John",
#     "age": 30,
#     "city": "New York",
#     777: 999
# }
#
# # Використання адаптера для перетворення в JSON
# json_adapter = JSONAdapter(data)
# json_data = json_adapter.to_json()
#
# print("Original Data:", data)
# print("JSON Data:", json_data)
#





#  =============== DIC -> JSON -> DIC ===================
import json


# Існуючий клас (клас, який буде адаптований)
class DictionaryAdapter:
    def __init__(self, dictionary={}):
        self._dictionary = dictionary

    def to_json(self):
        return json.dumps(self._dictionary)

    def from_json(self, json_string):
        self._dictionary = json.loads(json_string)


# Приклад використання
if __name__ == "__main__":

    original_dict = {
        "key1": "value1",
        777: 999,
        None: 3.14159
    }

    print('Original Dictionary:', original_dict)

    # Застосовуємо адаптер для перетворення словника в JSON
    adapter = DictionaryAdapter(original_dict)
    json_data = adapter.to_json()
    print("Dictionary to JSON:", json_data)

    # Застосовуємо адаптер для перетворення JSON назад у словник
    new_adapter = DictionaryAdapter()
    new_adapter.from_json(json_data)
    # adapter.from_json(json_data)
    new_dict = new_adapter._dictionary
    # new_dict = adapter._dictionary
    dict = adapter._dictionary

    print("JSON to Dictionary:", new_dict)
    print("JSON to Dictionary:", dict)

"""
У цьому прикладі маємо клас DictionaryAdapter, 
який адаптує роботу зі словниками, дозволяючи їх перетворювати в формат JSON 
та навпаки. Метод to_json перетворює словник на рядок JSON 
за допомогою json.dumps(), а метод from_json перетворює рядок JSON 
на словник за допомогою json.loads().

У прикладі використання ми спочатку створюємо словник original_dict. 
Застосовуємо адаптер для перетворення цього словника в формат JSON, 
і виводимо результат. Потім знову застосовуємо адаптер для перетворення 
JSON назад у словник і виводимо новий словник.

Таким чином, патерн Адаптер допомагає адаптувати існуючий клас DictionaryAdapter 
для роботи зі словниками, які можуть бути перетворені в JSON та зворотньо.


"""