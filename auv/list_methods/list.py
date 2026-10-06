lenList=int(input())
b=[]
for u in range(lenList):
    x=int(input())
    b.append(x)

def clear(c):
    d=[]
    return d
def appendd(b, i):
    c=[5]*(len(b)+1)
    for a in range(len(b)):
        c[a]=b[a]
    c[len(b)] = i
    return c
def insertt(b,f,i):
    d=[5]*(len(b)+1)
    for a in range(len(b)-1,-1,-1):
        if a < f:
            d[a]=b[a]
        else:
            d[a+1]=b[a]
    d[f]=i
    return d
def popp(b):
    d=[5]*(len(b)-1)
    for a in range(len(b)-1):
        d[a]=b[a]
    return d
def removee(b,i):
    c=[5]*(len(b)-1)
    x=0
    done=False
    for a in range(len(b)):
        if b[a] == i and done==False:
            done=True
            continue
        if x<len(c):
            c[x]=b[a]
            x=x+1
    return c
def reversee(b):
    d=[5]*(len(b))
    for a in range(len(b)):
        d[a]=b[len(b)-a-1]
    return d
def sortt(b):
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
N = int(input())
a=[]
for _ in range(N):
    func, *line = input().split()
    if func=="insert":
        c=int(line[0])
        d=int(line[1])
        b=insertt(b,c,d)
    elif func=="append":
        s=int(line[0])
        b=appendd(b,s)
    elif func=="reverse":
        b=reversee(b)
    elif func=="sort":
        b=sortt(b)
    elif func=="pop":
        b=popp(b)
    elif func=="remove":
        c=int(line[0])
        b=removee(b,c)
    elif func=="print":
        print(b)
    print(b)
