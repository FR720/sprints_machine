import numpy as np

# Creating a 1D array
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# Reshaping the array into a 3x3 matrix
arr_reshaped = arr.reshape((3, 3))

# Stacking arrays vertically and horizontally
arr2 = np.array([10, 11, 12])

# Reshaping arr2 to match the 3x3 matrix for vertical stacking
arr2_reshaped = arr2.reshape(1, 3)

arr_vertical = np.vstack((arr2_reshaped, arr_reshaped))  # Stacking vertically

# Reshaping arr2 to (3,) to match dimensions for horizontal stacking
arr_horizontal = np.hstack((arr_reshaped, arr2_reshaped.T))  # Stacking horizontally, arr2 reshaped

# Splitting the array into two halves
arr_split = np.split(arr, 3)

# Applying Boolean indexing (filter even numbers)
arr_bool_filter = arr[arr % 2 == 0]

print(f"Reshaped Array: \n{arr_reshaped}")
print(f"Vertical Stack: \n{arr_vertical}")
print(f"Horizontal Stack: \n{arr_horizontal}")
print(f"Array after Splitting: \n{arr_split}")
print(f"Filtered Array (even numbers): {arr_bool_filter}")
