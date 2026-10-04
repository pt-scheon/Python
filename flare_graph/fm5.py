import numpy as np
import matplotlib.pyplot as plt
import math as m
import itertools



rx,ry=map(int,input("red flare: ").split())
bx,by=map(int,input("blue flare: ").split())
gx,gy=map(int,input("green flare: ").split())
auvx,auvy = map(int, input("coords of auv: ").split())
obstacle_count=int(input("no. of obstacles: "))
e=[]
for i in range(obstacle_count):
    e.append(tuple(map(int,input(f"coords of {i}th obstacle: ").split())))
obstacle=np.array(e)





auv=(auvx, auvy)
rf=(rx,ry)
bf=(bx,by)
gf=(gx,gy)
flares=[rf,gf,bf]
def dist(a,c):
    return m.hypot(a[0]-c[0],a[1]-c[1])
final=[]
min_d=float('inf')

for p in itertools.permutations(flares):
    d=0
    curr=auv
    for f in p:
        d+=dist(curr, f)
        curr=f
    if d<min_d:
        min_d=d
        final=list(p)
print(final)
path=[auv]+final

x_coords=[]
y_coords=[]
def in_path(a, b, ob):
    return abs(dist(a, ob) + dist(ob,b)-dist(a, b))<1e-6

    
for i in range(len(path)-1):
    start=path[i]
    end=path[i+1]
    
    x_coords.append(start[0])
    y_coords.append(start[1])


    obstacles=[q for q in obstacle if in_path(start, end, q)]
    
    obstacles.sort(key=lambda q: dist(start, q))

    for q in obstacles:

        dx = end[0]-start[0]
        dy = end[1]-start[1]

        length=m.hypot(dx, dy)
        a=5
        if length>0:
            perp_dx= -dy/length
            perp_dy= dx/length

            detour_x=q[0]+(1.216/length)*2.828
            detour_y=q[1]
            
            x_coords.append(detour_x)
            y_coords.append(detour_y)

x_coords.append(path[-1][0])
y_coords.append(path[-1][1])

xobs=[point[0] for point in e]
yobs=[point[1] for point in e]



plt.plot(x_coords, y_coords, label="path", color="cyan",linewidth=2)
color_map={auv:"black",rf:"red",bf:"blue",gf:"green"}
colors=[color_map[point] for point in path]

x_orig = [p[0] for p in path]
y_orig = [p[1] for p in path]

plt.scatter(x_orig,y_orig,c=colors,s=50,zorder=5)
if len(e)>0:
    plt.scatter(xobs,yobs,c="grey",s=50)
plt.title("PATH OF AUV")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.show()