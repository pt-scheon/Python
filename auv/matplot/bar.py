import matplotlib.pyplot as plt
import numpy as np
bars=plt.bar(["A","B","C"],[1,4,2])
#hatches and hatch values
bars[0].set_hatch("/")
bars[1].set_hatch("o")
bars[2].set_hatch("*")
plt.figure(figsize=(12.8,8),dpi=200,edgecolor="black",facecolor="turquoise")
plt.plot()
plt.show()