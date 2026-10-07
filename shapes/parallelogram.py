n = int(input())
c = "*"

for p in range(-((n-1)//2),(n+1)//2):
    end_space=" "*((n-1-(2*p))//2)
    if p == -((n-1)//2):
        print(" " * (n-1) + c)
    elif p<0:
        print(" " * (-p+n-1-((n-1)//2)) + c + " " * (2 * (p + ((n-1)//2)) - 1) + c)
    if p==0:
        print(end_space+((c+" ")*((n//2)+1)))
    elif p==(((n+1)//2)-1):
        print(((c+" ")*((n//2)+1)))
    elif p>0 and p!=(((n+1)//2)-1): 
        print(" "*((n-1-(2*p)//2)-(n-1)//2) + c + " "*((2*p)-1)  + c + " "*(n-(2*(1+p))) + c + " "*p)
 
