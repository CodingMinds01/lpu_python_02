# BITWISE OPERATORS - &(AND), |(OR), ~(NOT), ^(XOR)
# a, b = 5, 4

# '''
# 5 -> 0101
# 4 -> 0100

# AND -> 0100 -> 4
# OR -> 0101 -> 5
# NOT -> -(0101 + 1) -> -(0110) -> -6
# XOR -> 0001 -> 1

# print('Bitwise AND is -> ', a & b)
# print('Bitwise OR is -> ', a | b)
# print('Bitwise NOT is -> ', ~a)
# print('Bitwise XOR is -> ', a ^ b)


# EXAMPLES ON BITWISE --> Binary digits
# 4 bit binary representation of 9
# ...  (2^3) (2^2) (2^1) (2^0)
# 16 8 4 2 1
# 0  1 0 0 1 . -> binary(9) -> 1001

# 15 -> 8 + 4 + 2 + 1 => 001111

# AND
# no(Input) -> a, b
# a     b       O/P
# 0     0       0
# 0     1       0
# 1     0       0
# 1     1       1
# num1 = 15
# num2 = 20
# 15 -> 0 1 1 1 1
# 20 -> 1 0 1 0 0
#           AND
#    -> 0 0 1 0 0 -> 4 -> ANS
# print(num1 & num2)

# OR
# no(Input) -> a, b
# a     b       O/P
# 0     0       0
# 0     1       1
# 1     0       1
# 1     1       1
# 15 -> 0 1 1 1 1
# 20 -> 1 0 1 0 0
#           OR
#       1 1 1 1 1   -> 31 -> ANS
# print(num1 | num2)

# NOT
# no(Input) -> a
# a      O/P
# 0      1
# 1      0
# 20 -> 1 0 1 0 0
#           NOT -> -(1 0 1 0 0 + 1)
#        +      1
#       - 1 0 1 0 1 -> -21 -> ANS


# 15 -> 0 1 1 1 1
#             + 1 
#       1 0 0 0 0 -> -16 -> ANS
# num3 = -15
# print("NOT of a -ve value - ", ~num3)
# print(~num1)
# print(~num2)

# XOR
# no(Input) -> a, b
# a     b       O/P
# 0     0       0
# 0     1       1
# 1     0       1
# 1     1       0
# 15 -> 0 1 1 1 1
# 20 -> 1 0 1 0 0
#           XOR
#        1 1 0 1 1 -> 27 -> ANS
# print(num1 ^ num2)

# FUNCTIONS
# -> A way to create some re-usable block of code, which can called anytime for proceesing
# SYNTAX - def functionName(parameters):

# Q -> Create a function to add 2 numbers
# def addTwoNums(num1, num2):
#     return num1 + num2

# # Q -> To get two numbers, add them and print the cube
# val_one = int(input('enter I value -'))
# val_two = int(input('enter II value -'))
# sum_val = addTwoNums(val_one, val_two)
# print(sum_val * sum_val * sum_val)

# PRIME-PALINDROME

# I/O Formatting
# name = "Arun Kudiyal"
# age = 21
# print("hello... my name is " + name + " and I am", age, "years old!")
# f-strings
# print(f"Hello my name is {name} and I am {age} years old!")

# format()
# txt = "For only {:d} dollars!".format(0b11111)
# print(txt)

# import datetime
# print(datetime.datetime.now())

# date = datetime.datetime.now().strftime("%d")
# month = datetime.datetime.now().strftime("%B")
# year = datetime.datetime.now().strftime("%Y")

# hours = datetime.datetime.now().strftime("%H")
# minutes = datetime.datetime.now().strftime("%M")
# seconds = datetime.datetime.now().strftime("%S")
# am_pm = datetime.datetime.now().strftime("%p")
# print(f"Today is {month} {date}th, {year} ; and time is {hours}:{minutes}:{seconds} {am_pm}") 


# month_list = { 1: "Jan", 2: "Feb", 3: "March", 4: "April", 5: "May", 6: "June", 7:"July", 8: "Aug", 9: "Sept", 10: "Oct", 11: "Nov", 12: "Dec" }
# inp_month = int(input("Enter the month number - "))
# print( month_list[inp_month] )

# import datetime
# date = int(input("Enter date (1-31) - "))
# month = int(input("Enter date (1-12) - "))
# year = int(input("Enter date (yyyy) - "))
# myDate = datetime.datetime(year, month, date)
# print(myDate)


# Loops -> Repitive statements

# range(a) -> Range starts with 0 and (num - 1)
# 1. FOR LOOP
# for variableName in range(upperRange):
#   EXPRESSION YOU WANT TO PERFORM IN LOOP

# for variable in range(10):
#     print(variable, end=" ")
# print("\n")

# Questions -> Find the sum of all ositive number upto the user's input
# steps = int(input("Enter the upper range - "))
# sum = 0
# for variable in range(steps):
#     # Checking if the number if even or not
#     if( variable % 2 == 0 ):
#         sum += variable

# print(sum)

# Q -> Given a set of numbers, print the numbers as a list
# steps = int(input("Enter the upper range - "))
# myList = []
# for var in range(steps):
#     # Input the values
#     value = int(input("Enter the value for the set - "))
#     # Inset each value at the end of the set
#     myList.append(value)

# for var2 in myList:
#     print(var2)

# range(a, b)
# print( range(10, 20) ) -> 10 is incluse but 20 is exclusive
# for value in range(10, 20):
#     print(value)

# Q -> Given a range, find all the prime numbers for that range
# lower = int(input("Enter the starting range - "))
# upper = int(input("Enter the ending range - "))
# prime_numbers = set()
# # 10, 11, 12, 13, .... , 19

# # 5, 6, 7, 8, 9, 10
# # variable = 15
# for variable in range(lower, upper):
#     # 2 -> 4, 2 -> 5, 2 -> 6, 2 -> 7, 2 -> 8, 2 -> 9
#     if variable > 1:
#         # variable2 -> (2 - 14)
#         for variable2 in range(2, variable):
#             if(variable % variable2) == 0:
#                 # STOP
#                 break
#         else:
#             prime_numbers.add(variable)
            
# for values in prime_numbers:
#     print(values, end=" ")

# FUNCTIONAL APPROACH -
# prime_numbers = set()
# def checkPrime(number):
#     if number > 1:
#         for i in range(2, number):
#             if(number % i == 0):
#                 break
#         else:
#             prime_numbers.add(number)

# range1 = int(input("Enter a lower range - "))
# range2 = int(input("Enter a upper range - "))
# for number in range(range1, range2):
#     checkPrime(number)

# for j in prime_numbers:
#     print(j, end=", ")

# range(a, b, c)
for i in range(2, 21, 2):
    print(i, end=" ")
print("\n")

for i in range(20, 0, -2):
    print(i, end=" ")
print("\n")