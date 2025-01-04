import pandas as pd
import numpy as np

# Create DataFrame from a list
data_list = [1, 2, 3, 4, 5]
df_list = pd.DataFrame(data_list, columns=["Numbers"])
print("DataFrame from List:")
print(df_list)

# Create DataFrame from a dictionary
data_dict = {"Name": ["Alice", "Bob", "Charlie"], "Age": [25, 30, 35]}
df_dict = pd.DataFrame(data_dict)
print("\nDataFrame from Dictionary:")
print(df_dict)

# Create DataFrame from a NumPy array
data_array = np.random.randint(1, 100, size=(5, 3))  # 5 rows, 3 columns
df_array = pd.DataFrame(data_array, columns=["A", "B", "C"])
print("\nDataFrame from NumPy Array:")
print(df_array)

# Selecting specific columns and rows
print("\nSelecting Column 'A':")
print(df_array["A"])

print("\nSelecting Rows with Values in Column 'A' > 50:")
filtered_df = df_array[df_array["A"] > 50]
print(filtered_df)

# Filtering based on multiple conditions
print("\nFiltering Rows where 'A' > 50 and 'C' < 30:")
filtered_multi_condition = df_array[(df_array["A"] > 50) & (df_array["C"] < 30)]
print(filtered_multi_condition)
