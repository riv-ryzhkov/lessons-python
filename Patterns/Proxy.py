# ======================================
# Приклад з Інтернет-сайтами ===========
# ======================================

# # Суб'єкт
# class Internet:
#     def connect(self, website):
#         return f"Connecting to {website}"
#
#
# # Проксі
# class InternetProxy:
#     def __init__(self):
#         self._internet = Internet()
#         self._banned_websites = ["facebook.com", "twitter.com"]
#
#     def connect(self, website):
#         if website in self._banned_websites:
#             return f"Access to {website} is blocked"
#         return self._internet.connect(website)
#
#
# # Приклад використання
# if __name__ == "__main__":
#
#     # internet = Internet()
#     internet = InternetProxy()
#
#     websites = ["google.com", "facebook.com", "youtube.com", "twitter.com"]
#
#     for website in websites:
#         result = internet.connect(website)
#         print(result)


"""
Патерн Проксі дозволяє контролювати доступ до об'єкта, 
додаючи додатковий рівень управління або обмеження доступу.

У цьому прикладі є суб'єкт Internet, 
який представляє можливість підключення до Інтернету.

Клас InternetProxy є класом проксі, 
який обгортає суб'єкт Internet. 
Він додає додатковий рівень перевірки, 
перш ніж дозволити з'єднання з веб-сайтом. 
В прикладі проксі перевіряє, чи веб-сайт заблокований у списку заборонених, 
і повертає відповідний результат.

У прикладі використання ми створюємо об'єкт InternetProxy 
та намагаємося підключитися до декількох веб-сайтів. 
Проксі перевіряє, чи веб-сайт є в списку заборонених, 
і відповідно обмежує або дозволяє доступ.

Цей приклад демонструє використання патерну Проксі 
для додаткового контролю над доступом до об'єкта, 
що може бути корисним для впровадження обмежень 
або додаткового функціоналу під час доступу до об'єкта.
"""

# =================================================
# Приклад з банківською карткою ===================
# =================================================


# # Базовий інтерфейс для реального рахунку та проксі-рахунку
# class BankAccount:
#     def __init__(self, account_holder, balance):
#         self.account_holder = account_holder
#         self.balance = balance
#
#     def get_balance(self):
#         return self.balance
#
#     def deposit(self, amount):
#         self.balance += amount
#         print(f"Balance of {self.account_holder}'s "
#               f"account has increased to {self.balance}.")
#
#     def withdraw(self, amount):
#         self.balance -= amount
#
#
# # Реальний банківський рахунок
# class RealBankAccount(BankAccount):
#     pass
#
#
# # Проксі-банківський рахунок з обмеженням доступу до зняття коштів
# class ProxyBankAccount(BankAccount):
#     def __init__(self, real_account):
#         self.real_account = real_account
#
#     def withdraw(self, amount):
#         if self.real_account.get_balance() >= amount:
#             self.real_account.withdraw(amount)
#             print(f"Withdrew {amount} from {self.real_account.account_holder}'s account.")
#         else:
#             print("Withdrawal denied. Insufficient funds.")
#
#
# # Приклад використання
# if __name__ == "__main__":
#     real_account = RealBankAccount("Alice", 1000)
#     proxy_account = ProxyBankAccount(real_account)
#
#     # Сума коштів на створеному реальному рахунку
#     print(f"Balance in {real_account.account_holder}'s account: {real_account.get_balance()}")
#     print('.' * 80)
#
#     # Клієнт намагається зняти кошти через проксі
#     proxy_account.withdraw(400)
#
#     # Залишок на реальному рахунку
#     print(f"Balance in {real_account.account_holder}'s account: {real_account.get_balance()}")
#     print('.' * 80)
#
#     # Клієнт намагається зняти більше коштів, ніж є на рахунку
#     proxy_account.withdraw(1000)
#
#     # Клієнт кладе кошти на свій рахунок
#     real_account.deposit(800)
#
#     # Залишок на реальному рахунку
#     # print(f"Balance in {real_account.account_holder}'s account: {real_account.get_balance()}")
#     print('.' * 80)
#
#     # Клієнт намагається зняти більше кошти в межах існуючої суми
#     proxy_account.withdraw(1000)
#
#     # Залишок на реальному рахунку
#     print(f"Balance in {real_account.account_holder}'s account: {real_account.get_balance()}")
