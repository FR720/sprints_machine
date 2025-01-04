import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Generate random 3D data
np.random.seed(42)  # For reproducibility
x = np.random.rand(100) * 10
y = np.random.rand(100) * 10
z = np.random.rand(100) * 10
colors = np.sqrt(x**2 + y**2 + z**2)  # Color mapping based on distance from origin

# Create a 3D scatter plot
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot 3D scatter points
scatter = ax.scatter(
    x, y, z, c=colors, cmap="viridis", marker="o", s=50, alpha=0.8
)

# Label axes
ax.set_title("3D Scatter Plot", fontsize=14)
ax.set_xlabel("X Axis", fontsize=12)
ax.set_ylabel("Y Axis", fontsize=12)
ax.set_zlabel("Z Axis", fontsize=12)

# Add a color bar for context
cbar = fig.colorbar(scatter, ax=ax, shrink=0.5, aspect=10)
cbar.set_label("Distance Magnitude", fontsize=10)

# Save the plot as an image
plt.savefig("3d_scatter_plot.png")
plt.show()
