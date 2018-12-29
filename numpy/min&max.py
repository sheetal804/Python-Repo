import numpy as np
np.set_printoptions(sign=' ')
n,m=map(int,input().split())
l=[]
for _ in range(n):
    l.append(list(map(int,input().split())))
print(np.max(np.min(np.array(l),axis=1)))


import numpy as np
np.set_printoptions(sign=' ')
n=int(input())
l=[]
for _ in range(n):
    l.append(list(map(int,input().split())))
a=np.array(l)
l=[]
for _ in range(n):
    l.append(list(map(int,input().split())))
b=np.array(l)
print(np.prod(a,b))