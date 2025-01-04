import plotly.graph_objects as go
import numpy as np

# Sample Data
x = np.linspace(0, 10, 50)
y_line = np.sin(x)
y_scatter = y_line + np.random.normal(scale=0.2, size=len(x))

# Line Plot
line_fig = go.Figure()
line_fig.add_trace(go.Scatter(x=x, y=y_line, mode='lines+markers', name='Sine Wave', line=dict(color='blue')))
line_fig.update_layout(
    title='Interactive Line Plot',
    xaxis_title='X-Axis',
    yaxis_title='Y-Axis',
    template='plotly_dark'
)
line_fig.write_html('line_plot.html')

# Scatter Plot
scatter_fig = go.Figure()
scatter_fig.add_trace(go.Scatter(x=x, y=y_scatter, mode='markers', name='Noisy Data', marker=dict(color='red')))
scatter_fig.update_layout(
    title='Interactive Scatter Plot',
    xaxis_title='X-Axis',
    yaxis_title='Y-Axis',
    template='plotly_white'
)
scatter_fig.write_html('scatter_plot.html')

print("Plots saved as HTML!")
