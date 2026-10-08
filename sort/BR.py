def bubble(a, n):
    if n == 1:
        return

    for i in range(n-1):
        if a[i]>a[i+1]:
            a[i],a[i+1] = a[i+1], a[i]
    bubble(a, n-1)
    return a
c=[4,7,3,2]
print(bubble(c,len(c)))