import numpy
n,m,p= map(int,input().split())
l=[]
for _ in range(n+m):
    l.append(list(map(int,input().split())))
print(numpy.array(l))