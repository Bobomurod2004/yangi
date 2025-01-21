# class talaba:
#     def __init__(self,talaba_ismi,talaba_yoshi,talaba_kursi,talaba_yunalish):
#         self.talaba_ismi=talaba_ismi
#         self.talaba_yoshi = talaba_yoshi
#         self.talaba_kursi = talaba_kursi
#         self.talaba_yunalish = talaba_yunalish
#
#     def __str__(self):
#          return f"{self.talaba_ismi} va uning yoshi {self.talaba_yoshi} da va yo'nalishi {self.talaba_yunalish}"
# talabalar=talaba('umid',20,3,'biyotexnologiya')
# talaba2=talaba('alijon',19,3,"suniy intelleckt")
# talaba3=talaba('muhammadjafar',20,3,'suniy intellekt')
# talaba2.talaba_ismi="bahodir"
# print(talabalar,'\n',talaba2,'\n',talaba3)

# class telfon:
#     def __init__(self,telfon_nomi,telfon_rusimi):
#         self.telfon_nomi=telfon_nomi
#         self.telfon_rusimi=telfon_rusimi
#     def kitobkani_bosish(self):
#         return "telefon yonmoq"
#     def __str__(self):
#         return f"{self.telfon_nomi } va {self.telfon_rusimi}"
# redmi=telfon('redmi 12 pro','REDMI')
# print(redmi.kitobkani_bosish())

# class tugmalar:
#     def __init__(self,shakli,rangi,matn):
#         self.shakli = shakli
#         self.rangi = rangi
#         self.matn = matn
#     def __str__(self):
#         return f"{self.rangi}"
#     def onClick(self):
#         return self.matn
#     def onhower(self):
#         self.rangi = "oq"
#         return self.rangi
# tortburchak = tugmalar ("to'rtburchak","ko'k",'twitter')
# tortburchak2 = tugmalar ("to'rtburchak","qizil","danger button")
# tortburchak3 = tugmalar ("to'rtburchak","yashil","primary button")
#
# print(tortburchak.onhower())

# class Student:
#     def __init__(self,student_id, student_name, class_name):
#         self.student_id = student_id
#         self.student_name = student_name
#         self.class_name = class_name
#
#     def __str__(self):
#         return f" Talaba = {self.student_id}, Ismi = {self.student_name},Sinfi = {self.class_name}"
#
# talaba1 = Student(25,"umid",'si2201')
# talaba2 = Student(21,'alijon','ax2203')
# print(talaba1,'\n',talaba2)

# class Sudent:
#     pass
#
# class Marks:
#     pass
#
# obj1 = Sudent
# obj2 = Marks
# print(obj1 is Sudent , obj2 is Marks)

# class Tortburchak:
#     def __init__(self, lenght, width):
#         self.lenght = lenght
#         self.width = width
#
#     def __str__(self):
#         return f" {self.lenght}  va {self.width}"
#     def yuza(self):
#         yuza = self.width*self.lenght
#         return  yuza
# yuza=Tortburchak(lenght=5,width=6)
#
# print()

# # uyga vazilar-------------
# def Student_data(Student_id, Student_name = None, Student_class = None):
#
#     print(f"{Student_id}")
#
#     if Student_name:
#         print(f" { Student_name}")
#     if Student_class:
#         print(f" { Student_class}")
# Student_data(25,'Alijon',2201)
#  keyingi___________________


# class Student:
#     def __init__(self, Student_name, Marks):
#         self.Student_name=Student_name
#         self.Marks=Marks
#
#     def __str__(self):
#         return f"{self.Student_name} '\n' {self.Marks}"
#
#     def natija(self):
#         self.Marks=70
#         return self.Marks
# talaba=Student(Student_name='alijon',Marks=60)
# talaba.Student_name = 'bahodir'
# print(talaba.Student_name, talaba.natija() )
