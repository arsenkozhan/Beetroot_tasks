print("task1")
#Sample String: 'helloworld'
# Expected Result : 'held'
s = 'helloworld'
print(s[:2],s[-2:], sep='')
print(s[0],s[1],s[8],s[9], sep='')

# Sample String: 'my'
# Expected Result : 'mymy'
s = 'my' * 2
print(s)

# Sample String: 'x'
# Expected Result: Empty String
s = "xd"
if len(s) < 2:
    print("empty string")
else:
    print(s)


#task2
print("task2")
num = "0673363830"
if len(num) == 10 and num.isdigit(): #перевіряє чи число == 10 символам, та чи містить цифри
    print("Valid phone number")
else:
    print("Invalid phone number")
print("\n")


#task3
num1 = 5
num2 = 10
num3 = num1 + num2
sum_user = int(input("Enter sum number: "))
if num3 == sum_user:
    print("correct")
else:
    print("incorrect")


#task4
print("task4")
stored_name = "arsen"
upper_a = ord('a') - 32
name = input("Enter your name: ")
if name.lower() == stored_name.lower():
    print("Yes, your name is ", name)
else:
    print("No, your name is ", name)
