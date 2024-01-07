# ЄДИНЕ ВІКНО!!!!!!!!!!!!!!!

# # Підсистема 1
# class SubsystemA:
#     def operation_a(self):
#         return "Subsystem A operation"
#
#
# # Підсистема 2
# class SubsystemB:
#     def operation_b(self):
#         return "Subsystem B operation"
#
#
# # Підсистема 3
# class SubsystemC:
#     def operation_c(self):
#         return "Subsystem C operation"
#
#
# # Фасад
# class Facade:
#     def __init__(self):
#         self._subsystem_a = SubsystemA()
#         self._subsystem_b = SubsystemB()
#         self._subsystem_c = SubsystemC()
#
#     def operate(self):
#         results = []
#         results.append(self._subsystem_a.operation_a())
#         results.append(self._subsystem_b.operation_b())
#         results.append(self._subsystem_c.operation_c())
#         return "\n".join(results)
#
#
# # Приклад використання
# if __name__ == "__main__":
#     facade = Facade()
#     print(facade.operate())


# ======= Приклад використання для розсилки повідомлення =======

# Підсистема для відправки повідомлення на Facebook
class FacebookAPI:
    def post_message(self, message):
        return f"Posted on Facebook: {message}"


# Підсистема для відправки повідомлення на Twitter
class TwitterAPI:
    def tweet(self, message):
        return f"Tweeted: {message}"

# Підсистема для відправки повідомлення на Instagram
class InstagramAPI:
    def share_photo(self, photo):
        return f"Shared on Instagram: {photo}"



# Фасад, який об'єднує роботу зі всіма підсистемами
class SocialMediaFacade:
    def __init__(self):
        self._facebook_api = FacebookAPI()
        self._twitter_api = TwitterAPI()
        self._instagram_api = InstagramAPI()


    def post(self, message, photo=None):
        results = []
        results.append(self._facebook_api.post_message(message))
        results.append(self._twitter_api.tweet(message))
        if photo:
            results.append(self._instagram_api.share_photo(photo))
        return "\n".join(results)


# Приклад використання
if __name__ == "__main__":
    facade = SocialMediaFacade()
    message = "Hello, world!"
    photo = "beautiful_sunrise.jpg"
    print(facade.post(message))
    print('.' * 80)
    print(facade.post(message, photo))


"""
У цьому прикладі є три підсистеми для відправки повідомлень 
на різні соціальні мережі: FacebookAPI, TwitterAPI і InstagramAPI, 
кожна з яких має свою функціональність.

SocialMediaFacade є класом фасаду, 
який об'єднує роботу з усіма підсистемами. 
Він має посилання на кожну підсистему і визначає метод post, 
який використовує методи підсистем для відправки повідомлення та фото (якщо воно є).

У прикладі використання ми створюємо об'єкт фасаду SocialMediaFacade 
та викликаємо його метод post для відправки повідомлень на всі три соціальні мережі. 
Можна відправити лише текстове повідомлення або текстове повідомлення з фото.

Цей приклад ілюструє використання патерну Facade 
для спрощення процесу роботи зі складними підсистемами, 
такими як соціальні мережі. 
Фасад приховує деталі роботи з кожною підсистемою 
та надає єдиний зручний інтерфейс для взаємодії з ними.
"""