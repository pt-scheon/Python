def insertion(a):
    for p in range(1,len(a)):
        t=a[p]
        q=p-1

        while q>=0 and a[q]>t:
            a[q+1]=a[q]
            q -= 1
        a[q+1]=t
    return a
c = [4,7,3,2]
print(insertion(c))