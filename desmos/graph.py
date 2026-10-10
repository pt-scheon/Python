import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# 1. Setup the data
x = np.arange(-10000, 10000)
initial_scale = 1.0

fig, ax = plt.subplots(figsize=(8, 6))
plt.subplots_adjust(bottom=0.25) 

line, = ax.plot(x, initial_scale * (x**2), lw=2)
ax.set_title("y = scale * x²")

ax_slider = plt.axes([0.25, 0.1, 0.65, 0.03]) 
scale_slider = Slider(
    ax=ax_slider,
    label='Scale',
    valmin=0.1,
    valmax=5.0,
    valinit=initial_scale
)

def update(val):
    current_scale = scale_slider.val
    line.set_ydata(current_scale * (x**2))  
    ax.relim()
    ax.autoscale_view()
    fig.canvas.draw_idle()
scale_slider.on_changed(update)

plt.show()