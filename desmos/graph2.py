import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider,Button

x=np.arange(-10000,10000)
y=x**2
fig,ax=plt.subplots()
plt.subplots_adjust(left=0.25)
plt.subplots_adjust(bottom=0.35)
axS=plt.axes([0.1, 0.25, 0.05, 0.5])
axl=plt.axes([0.25,0.2,0.65,0.1])
# axB=plt.axes([0.3,0.1,0.1,0.1])

scale=Slider(ax=axS,valmin=0.1,valmax=10,label="Scale slider",valinit=5,orientation="vertical")
l2r=Slider(ax=axl,valmin=-10,valmax=10,label="Left to right",valinit=0,orientation="horizontal")
# button=Button(ax=axB,label="button",color="grey",hovercolor="green")


line,=ax.plot(x, x**2)

ax.set_ylim(0,50000)
ax.set_xlim(-300,300)

base_xticks = np.arange(-300,301,100)
base_yticks = np.arange(0,50001,10000)

def update(val):

    a=scale.val
    h=l2r.val
    
    line.set_ydata(a*(x)**2)
    ax.set_xlim(-300/a,300/a)
    ax.set_ylim(0,50000/(a**2))
    # plt.xticks(a*(x-h*100)**2)
    fig.canvas.draw_idle()

scale.on_changed(update)
l2r.on_changed(update)
# button.on_clicked(update)
plt.show()





    # if button:
    #     line.set_ydata(a*(x-h*100)**3)
    #     ax.set_xlim(-300,300)
    #     ax.set_ylim(-20000,20000)