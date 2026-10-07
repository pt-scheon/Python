import math

r = int(input(""))

for y in range(r,-r-1,-1):
    for x in range(-2*r,2*r+1):
        if round(math.sqrt((x / 1.96) ** 2 + y ** 2))== r:
            print("*", end="")
        else:
            print(" ", end="")
    print()