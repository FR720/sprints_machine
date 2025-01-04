# Recursive function to calculate factorial
def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)  # Recursive call

num = 5  # You can change the number here
result = factorial(num)
print(f"The factorial of {num} is {result}")