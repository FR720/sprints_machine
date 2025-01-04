import matplotlib.pyplot as plt
import numpy as np

# Data for bar plot
categories = ["A", "B", "C", "D"]
values = [15, 25, 35, 20]

# Data for histogram
data = np.random.normal(50, 10, 500)  # Normally distributed data

# Create a figure with subplots
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# Bar plot
axes[0].bar(categories, values, color=["blue", "green", "red", "orange"])
axes[0].set_title("Bar Plot", fontsize=14)
axes[0].set_xlabel("Categories", fontsize=12)
axes[0].set_ylabel("Values", fontsize=12)
axes[0].grid(True)

# Adding annotation to highlight max value
max_value_index = values.index(max(values))
axes[0].annotate(
    f"Max: {max(values)}",
    xy=(categories[max_value_index], values[max_value_index]),
    xytext=(categories[max_value_index], values[max_value_index] + 5),
    arrowprops=dict(facecolor="black", arrowstyle="->"),
    fontsize=10,
)

# Histogram
axes[1].hist(data, bins=20, color="purple", edgecolor="black", alpha=0.7)
axes[1].set_title("Histogram", fontsize=14)
axes[1].set_xlabel("Value Range", fontsize=12)
axes[1].set_ylabel("Frequency", fontsize=12)
axes[1].grid(True)

# Adjust layout and display the plots
plt.tight_layout()
plt.show()
