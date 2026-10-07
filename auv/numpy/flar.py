import numpy as np
import random
import math
import itertools

pool = np.zeros((16, 25), int)
auv = 1
# rx,bx,gx=random.randint(7, 15), random.randint(7, 15), random.randint(7, 15)
# ry,by,gy=random.randint(0,15),random.randint(0,15),random.randint(0,15)
rx, bx, gx=map(int, input("Enter rx bx gx: ").split())
ry, by, gy=map(int, input("Enter ry by gy: ").split())
f1 = (2,3)
f2 = (4,5)
f3 = (6,7)
f4 = (8,9)
f5 = (10,11)
f6 = (12,13)

l = [f1,f2,f3,f4,f5,f6]

#0 to 6
n = max(0, min(int(input("Enter n (0-6): ")), 6))
selected = l[:n]

r = (ry, rx)
g = (gy, gx)
b = (by, bx)

targets = [r,g,b]+selected
m = len(targets)

auv_in = list(map(int, input("AUV COORDS: ").split()))
auvy, auvx = auv_in[1]-1,auv_in[0] - 1
auv = (auvy, auvx)

def dist(a,b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])

initial_state=(auv,0)
#total cost, initial/prev state, target gone to
current_layer={initial_state:(0.0, None, None)}
trellis = [current_layer]

# trellis
for step in range(m):
    next_layer = {}
    
    for (curr_pos, mask), (cost,_,_) in current_layer.items():
        for i in range(m):
            #i check
            if not (mask & (1<<i)):
                next_pos=targets[i]
                move_cost=dist(curr_pos, next_pos)          
                new_mask = mask | (1 << i)
                new_state=(next_pos,new_mask)
                total_cost=cost+move_cost

                # shortest path 
                if (new_state not in next_layer) or (total_cost<next_layer[new_state][0]):
                    next_layer[new_state] = (total_cost,(curr_pos,mask),next_pos)

    current_layer = next_layer
    trellis.append(current_layer)


    #final state with min cost
    best_final_state = min(current_layer.keys(), key=lambda st: current_layer[st][0])
    optimal_path=[]
    current_state=best_final_state
    
    #Backward 
    for layer_idx in range(len(trellis)-1,0,-1):
        cost,prev_state,target_visited = trellis[layer_idx][current_state]
        optimal_path.append(target_visited)
        current_state=prev_state
        
    optimal_path.reverse()

    def update_markers():
        pool[r[0]][r[1]] = 3
        pool[g[0]][g[1]] = 4
        pool[b[0]][b[1]] = 5
        for idx, flare in enumerate(selected):
            pool[flare[0]][flare[1]]=6+idx

    update_markers()

#path 
for target in optimal_path:
    targety,targetx=target
    print(f"visiting:{target}")
    pool[auvy, min(auvx,targetx):max(auvx,targetx)+1]=1
    pool[min(auvy, targety):max(auvy, targety) + 1, targetx] = 1
    update_markers()
    
    auvy,auvx=targety,targetx
    auv=(auvy,auvx)
    print(pool)