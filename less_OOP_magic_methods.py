class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):   # representation
        return f"Vector({self.x}, {self.y})"

    def __str__(self): #print()
        return f"({self.x}, {self.y})"

    #
    # def __eq__(obj1, obj2): #  =
    #     if obj1.x == obj2.x and obj1.y == obj2.y:
    #         return True
    #     else:
    #         False

    # def __add__(self, v): #   +
    #     return Vector(self.x + v.x, self.y + v.y)
    #
    # def __sub__(self, v):   # -
    #     return Vector(self.x - v.x, self.y - v.y)
    #
    #
    # def len(self):   # довжина
    #     return (self.x**2 + self.y**2)**0.5
    #
    # def __gt__(self, other):
    #     if self.len() > other.len():
    #         return True
    #     else:
    #         return False
    #
    # def __ge__(self, other):
    #     if self.len() >= other.len():
    #         return True
    #     else:
    #         return False



# v1 = Vector(2, 4)
# print(v1)
# print(f"vector v1 = {v1}")
# v2 = Vector(3, 6)
# print(f"vector v2 = {v2}")
# print([v1, v2])

# # print(f"v1 = v2 ->", v1 == v2)
# print(f"v1 + v2 = {v1 + v2}")
# print(f"v2 - v1 = {v2 - v1}")
# print(f"|v1| = {v1.len()}")
#
# print(*dir(v1), sep='\n')
#
# print('v1 > v2', v1 > v2)
# print('v1 < v2', v1 < v2)
# print('v1 >= v2', v1 >= v2)
# print('v1 <= v2', v1 <= v2)
# '''
# __eq__  ->  =
# __ge__  ->  >=
# __gt__  ->  >
# __le__  ->  <=
# __lt__  ->  <
# __ne__  ->  NOT
# '''
#




# ===============================================================
# class UserLevel:
#     us_dict = {"Admin": 4, "Operator": 3, "Dispatcher": 2, "Guest": 1}
#
#     def __init__(self, user_level):
#         if user_level in self.us_dict:
#             self.u_level = user_level
#         else:
#             print("Wrong user type!")
#             self.u_level = "Guest"
#
#     def diff(self, level1, level2):
#         return self.us_dict[level1] - self.us_dict[level2]
#
#
#
#     def __lt__(self, user):
#         return True if self.diff(self.u_level, user.u_level) < 0 else False
#
#     def __le__(self, user):
#         return True if self.diff(self.u_level, user.u_level) <= 0 else False
#
#     def __eq__(self, user):
#         return True if self.diff(self.u_level, user.u_level) == 0 else False
#
#     def __ge__(self, user):
#         return True if self.diff(self.u_level, user.u_level) >= 0 else False
#
#     def __gt__(self, user):
#         return True if self.diff(self.u_level, user.u_level) > 0 else False
#
#     def __repr__(self):
#         return f"UserLevel({self.u_level})"
#
#     def __str__(self):
#         return self.u_level
#
#     # def __sub__(self, other):
#     #     return self.diff(self.u_level, other.u_level)
#
#
# a1 = UserLevel('Operator')
# a2 = UserLevel('Guest')
# a3 = UserLevel('Admin')
# a4 = UserLevel('Got')
#
# print(a1)
# print(a2)
# print(a3)
# print(a4)
#
#
# print(a1.diff('Admin', 'Guest'))
# # print(a1 - a2)







# def __sub__(obj1, obj2):
#     return UserLevel.us_dict[obj1.u_level] - UserLevel.us_dict[obj2.u_level]
#
#
# if __name__ == "__main__":
#     need = "Operator"
#     need_level = UserLevel(need)
#     print(f"need level: {need_level.us_dict[need]}  {need}")
#
#     user = "Dispatcher"
#     # user = input('User level = ')
#     user_level = UserLevel(user)
#     print(f"user level: {user_level.us_dict[user]}  {user}")
#
#     if user_level.us_dict[user] >= need_level.us_dict[need]:
#         print("Access enabled!")
#     else:
#         print("Access denied!")