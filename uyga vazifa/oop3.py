#
# class User:
#
#     def __init__(self, full_name, password, role):
#         self.full_name = full_name
#         self.password = password
#         self.role = role
#
# class BankAccount:
#
#     def __init__(self, full_name, balace, cv):
#         self.full_name = full_name
#         self._balance = balace
#         self.__cv = cv
#
#     def updete_balance(self, user, amount):
#         if user.role=="admin":
#             self._balance = amount
#         else:
#             return "xato siz kira olmaysiz"
#
#
#     def __updete_cv(self, cv):
#         self.__cv=cv
#
#     def uptete_cv(self, user, cv):
#         if user.role == "direktor":
#             self.__cv=cv
#             return self.__cv
#         else:
#             return "xatolik"
#
# user1=User("alijon",455,"direktor")
#
# user2=BankAccount("alijon",2455,45)
# print(user2.uptete_cv(user1,48))
#
# # bank=BankAccount("nahodir",98,15)
# # print(bank._balance)
# #
# # bank.updete_balance(user1,2500000)
# # print(bank._balance)
#
#








































# class User:
#     def __init__(self, full_name, password, role):
#         self.full_name=full_name
#         self.password=password
#         self.role=role
#
# class Bankaccount:
#     def __init__(self, owner: User, balance:int, cv:int):
#         self.owner=owner
#         self._balance=balance
#         self.__cv=cv
#
#     def update_balance(self, admin:User, amount: int):
#         if admin.role == "admin" and self.owner.role == "sutudent":
#             self._balance=amount
#             return
#         else:
#             return "xatolik"
#
#
# user1=User("alijon",1245,"sutudent")
# user2=User("mamur",142,"admin")
# bank=Bankaccount(user1,45000,14)
# bank.update_balance(user2,450221)
# print(bank._balance)
#
#Uyga vazifalar-------------------------------------

# 1masala

# class BankAccount:
#     def __init__(self,account_number, balance, owner):
#         self.__accoount_number=account_number
#         self.__balance=balance
#         self.__owner=owner
#
#     def depozit(self, amount):
#         self.__balance += amount
#
#     def writdraw(self, ount):
#         self.__balance -=ount
#
#     def get_balance(self):
#         return self.__balance
#
# bank=BankAccount(4578,280000,"Admin")
# print(bank.get_balance())

# 2masala

# class Employee :
#     def __init__(self, id, name,base_salary, bonus):
#         self.__id=id
#         self.__name=name
#         self.__base_salary=base_salary
#         self.__bonus=bonus
#
#     def get_id(self):
#         return self.__id
#
#     def get_name(self):
#         return self.__name
#
#     def get_base_salary(self):
#         return self.__base_salary()
#
#     def get_bonus(self):
#         return self.__bonus
#
#     def set_id(self):
#         return self.__id
#
#     def set_name(self):
#         return self.__name
#
#     def set_base_salary(self):
#         return self.__base_salary()
#
#     def set_bonus(self):
#         return self.__bonus
#     def __base_salary(self,):
#         self.__base_salary += self.__bonus
#
#
#     def getter(self, get_id, get_name):
#
#
#     def setter(self, set_id, set_name):
#
#         pass

# class User:
#     def __init__(self, name, roli,):
#         self.name=name
#         self.roli=roli
#
# class Exam:
#     def __init__(self,owner,baholar):
#         self.owner=owner
#         self.__baholar=baholar
#
#     def baholar1(self,admin,natija):
#         if admin.roli=="o'qituvchi":
#             self.__baholar=natija
#
# user1=User("Alijon","Talaba")
# user2=User("Muhammadali","o'qituvchi")
# baho=Exam(user1,4)
# print(baho.baholar1(user1, 5))






