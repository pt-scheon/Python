n = int(input())
a = list(map(int, input().split()))

a.sort()

for p in range(0, n-1):
    if a[p] != a[p+1]:
        print(a[p])
    
