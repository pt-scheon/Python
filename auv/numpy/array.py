import numpy as np

array1 = np.array([[1,2,3],[4,5,6],[7,8,9]],dtype="int16")
array2=np.array([5,6,7])
a=[1,2,3,4,5,6]
b=[3]
print(a[1:-1])



#filling
print(np.zeros((2,3,3,2)))
print(np.full((2,3,3),8))
print(np.ones(4,4,2))

#inf
print(np.array(np.NINF,np.INF))
print(np.isneginf(a))
print(np.isposinf(a))

#nan or undefined
print(np.array([np.nan]))


#random
np.random.seed(1234)
print(np.random.rand(2,3,4,3))
print(np.random.randint(-1,3,(3,3)))
#prob should sum to 1
#prob length = array length
print(np.random.choice(([1,2,3,4,5,6]),size=20,replace=True,p=[0.05,0,0.2,0.4,0.3,0.05]))
print(np.random.shuffle([[1,2,3],[6,2,1]]))

print(np.repeat(np.random.randint(1,4,(3,3)),2))



#range
print(np.arange(start=1,stop=10,step=1))
print(np.linspace(start=[4,8,12],stop=[100,100,100],num=20))


#stats
##same with all log,exp, etc fun how to use
print(np.sum(array1))
#if there is a nan in func then print(np.sum(array1,where=-np.isnan(array1)))
#or np.nan(np.nan_to_num(array1))
#or np.nansum(array1)
print(np.max(array1))
print(np.min(array1))

#vstack
print(np.vstack([array1,array2]))

#hstack
print(np.hstack([array2,a]))


#boolean indexing
g=np.array([[1,2,3],[2,5,1],[6,8,2]])
g[g==2]=0
print(g)
#(gives elements which are true)
names = np.array(["Dennis","Dee","Charlie", "Mac","Frank"])
ages = np.array([43, 44, 43, 42, 74])
genders = np. array(['male','female','male','male','male'])
c=names[ages>=44]
print(c)
m=names[(ages>42) & (genders=="male")]
print(m)
print(names[(genders=="female") | (ages<43)])

print(np.where(a,))

#matrix

#identity
print(np.identity(3))

# transpose: can change axes
s=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(np.transpose((s)))

#multiply
print(np.matmul(array1,array2))

#normal operations 
print(array1+3)

#matrix det
print(np.linalg.det(array1))

#wraps up elements after 999 places, default is 75
print(np.set_printoptions(linewidth=999))

#any or all for nan 
print(np.any(np.isnan(array1),axis=1))
print(np.all(np.isnan(array1),axis=0))


print(np.diag(a))
print(np.triu(a))
print(np.tril(a))