# class Mathoperator:
#     @staticmethod
#     def add_numbers(a, b):
#         return a+b
#
# print(Mathoperator.add_numbers(10, 40))
#
# obj1=Mathoperator()
# print(obj1.add_numbers(45,552))

# class Matematika:
#
#     def __init__(self, qoshish):
#         self.qoshish=qoshish
#
#
#     @classmethod
#     def yigindi(cls, summa):
#         return cls(summa)
#
#
# obj1=Matematika(48)
# a = Matematika.yigindi(78)
# print(a.qoshish)

# class Circle:
#     def __init__(self, radius):
#         self._radius=radius
#
#     @property
#     def area(self):
#         return self._radius * 2
#
#     @area.setter
#     def area(self, value):
#         if value < 0:
#             raise ValueError("Radius connot be negative")
#         self._radius = value
#
# circle = Circle(5)lass Person:
# #     def __init__(self,ismi):
# #         self._ismi=ismi
# #     @property
# #     def ism(self):
# #         return self._ismi
# #
# #     @ism.setter
# #     def ism1(self, value):
# #         if not value.strip():
# #             raise ValueError("nfenfjcncdjnd")
# #         self._ismi = value
# #
# #     @ism.deleter
# #     def ism2(self):
# #         print(f"jfenfjenjj{self._ismi}")
# #         del self._ismi
# #
# # person1 = Person("umid")
# # del person1.ism2
# print(circle.area)
#
# circle._radius =10
# print( circle.area)


