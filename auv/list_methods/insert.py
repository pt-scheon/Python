i = 1
b=[1,2,3,4]
c =[]

def insertt(c,f,i):
    d=[5]*(len(b)+1)
    for a in range(len(b)-1):
        if a<f:
            d[a]=b[a]
        else:
            d[a]=b[a-1]
    d[f] = i
    return d
c = insertt(c,2,i)
print(c)