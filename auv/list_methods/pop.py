a = 1
b=[1,2,3,4]
c =[]

def popp(c):
    d=[5]*(len(b)-1)
    for a in range(len(b)-1):
        d[a]=b[a]
    return d
c = popp(c)
print(c)