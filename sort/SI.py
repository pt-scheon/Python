def selection(a):
    for i in range(len(a)):
        min=i
        for j in range(i+1, len(a)):
            if a[j]<a[min]:
                min=j

        a[i],a[min] =a[min],a[i]
    return a
b=[1,4,5,7,2,4]
print(selection(b))