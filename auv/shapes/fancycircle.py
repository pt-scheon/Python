import math
n=int(input())
r=n 
scale=2.0 
for y in range(r, -r - 1, -1):
    for x in range(int(-r * scale), int(r * scale) + 1):
        dist = math.sqrt((x / scale)**2 + y**2)
        diff = abs(dist-r)
        if diff < 0.15:
            print("@", end="") 
        elif diff < 0.35:
            print("#", end="")
        elif diff < 0.55:
            print("+", end="") 
        elif diff < 0.75:
            print(":", end="") 
        elif diff < 0.95:
            print(".", end="")
        else:
            print(" ", end="")          
    print()