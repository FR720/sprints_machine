import pandas as pd
import numpy as np

# Create a DataFrame with random data
np.random.seed(42)
data = np.random.randint(10, 100, size=(10, 4))
columns = ["A", "B", "C", "D"]
df = pd.DataFrame(data, columns=columns)
print("Original DataFrame:")
print(df)

# Calculate column-wise sum using NumPy
column_sum = np.sum(df, axis=0)
print("\nColumn-wise Sum:")
print(column_sum)

# Add a new column as the average of columns 'A' and 'B'
df["A_B_Average"] = np.mean(df[["A", "B"]], axis=1)
print("\nDataFrame with A_B_Average Column:")
print(df)

# Calculate row-wise maximum
df["Row_Max"] = np.max(df, axis=1)
print("\nDataFrame with Row-wise Max Column:")
print(df)

# Perform aggregation using both Pandas and NumPy
aggregated_data = {
    "Mean": np.mean(df["A"]),
    "Median": np.median(df["A"]),
    "Variance": np.var(df["A"]),
    "Std Dev": np.std(df["A"])
}
print("\nStatistical Aggregation on Column 'A':")
print(aggregated_data)

# Standardize the data
df_standardized = (df - np.mean(df)) / np.std(df)
print("\nStandardized DataFrame:")
print(df_standardized)
