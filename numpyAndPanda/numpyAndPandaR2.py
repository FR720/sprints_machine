import pandas as pd
import numpy as np

# Create a DataFrame with missing data
data_with_nan = {"A": [1, 2, np.nan, 4], "B": [5, np.nan, 7, 8], "C": [9, 10, 11, np.nan]}
df_nan = pd.DataFrame(data_with_nan)
print("Original DataFrame with Missing Data:")
print(df_nan)

# Handle missing data using .fillna()
print("\nFilling Missing Data with 0:")
df_filled = df_nan.fillna(0)
print(df_filled)

# Handle missing data using .dropna()
print("\nDropping Rows with Any Missing Data:")
df_dropped = df_nan.dropna()
print(df_dropped)

# Create two DataFrames to demonstrate merging
df1 = pd.DataFrame({"Key": [1, 2, 3], "Value1": ["A", "B", "C"]})
df2 = pd.DataFrame({"Key": [2, 3, 4], "Value2": ["D", "E", "F"]})

# Merge DataFrames
print("\nMerging DataFrames on 'Key':")
merged_df = pd.merge(df1, df2, on="Key", how="inner")  # Use 'outer', 'left', or 'right' as needed
print(merged_df)

# Demonstrating join with a common index
df1 = df1.set_index("Key")
df2 = df2.set_index("Key")
print("\nJoining DataFrames by Index:")
joined_df = df1.join(df2, how="inner")
print(joined_df)
