i = 1
b=[1,2,3,4]
c =[]

def reversee(c, i):
    d=[5]*(len(b))
    for a in range(len(b)):
        d[a]=b[len(b)-a-1]
    return d
c = reversee(c, i)
print(c)