import numpy as np
#prob should sum to 1
#prob length = array length
np.random.seed(2345)
print(np.random.choice(([1,2,3,4,5,6]),size=20,replace=True,p=[0.05,0,0.2,0.4,0.3,0.05]))
print(np.random.uniform(1,3,(2,2)))




#only on first axis
# print(np.random.permutation([[1,2,3],[6,2,1]]))


















# g=np.array([[1,2,3],[2,5,1],[6,8,2]])
# g[g==2]=0
# print(g)


# h=np.array([True,False,True])

# ##indexing as r,c but r1,c1 and r2,c2...
# x = np.array( [[1, 2], [3, 4], [5, 6]] )
# print( x[[0, 1, 2], [0, 0, 1]] )




#transpose
# a=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(np.transpose((a)))



#reshape
# a=np.array([[1,2,3,4],[5,6,7,8]])
# print(a.reshape((4,2),order="C"))
# print(a.reshape((4,2),order="F"))
##use -1 if u dont know the next dimension 
##creates copy






#BROADCASTINGGGGG
# np.random.seed(1111)
# A = np.random.randint(low = 1, high = 10,size = (3, 1, 4))
# B = np.random.randint(low = 1, high = 10,size=(2,1))
# print(A)
# print(B)
# print(A+B)

#4*2 ki 3 matrices 







# print(np.linspace(start=[4,8,12],stop=[100,100,100],num=20))





# import numpy as np
# dailywts =185 - (np.arange(5*7))/5
# print(len(dailywts))
# avg=np.zeros((5))
# for i in range(len(dailywts)):
#     avg[i//7] += dailywts[i]/7
# print(avg)
