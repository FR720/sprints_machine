import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# Sample data for correlation heatmap
np.random.seed(42)
corr_data = pd.DataFrame({
    "Feature A": np.random.rand(100),
    "Feature B": np.random.rand(100),
    "Feature C": np.random.rand(100) * 0.8 + 0.2,
    "Feature D": np.random.rand(100) + 0.5,
})

# Calculate correlation matrix
correlation_matrix = corr_data.corr()

# Heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm", cbar=True)
plt.title("Correlation Heatmap", fontsize=14)
plt.show()

