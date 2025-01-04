#Requirment-1 
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

sum_result = num1 + num2
difference_result = num1 - num2
product_result = num1 * num2
quotient_result = num1 / num2 if num2 != 0 else "Undefined (Division by Zero)"

print(f"Sum: {sum_result}")
print(f"Difference: {difference_result}")
print(f"Product: {product_result}")
print(f"Quotient: {quotient_result}")

###############################################################
#Requirment-2

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

add = num1 + num2
subtract = num1 - num2
multiply = num1 * num2
divide = num1 / num2 if num2 != 0 else "Undefined (Division by Zero)"

print(f"Addition: {add}")
print(f"Subtraction: {subtract}")
print(f"Multiplication: {multiply}")
print(f"Division: {divide}")


##############################################################
#Requirment-3
while True:
    try:
        num1 = float(input("Enter the first number: "))  # Try to convert input to float
        break
    except ValueError:
        print("Invalid input! Please enter a valid number.")

while True:
    try:
        num2 = float(input("Enter the second number: "))
        break
    except ValueError:
        print("Invalid input! Please enter a valid number.")

add = num1 + num2
subtract = num1 - num2
multiply = num1 * num2
divide = num1 / num2 if num2 != 0 else "Undefined (Division by Zero)"

print(f"Addition: {add}")
print(f"Subtraction: {subtract}")
print(f"Multiplication: {multiply}")
print(f"Division: {divide}")