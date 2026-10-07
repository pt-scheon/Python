import matplotlib.pyplot as plt
import numpy as np
x=np.array(np.arange(0,50))
y=x**2

fig = plt.figure(figsize=(6, 4), dpi=250, facecolor='lightgray', edgecolor='black', linewidth=5)
plt.plot(x, y, color='blue', label='y = x²')
plt.legend()
plt.show()