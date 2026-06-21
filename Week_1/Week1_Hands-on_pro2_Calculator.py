# Simple Calculator: Perform basic arithmetic operations

#get 2 numbers as input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# print results of basic arithmetic operations
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)

if num2 != 0:
    print("Division:", num1 / num2)
else:
    print("Cannot divide by zero")