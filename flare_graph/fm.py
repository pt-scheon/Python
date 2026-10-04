import numpy as np
import matplotlib.pyplot as plt
import math as m

rx,ry=map(int,input("red flare: ").split())
bx,by=map(int,input("blue flare: ").split())
gx,gy=map(int,input("green flare: ").split())
auvx,auvy = map(int, input("coords of auv: ").split())
auv=(auvx, auvy)
r=(rx,ry)
b=(bx,by)
gf=(gx,gy)
flares=[r,gf,b]
def dist(a,c):
    return m.hypot(a[0]-c[0],a[1]-c[1])
q=[]
final=[]
num_steps=len(flares)
for p in range(num_steps):
    q=[]
    for i in range(len(flares)):
        q.append([dist(flares[i],auv),flares[i]])
    q.sort(key=lambda x: x[0],reverse=True)
    c=q.pop()
    auv=c[1]
    final.append(auv)
    flares.remove(auv)
print(final)       


