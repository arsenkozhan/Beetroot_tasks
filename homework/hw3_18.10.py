
print("Task 1")
name = "Arsen"
day = "Monday"
print(f"Good day, {name}! {day} is a perfect day to learn some python.")
print("Good day, %s! %s is a perfect day to learn some python." % (name, day), end="\n\n")

print("Task 2")
first_name = "Arsen"
last_name = "Kozhan"
print(first_name, last_name, sep=" ")
print(first_name + " " + last_name)
print(f"{first_name} {last_name}")
first_name = "Arsen"
first_name += " Kozhan"
print(first_name, end="\n\n")

print("Task 3")
a = 3
b = 2
print(a + b)
print(a - b)
print(a / b)
print(a * b)
print(a ** b)
print(a // b)
print(a % b)