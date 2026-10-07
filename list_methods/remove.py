i = 1
b=[1,2,3,4]
d =[]
done = False

def removee(c,i):
    c=[5]*(len(b)-1)
    for a in range(len(b)-1):
        c[a]=b[a]
        if b[a]==i:
            c[a]=b[a+1]
        c[(len(b)-2)]=b[len(b)-1]
    return c
d = removee(d,2)
print(d)