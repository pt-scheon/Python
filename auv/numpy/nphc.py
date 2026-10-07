import numpy as np
import numpy as np

n=int(input("No. of equations: "))
v=int(input("Enter the no. of variables: "))
q=[]
for i in range(n):
    print(f"Equation {i+1}:")
    row = []
    for g in range(v+1): 
        val = float(input(f"Enter value {g+1}: "))
        row.append(val)
    q.append(row)
matrix = np.array(q)
lt=np.tril(matrix[:,:v],k=-1)
print(matrix)
rank_A = np.linalg.matrix_rank(matrix[:, :v])
rank_Ab = np.linalg.matrix_rank(matrix)
if rank_A<rank_Ab:
    print("No sol")
elif rank_A<v:
    print("Infinite solutions")
else:
    while np.any(lt!=0):
        if matrix[0,0]!=1:
            matrix[0,:]=matrix[0,:]/matrix[0][0]
        else:
            coords=np.argwhere(lt)
            for r,c in coords:
                factor=matrix[r,c]/matrix[c,c]
                matrix[r,:]=matrix[r,:]-(factor*matrix[c, :])
                print(matrix)
                lt=np.tril(matrix[:, :v], k=-1)
    x = np.zeros(v)
    for i in range(v-1,-1,-1):
        x[i] = (matrix[i, v]-np.dot(matrix[i, i+1:v], x[i+1:v]))/matrix[i,i]
    for i in range(v):
        print(f"value of variable {i+1} is {x[i]}")
