# # Клас ітератора
# class Iterator:
#     def __init__(self, collection):
#         self.collection = collection
#         self.index = 0
#
#     def has_next(self):
#         return self.index < len(self.collection)
#
#     def next(self):
#         if self.has_next():
#             item = self.collection[self.index]
#             self.index += 1
#             return item
#         else:
#             raise StopIteration()
#
#
# # Колекція, для якої створюється ітератор
# class Collection:
#     def __init__(self):
#         self.items = []
#
#     def add_item(self, item):
#         self.items.append(item)
#
#     def __iter__(self):
#         return Iterator(self.items)
#
#
#
# # Приклад використання
# if __name__ == "__main__":
#     collection = Collection()
#     collection.add_item("Item 1")
#     collection.add_item("Item 2")
#     collection.add_item("Item 3")
#     collection.add_item(789.89)
#     collection.add_item(34)
#     collection.add_item([1, 2, 3, 4])
#     collection.add_item((13, 25, 36, 48))
#     collection.add_item({'key': 'value'})
#
#     print('Друкуємо через Next()')
#     iterator = collection.__iter__()
#
#     # while True:
#     #     try:
#     #         item = iterator.next()
#     #         print(item)
#     #     except StopIteration:
#     #         break
#     # print('.' * 80)
#
#     for el in range(len(collection.items)):
#     # for el in range(5):
#         try:
#             item = iterator.next()
#             print(item)
#         except StopIteration:
#             break
#     print('.' * 80)

"""
Патерн "Ітератор" дозволяє отримувати послідовний доступ 
до елементів складної колекції, не розкриваючи її внутрішньої структури.

У цьому прикладі є клас Iterator, який визначає інтерфейс для ітератора. 
Кожен ітератор містить посилання на колекцію, для якої він призначений, 
та показник поточного елемента. 
Він надає методи для перевірки наявності наступного елемента 
та отримання наступного елемента.

Клас Collection є колекцією, для якої створюється ітератор. 
Він має метод add_item, який додає елементи до колекції, 
та переозначає метод __iter__, який повертає об'єкт ітератора.

У прикладі використання ми створюємо об'єкт колекції, 
додаємо до нього елементи і отримуємо об'єкт ітератора 
через виклик collection.__iter__(). 
Потім ми використовуємо цей ітератор для послідовного отримання 
всіх елементів колекції за допомогою iterator.next().

Цей приклад демонструє використання патерну "Ітератор" 
для послідовного доступу до елементів колекції 
без розкриття її внутрішньої структури.
"""


# =============================================
# Приклад створення списку різноманітних завдань
# =============================================

# class Task:
#     def __init__(self, description):
#         self.description = description
#
#
# class TaskList:
#     def __init__(self):
#         self.tasks = []
#
#     def add_task(self, task):
#         self.tasks.append(task)
#
# # Тепер ми хочемо створити ітератор для перебору завдань у цьому списку.
# # Для цього ми створимо окремий клас ітератора:
#
#
# class TaskListIterator:
#     def __init__(self, task_list):
#         self.task_list = task_list
#         self.index = 0
#
#     def has_next(self):
#         return self.index < len(self.task_list.tasks)
#
#     def next(self):
#         if self.has_next():
#             task = self.task_list.tasks[self.index]
#             self.index += 1
#             return task
#         else:
#             raise StopIteration()
#
# # Тепер ми можемо використовувати цей ітератор для перебору завдань у списку:
#
# # task1 = Task("Complete assignment")
# # task2 = Task("Prepare presentation")
# # task3 = Task("Review emails")
# # task4 = Task("Review my emails")
# # task5 = Task("Review my emails for today!")
#
#
# # task1 = Task(2023.12)
# # task2 = Task([1, 2, 3])
# # task3 = Task("Hello, world!")
#
#
# # my_tasks = [
# #     'Have breakfast',
# #     'Review emails',
# #     'Check telegram',
# #     'Do my work',
# #     'Go Home',
# #     'Do something'
# # ]
#
# my_tasks = []
# text = ''
#
# while text != 'exit':
#     text = input('Введіть наступну задачу : ')
#     my_tasks.append(text)
#
#
#
# task_list = TaskList()
#
#
# # task_list.add_task(task1)
# # task_list.add_task(task2)
# # task_list.add_task(task3)
# # task_list.add_task(task4)
# # task_list.add_task(task5)
#
#
# for elem in my_tasks:
#     task_list.add_task(Task(elem))
#
#
#
# # Створимо ітератор для списку завдань
# iterator = TaskListIterator(task_list)
#
# # Перебираємо та виводимо завдання
# while True:
#     try:
#         task = iterator.next()
#         print("Task:", task.description)
#         # print('Виконано!', input('Y/N'))
#     except StopIteration:
#         break
