# Dependency Inversion Principle - DIP

"""
Принцип інверсії залежності (Dependency Inversion Principle - DIP)
спрямований на створення слабких залежностей між класами та модулями.
Основна ідея полягає в тому,
що високорівневі модулі не повинні залежати від низькорівневих модулів,
а обидва рівні повинні залежати від абстракцій.
"""


# Абстракція (абстрактний клас або інтерфейс)
class NotificationService:
    def send_notification(self, message):
        pass

    def __repr__(self):
        return 'None'


# Низькорівневий модуль (конкретна реалізація)
class EmailNotification(NotificationService):
    def send_notification(self, message):
        print(f"Sending email notification: {message}")

    def __repr__(self):
        return 'Email'


# Низькорівневий модуль (конкретна реалізація)
class SMSNotification(NotificationService):
    def send_notification(self, message):
        print(f"Sending SMS notification: {message}")

    def __repr__(self):
        return 'SMS'



# Високорівневий модуль, який залежить від абстракції (NotificationService)
class NotificationManager:
    def __init__(self, notification_service):
        self.notification_service = notification_service

    def send_notification(self, message):
        self.notification_service.send_notification(message)

    def __str__(self):
        return f'Sending {self.notification_service}-message.'





# Приклад використання
if __name__ == "__main__":
    email_notification = EmailNotification()
    sms_notification = SMSNotification()
    empty_notification = NotificationService()

    # Високорівневий модуль взаємодіє з низькорівневими модулями через абстракцію
    manager1 = NotificationManager(email_notification)
    manager1.send_notification("Hello, this is an email!")

    manager2 = NotificationManager(sms_notification)
    manager2.send_notification("Hi, this is a SMS!")


    manager3 = NotificationManager(empty_notification)
    manager3.send_notification("Hello, world!")


# В якості атрибута - об'єкт певного класу !
print(type(manager1))
print(type(manager2))
print(type(manager3))

print('.'*80)
print(type(manager1.notification_service))
print(type(manager2.notification_service))
print(type(manager3.notification_service))
print('.'*80)
print(manager1)
print(manager2)
print(manager3)