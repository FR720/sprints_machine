import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Seaborn theme setup
sns.set_theme(style="darkgrid", palette="muted")

# Sample data for line plot and scatter plot
x = np.linspace(0, 10, 50)
y_line = np.sin(x)  # Line plot data
y_scatter = y_line + np.random.normal(scale=0.2, size=len(x))  # Scatter plot with noise

# Line plot
plt.figure(figsize=(8, 5))
sns.lineplot(x=x, y=y_line, marker="o", label="Sine Wave", color="blue")
plt.title("Basic Line Plot with Seaborn", fontsize=14)
plt.xlabel("X-Axis", fontsize=12)
plt.ylabel("Y-Axis", fontsize=12)
plt.legend()
plt.show()

# Scatter plot
plt.figure(figsize=(8, 5))
sns.scatterplot(x=x, y=y_scatter, color="red", marker="x", label="Noisy Data")
plt.title("Scatter Plot with Seaborn", fontsize=14)
plt.xlabel("X-Axis", fontsize=12)
plt.ylabel("Y-Axis", fontsize=12)
plt.legend()
plt.show()

