n=4
a={1,2,3,4}
m=4
b={1,7,8,2}
l=sorted(a.difference(b).union(b.difference(a)))
print(*l,sep="\n")
