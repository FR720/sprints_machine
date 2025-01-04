import numpy as np

# Creating NumPy arrays
arr_int = np.array([1, 2, 3, 4])          # Integer array
arr_float = np.array([1.1, 2.2, 3.3, 4.4])    # Float array
arr_bool = np.array([True, False, True, False])  # Boolean array

# Performing basic arithmetic operations
arr_sum = arr_int + arr_float                # Addition
arr_diff = arr_float - arr_int               # Subtraction
arr_prod = arr_int * arr_float               # Multiplication

print(f"Integer Array: {arr_int}")
print(f"Float Array: {arr_float}")
print(f"Boolean Array: {arr_bool}")
print(f"Addition (arr_int + arr_float): {arr_sum}")
print(f"Subtraction (arr_float - arr_int): {arr_diff}")
print(f"Multiplication (arr_int * arr_float): {arr_prod}")
