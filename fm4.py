import numpy as np
import matplotlib.pyplot as plt
import itertools
import math



rx,ry=map(int,input("red flare: ").split())
bx,by=map(int,input("blue flare: ").split())
gx,gy=map(int,input("green flare: ").split())

confidenceR=float(input("confidence in Red flare: "))
confidenceB=float(input("confidence in Blue flare: "))
confidenceG=float(input("Confidence in Green flare: "))



auvx,auvy = map(int, input("coords of auv: ").split())
obstacle_count=int(input("no. of obstacles: "))
e=[]
for i in range(obstacle_count):
    e.append(tuple(map(int,input(f"coords of {i}th obstacle: ").split())))
obstacle=np.array(e)





auv=(auvx, auvy)
rf=(rx,ry,confidenceR)
bf=(bx,by,confidenceB)
gf=(gx,gy,confidenceG)
flares=[rf,gf,bf]
def dist(a,c):
    return math.hypot(a[0]-c[0],a[1]-c[1])
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
temp=[]
for flare in final:
    if flare[2]<0.75:
        temp.append(flare)
        final.remove(flare)

print(final)

path=[auv]+final+temp

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

        dx=end[0]-start[0]
        dy=end[1]-start[1]

        length=math.hypot(dx, dy)
        
        if length>0:
            fwd_dx=dx/length
            fwd_dy=dy/length
     
            perp_dx=-dy/length
            perp_dy=dx/length
    
            m=0.5  

            p1_x=q[0]-(fwd_dx*m)
            p1_y=q[1]-(fwd_dy*m)
 
            p2_x=p1_x+(perp_dx*m)
            p2_y=p1_y+(perp_dy*m)

            p3_x=p2_x+(fwd_dx*m*2)
            p3_y=p2_y+(fwd_dy*m*2)

            p4_x=q[0]+(fwd_dx*m)
            p4_y=q[1]+(fwd_dy*m)

            x_coords.extend([p1_x, p2_x, p3_x, p4_x])
            y_coords.extend([p1_y, p2_y, p3_y, p4_y])

x_coords.append(path[-1][0])
y_coords.append(path[-1][1])

xobs=[point[0] for point in e]
yobs=[point[1] for point in e]



plt.plot(x_coords, y_coords, label="path", color="cyan",linewidth=2)
color_map={auv:"black",rf:"red",bf:"blue",gf:"green"}
colors=[color_map[point] for point in path]

x_orig = [p[0] for p in path]
y_orig = [p[1] for p in path]

plt.scatter(x_orig,y_orig,c=colors,s=100,zorder=5)
if len(e)>0:
    plt.scatter(xobs,yobs,c="grey",s=100)
plt.title("PATH OF AUV")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.show()