import matplotlib.pyplot as plt
import numpy as np
x=np.array(np.arange(50))
y=np.array(np.arange(0,100,2))


plt.plot(x,y,color="red",linewidth="3",ls=":",alpha=0.5,marker="o",label="line",ms=2)
#shorthand notation
#fmt="[color],[marker],[line]"
#Ro--
plt.xlabel("Sensor Readings", 
           fontsize=14,          # Text size
           fontweight='bold',    # 'normal', 'bold', 'heavy', 'light'
           color='navy',         # Text color
           fontstyle='italic')

plt.title("Graph", fontdict={"fontname": "cursive"})

plt.scatter(x, y, 
            s=100,           # Set all points to size 100
            c='green',       # Set all points to green
            marker='^',      # Use triangles
            edgecolors='k')
#fig, figsize*dpi=no.of pixels so figsize is ratio
fig = plt.figure(figsize=(6, 4), dpi=200, facecolor='lightgray', edgecolor='red', linewidth=5)

#major ticks and minor ticks in axes
#it automatically resizes
plt.xticks([np.arange(50)])
plt.yticks([np.arange(0,100,2)])

#saving
plt.savefig("mygraph.png",dpi=200)

#bar chart
plt.bar(["A","B","C"],[1,4,2])

#lim
plt.xlim(start=0,stop=100)

plt.legend()
plt.show()

