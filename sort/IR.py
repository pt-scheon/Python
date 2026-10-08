def insertion(a, p):
    if p==len(a):
        return a
    t=a[p]
    q = p-1
    while q>=0 and a[q]>t:
        a[q+1]=a[q]
        q-=1
    a[q+1]=t
    return insertion(a,p+1)


c = [4,7,3,2]
print(insertion(c, 1))