lenList=int(input())
b=[]
for u in range(lenList):
    u=int(input())
    b.append(u)
d=[]
def sortt(c):
    c=[5]*(len(b))
    for p in range(len(b)):
        for a in range(len(b)-1):
            if b[a]>b[p] and a>p:
                b[a], b[p] = b[p], b[a]
                c[a]=b[a]
                c[p]=b[p]
            elif b[a]>b[p] and a<p:
                c[a]=b[a]
                c[p]=b[p]
            elif b[a]<b[p] and a>p:
                c[a]=b[a]
                c[p]=b[p]
            elif b[a]<b[p] and a<p:
                b[a], b[p] = b[p], b[a]
                c[a]=b[a]
                c[p]=b[p]
            else:
                c[a]=b[a]
                c[p]=b[p]
    return c
d = sortt(d)
print(d)