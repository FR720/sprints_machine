import numpy as np

# Creating a NumPy array
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# Sum
arr_sum = np.sum(arr)

# Mean
arr_mean = np.mean(arr)

# Min and Max
arr_min = np.min(arr)
arr_max = np.max(arr)

# Other aggregation operations: variance and standard deviation
arr_var = np.var(arr)
arr_std = np.std(arr)

print(f"Sum: {arr_sum}")
print(f"Mean: {arr_mean}")
print(f"Min: {arr_min}")
print(f"Max: {arr_max}")
print(f"Variance: {arr_var}")
print(f"Standard Deviation: {arr_std}")
