import numpy as np
np.set_printoptions(sign=' ')
n,m=map(int,input().split())
l=[]
for i in range(n):
    l.append(list(map(int,input().split())))
print(np.product(np.sum(np.array(l),axis=0)))

