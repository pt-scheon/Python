def selection(a, i):
    if i==len(a):
        return a
    min=i
    for j in range(i+1, len(a)):
        if a[j]<a[min]:
            min=j
    a[i], a[min] = a[min], a[i]
    return selection(a,i+1)

c = [4,7,5,6,3,2]
print(selection(c, 0))