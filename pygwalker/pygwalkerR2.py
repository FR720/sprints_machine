import plotly.express as px
import pandas as pd
import numpy as np

# Example Data for 3D Plot
df = pd.DataFrame({
    'x': np.random.rand(100),
    'y': np.random.rand(100),
    'z': np.random.rand(100),
    'size': np.random.rand(100) * 30,
    'color': np.random.choice(['A', 'B', 'C'], 100),
})

# 3D Scatter Plot
fig_3d = px.scatter_3d(
    df, x='x', y='y', z='z', color='color', size='size',
    title='Interactive 3D Scatter Plot',
    labels={'x': 'X-axis', 'y': 'Y-axis', 'z': 'Z-axis'}
)
fig_3d.write_html('3d_scatter_plot.html')

print("3D Plot saved as HTML!")
