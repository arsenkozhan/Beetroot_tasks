# Write a program to display the names of countries in capital letters if string
#hasn't a digit and skip the output if has
# which also includes while true and checking the end of the work on the keyword
# 1. while True
# 2. input -> print capital letters
# 3. break point (condition when program stop)

#
# while True:
#     country = input("Enter country (or 'end' to stop): ")
#     if country == 'end':
#         print("Program stopped.")
#         break
#     if country.isalpha():
#         print("you have entered: ", country.capitalize())
#     else:
#         print("wrong input")

#
#

# Напишіть програму на Python, яка підсумовує всі цифри в рядку.
# Приклад: вхідні дані — '1234', вихід — 10
# Передбачте перевірку наявності нецифрових символів у рядку.

# while True:
#     num = input("Enter a number: ")
#     if num.isdigit():
#         total = 0
#         for digit in num:
#             total += int(digit)
#         print("Sum: ", total)
#     else:
#         print("wrong input")


# Write a Python program to construct the following pattern, using a while loop
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
# Передбачити задання довжини вершини (максимальної кількості зірочок)

# n = int(input("How many stars do you want? "))
# i = 1
# while i <= n:
#     print('*' * i)
#     i += 1
#
# i = n - 1
# while i > 0:
#     print('*' * i)
#     i -= 1