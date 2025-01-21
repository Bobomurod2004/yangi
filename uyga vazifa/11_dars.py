# def yigindi(son):
#     summ=0
#     while son>0:
#         summ +=son%10
#         son//=10
#     return  summ
# son=int(input("son kiriting="))
# print(f"Biz kiritgan son yig'indis={yigindi(son)}")
# #2masala--------------------------------------------
# # my_list=['olma','olcha','uzmum']
# # katta=list(map(lambda x:str(x).upper(),my_list))
# # print(katta)
# #1masala---------------------


# def factorial(n):
#     if n < 0:
#         raise ValueError("Factorial is not defined for negative numbers.")
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n - 1)
#
#
# # Example usage
# try:
#     number = 5
#     print(f"Factorial of {number} is {factorial(number)}")
# except ValueError as e:
#     print(e)





# def sum_of_digits(n):
#
#     if n < 0:
#         raise ValueError("Sum of digits is not defined for negative numbers.")
#     if n < 10:
#         return n
#     return n % 10 + sum_of_digits(n // 10)
#
# # Example usage
# try:
#     number = 6
#     print(f"Sum of digits of {number} is {sum_of_digits(number)}")
# except ValueError as e:
#     print(e)


# a = 0
# b = 0
# turtle.speed(18)
# turtle.bgcolor('blue')
# turtle.pencolor('red')
# turtle.penup()
# turtle.goto(0, 100)
# turtle.pendown()
# while True:
#     turtle.forward(a)
#     turtle.right(b)
#     a += 3
#     b += 1
