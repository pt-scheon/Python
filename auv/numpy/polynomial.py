import numpy as np
degree=int(input("enter the degree of polynomial "))
q=[]
for i in range(degree+1):
    q.append(int(input()))
coefficients=np.array(q)
roots=np.polynomial.Polynomial(coefficients).roots()
print("roots are:",roots)