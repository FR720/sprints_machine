# Function to perform bitwise operations
def bitwise_operations(a, b):
    # Bitwise AND
    and_result = a & b
    print(f"{a} & {b} = {and_result} (Binary: {bin(and_result)})")

    # Bitwise OR
    or_result = a | b
    print(f"{a} | {b} = {or_result} (Binary: {bin(or_result)})")

    # Bitwise XOR
    xor_result = a ^ b
    print(f"{a} ^ {b} = {xor_result} (Binary: {bin(xor_result)})")

# User input
a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))

# Call function to perform bitwise operations
bitwise_operations(a, b)
