import math
n = int(input(""))
r = n  
for y in range(r, -r-1, -1):
    for x in range(-2*r, 2*r+1):
        dist = round(math.sqrt((x / 2) **2+y**2))
        if dist==r:
            print("*", end="")
        elif dist<r:
            x2 = round(x / 2)
            c = (x2==0 or y==0)
            d = (x2 == y or x2 == -y)
            if c or d:
                if d:
                    dd = math.sqrt(x2**2 + y**2)
                    if dd > r:
                        print(" ", end="")
                        continue
                print("*", end="")
            else:
                print(" ", end="")
        else:
            print(" ", end="")
    print()