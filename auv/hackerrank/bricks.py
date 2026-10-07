p=int(input())
r='H'
for i in range(0,p):
    print(((i*2+1)*r).center(p*2-1))

for i in range(p+1):
    print((r*p).center(p*2-1)+(" ")*13+(r*p).ljust(p))

for i in range(p-2):
    print((r*p*p).center((p*p)+(p-1)))

for i in range(p+1):
    print((r*p).center(p*2-1)+(" ")*13+(r*p).ljust(p))

for i in range(0,p):
    print(" "*((p*p)-p)+((9-(i*2))*r).center(p*2-1))
   
        

        