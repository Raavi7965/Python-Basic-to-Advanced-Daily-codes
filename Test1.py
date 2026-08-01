# Problem 1: Safe Division
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if b != 0:
    print(a / b)
else:
    print("Cannot Divide")


# Problem 2: Storage Limit
used_space = int(input("Enter used space (GB): "))

if used_space < 64:
    print("Space Available")
else:
    print("Storage Full")


# Problem 3: Train Arrival
delay = int(input("Enter delay in minutes: "))

if delay > 10:
    print("Late")
else:
    print("On Time")


# Problem 4: Battery Check
battery = int(input("Enter battery percentage: "))

if battery < 20:
    print("Power Saving Mode")
else:
    print("Normal Mode")


# Problem 5: Discount Eligibility
bill = int(input("Enter bill amount: "))

if bill >= 999:
    print("Free Delivery")
else:
    print("Delivery Charges Apply")


# Problem 6: Identify Data Type
a = 10
b = 2.5
c = "Hi"
d = True

print(type(a))
print(type(b))
print(type(c))
print(type(d))


# Problem 7: Memory Address
a = 100
b = a

print(id(a))
print(id(b))


# Problem 8: Memory Comparison
x = "Hi"
y = "Hi"

if id(x) == id(y):
    print("Same Address")
else:
    print("Different Address")


# Problem 9: Arithmetic Result Type
a = 10
b = 2

result = a / b

print(result)
print(type(result))


# Problem 10: Exponent Result
a = 2
b = 5

result = a ** b

print(result)
print(type(result))


# Problem 11: Username Validation
username = input("Enter username: ")

if len(username) >= 8:
    print("Valid Username")
else:
    print("Invalid Username")


# Problem 12: Roll Number Check
roll = input("Enter roll number: ")

if len(roll) == 10:
    print("Valid")
else:
    print("Invalid")


# Problem 13: Product Code
code = input("Enter product code: ")

if len(code) >= 6:
    print("Accepted")
else:
    print("Rejected")


# Problem 14: Password Strength
password = input("Enter password: ")

if len(password) >= 12:
    print("Strong Password")
else:
    print("Weak Password")


# Problem 15: Team Size
team = [1,2,3,4,5,6,7,8,9,10,11]

if len(team) >= 11:
    print("Complete Team")
else:
    print("Incomplete Team")


# Problem 16: Boundary Characters
word = input("Enter a word: ")

print(word[0])
print(word[-1])


# Problem 17: Middle Character
word = input("Enter a word: ")

middle = len(word) // 2

print(word[middle])


# Problem 18: Compare Ends
word = input("Enter a word: ")

if word[0] == word[-1]:
    print("Palindrome Ends")
else:
    print("Not Palindrome Ends")


# Problem 19: Third List Element
numbers = [4, 8, 12, 16]

print(numbers[2])


# Problem 20: Last Tuple Element
data = (5, 10, 15)

print(data[-1])


# Problem 21: Reverse Employee ID
emp = input("Enter Employee ID: ")

print(emp[::-1])


# Problem 22: Department Code
dept = input("Enter Department Code: ")

print(dept[:4])


# Problem 23: Last Four Digits
number = input("Enter Number: ")

print(number[-4:])


# Problem 24: First Half
word = input("Enter a word: ")

half = len(word) // 2

print(word[:half])


# Problem 25: Secret Code Verification
secret = input("Enter Secret Code: ")

if secret[:3] == "ABC":
    print("Verified")
else:
    print("Rejected")