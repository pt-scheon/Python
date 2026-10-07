n = int(input())
c = "*"
if n%2==0:
    for p in range(1, n+1, 2):
        print(" "*((n-p)//2)+c*((p+1)))
else:
    for p in range(0, n, 2):
        print(" "*((n-p)//2)+c*((p+1)))