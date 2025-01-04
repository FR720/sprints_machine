import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Sample dataset for demonstration
data = pd.DataFrame({
    "Category": np.random.choice(["Group A", "Group B", "Group C"], size=100),
    "Values": np.random.normal(loc=50, scale=10, size=100),
})

# Box plot
plt.figure(figsize=(8, 5))
sns.boxplot(x="Category", y="Values", data=data)
plt.title("Box Plot of Values by Category", fontsize=14)
plt.xlabel("Category", fontsize=12)
plt.ylabel("Values", fontsize=12)
plt.show()

# Violin plot
plt.figure(figsize=(8, 5))
sns.violinplot(x="Category", y="Values", data=data, palette="muted")
plt.title("Violin Plot of Values by Category", fontsize=14)
plt.xlabel("Category", fontsize=12)
plt.ylabel("Values", fontsize=12)
plt.show()

# Categorical data visualization
# Bar plot
plt.figure(figsize=(8, 5))
sns.barplot(x="Category", y="Values", data=data, estimator=np.mean, ci=None, palette="pastel")
plt.title("Bar Plot (Mean Values by Category)", fontsize=14)
plt.xlabel("Category", fontsize=12)
plt.ylabel("Mean Values", fontsize=12)
plt.show()

# Count plot
plt.figure(figsize=(8, 5))
sns.countplot(x="Category", data=data, palette="bright")
plt.title("Count Plot of Categories", fontsize=14)
plt.xlabel("Category", fontsize=12)
plt.ylabel("Count", fontsize=12)
plt.show()

