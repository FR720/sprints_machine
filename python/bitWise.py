# Bitwise Operators

# Defining two integers
a = 5  # Binary: 101
b = 3  # Binary: 011

# Bitwise AND (&)
and_result = a & b  # Binary: 001 (1 in decimal)
print(f"{a} & {b} = {and_result} (Binary: {bin(and_result)})")

# Bitwise OR (|)
or_result = a | b  # Binary: 111 (7 in decimal)
print(f"{a} | {b} = {or_result} (Binary: {bin(or_result)})")

# Bitwise XOR (^)
xor_result = a ^ b  # Binary: 110 (6 in decimal)
print(f"{a} ^ {b} = {xor_result} (Binary: {bin(xor_result)})")

# Bitwise Left Shift (<<)
left_shift_result = a << 1  # Binary: 1010 (10 in decimal)
print(f"{a} << 1 = {left_shift_result} (Binary: {bin(left_shift_result)})")

# Bitwise Right Shift (>>)
right_shift_result = a >> 1  # Binary: 10 (2 in decimal)
print(f"{a} >> 1 = {right_shift_result} (Binary: {bin(right_shift_result)})")
