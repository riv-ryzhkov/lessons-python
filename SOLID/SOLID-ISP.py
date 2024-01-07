# Interface Segregation Principle - ISP

"""
Принцип розділення інтерфейсу (Interface Segregation Principle - ISP) стверджує,
що клієнти не повинні залежати від інтерфейсів, які вони не використовують.
Іншими словами, інтерфейси повинні бути специфічними для потреб клієнтів.
"""


class Worker:
    def work(self):
        pass

    def get_paid(self):
        pass

    def track_hours(self):
        pass

    def get_vacation(self):
        pass


class Employee(Worker):
    def work(self):
        print("Employee is working")

    def get_paid(self):
        print("Employee is getting paid")

    def get_vacation(self):
        print('Employee has vacation')


class Freelancer(Worker):
    def work(self):
        print("Freelancer is working")

    def get_paid(self):
        print("Freelancer is getting paid")

    def track_hours(self):
        print("Freelancer is tracking hours")




user1 = Employee()
user2 = Freelancer()
user3 = Employee()



workers = [user1, user2, user3]


for human in workers:
    human.work()
    human.get_paid()
    human.track_hours()
    human.get_vacation()
    print()


"""
Ми маємо два підкласи Employee і Freelancer, 
які реалізують інтерфейс батьківського класу Worker. 
Кожен з них виконує роботу та отримує зарплату, 
але Freelancer також володіє додатковим методом track_hours, 
який є специфічним для фрілансерів.

Це дотримання принципу розділення інтерфейсу, 
оскільки обидва класи реалізують тільки ті методи, 
які необхідні для їхнього функціонування. 
Employee та Freelancer не мають залежностей від методів, 
які вони не використовують, 
і вони можуть бути використані клієнтами згідно їхніх потреб.
"""