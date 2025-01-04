import matplotlib.pyplot as plt

# Data for line and scatter plots
x = range(1, 11)
y_line = [2 * n for n in x]  # Line plot values (2x)
y_scatter = [2 * n + (n % 3 - 1) * 4 for n in x]  # Scatter plot with variations

# Create a figure and axis
plt.figure(figsize=(10, 5))

# Line plot
plt.plot(x, y_line, label="Line Plot (y=2x)", color="blue", linestyle="--", marker="o")

# Scatter plot
plt.scatter(x, y_scatter, label="Scatter Plot", color="red", marker="x")

# Add titles and labels
plt.title("Basic Line and Scatter Plots", fontsize=14)
plt.xlabel("X-Axis", fontsize=12)
plt.ylabel("Y-Axis", fontsize=12)

# Add a legend
plt.legend()

# Display the plot
plt.grid(True)
plt.show()
