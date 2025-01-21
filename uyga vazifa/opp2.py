# class Mashina:
#     def __init__(self, rangi, yili):
#         self.rangi=rangi
#         self.yili = yili
#
# class Tranport(Mashina):
#     pass
#
# transportlar=Tranport('qora',2005)
#
# print(transportlar.rangi,transportlar.yili)

# class Shakllar:
#
#     def __init__(self, uzunlik):
#         self.uzunlik=uzunlik
#
#     def korinish(self):
#         return "ko'rinish"
# class Korinish(Shakllar):
#     def korinish(self):
#         return "aylana"
# natija=Korinish(45)
# print(natija.korinish())

# class Animal:
#
#      def __init__(self, ismi, yoshi):
#          self.ismi=ismi
#          self.yoshi=yoshi
#
# class It(Animal):
#
#     pass
# it=It('alopar',25)
# print(it.ismi)

#
# class Brand:
#     def __init__(self, name, created_at):
#         self.name=name
#         self.created_at=created_at
#
# class BMW(Brand):
#      def __init__(self, name, created_at, speed):
#          super().__init__(name, created_at)
#          self.speed = speed
# mashina=BMW("BMW 5",2002,180)
# print(mashina.speed)

# class Bird:
#     def flay(self):
#         return "ucmaydi"
# class Eagle(Bird):
#     def flay(self):
#         return "uchadi"
#
# hayvon=Eagle()
# print(hayvon.flay())

# class Employee:
#     def salary(self):
#         return "narxi"
#
# class Manager:
#     def salary(self):
#         return "45"
#
#
# class Developer:
#     def salary(self):
#         return "54000"
#
# narxi=Developer()
# print(narxi.salary())

#TOPSHIRIQLAR-------------------------------------
# class BankAccaunt:
#     def __init__(self, accaount_namer, data_of_opening, balanc, customer_name):
#         self.accaount_namer=accaount_namer
#         self.data_of_opening=data_of_opening
#         self.balanc=balanc
#         self.customer_name=customer_name
#
#     def deposit(self, amount):
#         self.balanc += amount
#         # summa=self.balanc+self.amount
#         # return f"Tashlanadigan summa:{summa}"
#
#     def withdraw(self, amoun):
#         self.balanc -=amoun
#         # return f"Yechiladigan summa:{}"
#
#     def check_balance(self, check_balansa):
#         self.check_balansa=check_balansa
#         return f"Kartadagi mavjud summa:{check_balansa}"
#
#     def print_customer_detail(self):
#         return "print_customer_detail"
# bank=BankAccaunt(4571,28.09,28000,"alijon")
# print(bank.withdraw(28000))
# print(bank.balanc)

#vorislar


# class Restaran:
#     def __init__(self, menu_items, book_table, customer_order):
#         self.menu_items = menu_items
#         self.book_table = book_table
#         self.customer_order = customer_order
#
#     def add_item_to_menu(self, toam_nomi, narxi):
#         self.taom_nomi=toam_nomi
#         self.narxi=narxi
#         return self.taom_nomi,self.narxi
#
#     def book_tables(self,stol_holati):
#         self.stol_holati=stol_holati
#         if stol_holati==0:
#              return "stol band emas"
#         else:
#             return "stol band"
#
#     def customer_orders(self):
#         return "customer_order"
#
# taom = Restaran(45,78,"ddmfmd")
# print(taom.book_tables(0))


# class Instrument:
#      def play(self, play_soati):
#          self.play_soati=play_soati
#          return
# class Guitar(Instrument):
#     def __init__(self, ):
#          super().__init__()
#          self.