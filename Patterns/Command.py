"""

Паттерн "Команда" (Command) відноситься до патернів проектування,
які дозволяють інкапсулювати запити або операції як об'єкти.
Він дозволяє розширювати функціональність системи,
робити її більш гнучкою і підтримувати відмінність між викликом операції
та її виконанням.

Основні компоненти паттерна "Команда":

Команда (Command):
Це абстрактний клас або інтерфейс,
що визначає метод виконання (execute) команди.

Конкретна команда (Concrete Command):
Реалізує інтерфейс команди, визначаючи конкретну операцію і об'єкт,
на якому вона буде викликана.

Отримувач (Receiver):
Це об'єкт, на якому виконується дія, що інкапсульована командою.
Він має методи, які будуть викликані під час виконання команди.

Викликач (Invoker):
Викликає команди для виконання. Він не повинен знати,
яка саме команда виконується і як саме вона виконується.

Сполучник (Client):
Створює об'єкти команд, визначає їх отримувачів
і прив'язує команди до викликачів.
"""

#
# # Клас команди
# class Command:
#     def execute(self):
#         pass
#
#
# # Конкретні команди
# class LightOnCommand(Command):
#     def __init__(self, light):
#         self.light = light
#
#     def execute(self):
#         self.light.turn_on()
#
#
# class LightOffCommand(Command):
#     def __init__(self, light):
#         self.light = light
#
#     def execute(self):
#         self.light.turn_off()
#
#
# # Отримувач команд
# class Light:
#     def turn_on(self):
#         print("Light is on")
#
#     def turn_off(self):
#         print("Light is off")
#
#
# # Об'єкт відправника команд
# class RemoteControl:
#     def __init__(self):
#         self.command = None
#
#     def set_command(self, command):
#         self.command = command
#
#     def press_button(self):
#         self.command.execute()
#
#
# # Приклад використання
# if __name__ == "__main__":
#     light = Light()
#
#     light_on = LightOnCommand(light)
#     light_off = LightOffCommand(light)
#
#     remote = RemoteControl()
#
#     remote.set_command(light_on)
#     print('Ready to turn ON!')
#     remote.press_button()
#
#     remote.set_command(light_off)
#     print('Ready to turn OFF!')
#     remote.press_button()


"""
Патерн "Команда" дозволяє інкапсулювати запит у об'єкті команди, 
що дозволяє параметризувати об'єктами операції та чергувати їх виконання.

У цьому прикладі є базовий клас Command, 
від якого успадковуються конкретні команди LightOnCommand та LightOffCommand. 
Кожна команда має посилання на об'єкт відповідального отримувача 
(у цьому випадку, світло) та реалізує метод execute, 
який викликає відповідну операцію на отримувачі.

Клас Light представляє отримувача команди, 
тобто об'єкт, на якому виконується команда.

Клас RemoteControl виступає як відправник команди. 
Він має методи для встановлення команди та виконання дії, пов'язаної з командою.

У прикладі використання ми створюємо об'єкт світла 
та команди для увімкнення та вимкнення. 
Далі створюємо об'єкт відправника команди, 
встановлюємо йому команду для увімкнення світла та натискаємо кнопку. 
Також встановлюємо команду для вимкнення та натискаємо кнопку.

Цей приклад ілюструє використання патерну "Команда" 
для відокремлення відправника та отримувача команди, 
що дозволяє визначити запити як об'єкти, 
а також забезпечує гнучкість в системі через параметризовані операції 
та чергування команд.

"""

# ================================================
# Приклад включення та вимкнення комп'ютера
# ================================================



#
# # Отримувач (Receiver)
# class Computer:
#     _state = 'off'
#
#     def start(self):
#         print("Computer is starting")
#
#     def shutdown(self):
#         print("Computer is shutting down")
#
#
# # Команда (Command)
# class Command:
#     def execute(self):
#         pass
#
#
# # Конкретні команди (Concrete Commands)
# class StartComputerCommand(Command):
#     def __init__(self, computer):
#         self.computer = computer
#
#     def execute(self):
#         if Computer._state == 'off':
#             Computer._state = 'on'
#             self.computer.start()
#
#
# class ShutdownComputerCommand(Command):
#     def __init__(self, computer):
#         self.computer = computer
#
#     def execute(self):
#         if Computer._state == 'on':
#             Computer._state = 'off'
#             self.computer.shutdown()
#
#
# # Викликач (Invoker)
# class User:
#     def __init__(self):
#         self.command = None
#
#     def set_command(self, command):
#         self.command = command
#
#     def execute_action(self):
#         self.command.execute()
#
#
# if __name__ == "__main__":
#     computer = Computer()
#     start_command = StartComputerCommand(computer)
#     shutdown_command = ShutdownComputerCommand(computer)
#
#     user = User()
#
#     user.set_command(start_command)
#     user.execute_action()
#
#     user.set_command(shutdown_command)
#     user.execute_action()
#
#     print('.' * 80)
#
#     actions = [
#         start_command,
#         start_command,
#         start_command,
#         shutdown_command,
#         shutdown_command,
#         shutdown_command,
#         start_command,
#         shutdown_command
#     ]
#
#     for act in actions:
#         user.set_command(act)
#         user.execute_action()
#



"""
У цьому прикладі ми маємо клас Computer як отримувач, 
який може запускати та вимикати комп'ютер. 
Клас Command - абстрактний клас команди.

StartComputerCommand і ShutdownComputerCommand 
- це конкретні команди, які виконують операції запуску 
та вимикання комп'ютера відповідно.

User - викликач, який може встановлювати команду та виконувати її дію.

У сполучнику ми створюємо об'єкти команд, 
встановлюємо їх для виконання і запускаємо ці команди з викликача. 
Це дозволяє виконувати різні дії (команди) на отримувачі (комп'ютері) 
без прив'язки споживача (користувача) до конкретної реалізації цих команд.
"""