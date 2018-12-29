import numpy
n,m = map(int,input().split())
l=[]
for _ in range(n):
    l.append(list(map(int,input().split())))
print(numpy.transpose(numpy.array(l)))
print(numpy.array(l).flatten())