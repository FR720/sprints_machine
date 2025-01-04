def factorial(n):
    # Check if the number is valid
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer.")
    
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
try:
    num = int(input("Enter a non-negative integer: "))
    print(f"The factorial of {num} is {factorial(num)}")
except ValueError as e:
    print(e)
