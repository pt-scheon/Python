n=int(input())
c='H'
for i in range(0,n):
    print(((i*2+1)*c).center(n*2-1))

#pillar
for i in range(n+1):
    print((" "*((n-1)//2)+c*n+" "*3*n+c*n))
#middle
for i in range((n+1)//2):
    print(" "*((n-1)//2)+(c*5*n))
#bottom pillar
for i in range(n+1):
    print((" "*((n-1)//2)+c*n+" "*3*n+c*n))
for i in range(0,n):
     print(" "*((4*n))+(((n*2-1)-(i*2))*c).center(n*2-1))
    
