# Requirement 1: Control Flow with if, elif, else
print("FizzBuzz Logic for Numbers 1-100:")
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

# Requirement 2: Loops (for loop) for FizzBuzz Logic in Custom Range
print("\nCustom Range FizzBuzz:")
# Input for custom range with validation
while True:
    try:
        start = int(input("Enter the starting number: "))
        end = int(input("Enter the ending number: "))
        
        # Validating the input to ensure start <= end
        if start > end:
            print("Starting number must be less than or equal to the ending number. Please try again.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter valid integers.")

# FizzBuzz with custom range (using the loop)
for num in range(start, end + 1):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
