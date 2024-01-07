"""
Паттерн "State" (Стан) дозволяє об'єкту змінювати свою поведінку
в залежності від свого стану.
Він перетворює кожен стан об'єкта в окремий клас
і дозволяє об'єкту змінювати свій стан в процесі виконання програми.
Цей паттерн допомагає вирішити проблему великої кількості умовних операторів,
які визначають поведінку об'єкта в різних станах.

Основні учасники паттерна State:

Контекст (Context):
Це клас, який має змінний стан і співпрацює з об'єктом-станом для виконання дій.

Стан (State):
Абстрактний клас або інтерфейс, який визначає методи,
що представляють різні стани об'єкта.

Конкретні стани (Concrete States):
Кожен конкретний стан є реалізацією абстрактного класу стану
і визначає конкретну поведінку об'єкта в цьому стані.
"""

# # Абстрактний клас для стану
# class State:
#     def go(self):
#         pass
#
#
# # Конкретні стани
# class RedLightState(State):
#     def go(self):
#         return "Stop"
#
#
# class GreenLightState(State):
#     def go(self):
#         return "Go"
#
#
# class YellowLightState(State):
#     def go(self):
#         return "Slow down"
#
#
# # Клас світлофора, який визначає стан та взаємодіє з ним
# class TrafficLight:
#     def __init__(self):
#         self.state = RedLightState()
#
#     def change_state(self, state):
#         self.state = state
#
#     def move(self):
#         return self.state.go()
#
#
# # Приклад використання
# import time
#
# if __name__ == "__main__":
#     red = RedLightState()
#     yellow = YellowLightState()
#     green = GreenLightState()
#
#     traffic_light = TrafficLight()
#     print(traffic_light.move())  # Stop
#
#     traffic_light.change_state(yellow)
#     print(traffic_light.move())  # Slow down
#
#     traffic_light.change_state(green)
#     print(traffic_light.move())  # Go
#
#     traffic_light.change_state(red)
#     print(traffic_light.move())  # Stop
#
#     print('.' * 80)
#     print('Trafic')
#     print('.' * 80)
#
#     work = [red, yellow, green, red, yellow, green, red]
#
#     for light in work:
#         traffic_light.change_state(light)
#         print(traffic_light.move())
#     print('.' * 80)
#
#
#     command = red
#     while True:
#         traffic_light.change_state(command)
#         print(traffic_light.move())
#
#         if command == red:
#             command = yellow
#             time.sleep(2)
#
#         elif command == yellow:
#             command = green
#             time.sleep(.5)
#
#         else:
#             command = red
#             time.sleep(3)
#
#         print('.' * 80)




"""
У цьому прикладі TrafficLight - це контекст, 
який може змінювати свій стан. 
Кожен стан (червоний, жовтий, зелений) представлений окремим класом, 
який реалізує метод go() для визначення поведінки світлофора в даному стані.

Під час виконання програми, 
світлофор може змінювати свій стан відповідно до поточного стану 
і виводити відповідне повідомлення про дії, 
які повинні бути виконані у цьому стані.
"""

# ===============================================
# Приклад використання паттерну "State".
# Система керування дверима,
# які можуть знаходитися в різних станах:
# відкрита, закрита, заблокована тощо.
# ===============================================


# # Абстрактний клас для стану дверей
# class DoorState:
#     def open(self):
#         pass
#
#     def close(self):
#         pass
#
#     def lock(self):
#         pass
#
#     def unlock(self):
#         pass
#
#
# # Конкретні стани дверей
# class OpenDoorState(DoorState):
#     def close(self):
#         return "Closing the door"
#
#     def lock(self):
#         return "Can't lock an open door"
#
#     def unlock(self):
#         return "Unlocking the door"
#
#
# class ClosedDoorState(DoorState):
#     def open(self):
#         return "Opening the door"
#
#     def lock(self):
#         return "Locking the door"
#
#     def unlock(self):
#         return "Unlocking the closed door"
#
#     def close(self):
#         return 'Already closed)))))'
#
#
# class LockedDoorState(DoorState):
#     def open(self):
#         return "Can't open a locked door"
#
#     def close(self):
#         return "Can't close a locked door"
#
#     def unlock(self):
#         return "Unlocking the door"
#
#
# # Клас дверей, який визначає стан та взаємодіє з ним
# class Door:
#     def __init__(self):
#         self.state = ClosedDoorState()
#
#     def change_state(self, state):
#         self.state = state
#
#     def open(self):
#         return self.state.open()
#
#     def close(self):
#         return self.state.close()
#
#     def lock(self):
#         return self.state.lock()
#
#     def unlock(self):
#         return self.state.unlock()


# Приклад використання
if __name__ == "__main__":
    door = Door()
    # print(str(type(door.state))[17:27])
    print(door.open())    # Opening the door
    print(door.lock())    # Locking the door
    print(door.unlock())  # Unlocking the door
    print(door.close())   # Closing the door

    door.change_state(LockedDoorState())
    # print(str(type(door.state))[17:27])
    print(door.open())    # Can't open a locked door
    print(door.close())    # Can't close a locked door


# """
# У цьому прикладі ми моделюємо двері,
# які можуть перебувати в різних станах:
# відкриті, закриті та заблоковані.
# Кожен стан представлений окремим класом,
# який реалізує методи для зміни стану та виконання дій у цьому стані.
#
# Під час виконання програми ми можемо відкривати, закривати, блокувати
# та розблоковувати двері відповідно до їх поточного стану.
# Цей паттерн дозволяє нам легко додавати нові стани
# та розширювати функціональність системи дверей без зміни коду класу Door.
# """