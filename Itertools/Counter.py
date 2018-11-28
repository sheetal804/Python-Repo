from collections import Counter
n=input()
l=Counter(list(map(int,input().split())))
s=0
for i in range(int(input())):
    size,price = map(int,input().split())
    if(l[size]>0):
        l[size]-=1
        s=s+price
print(s)