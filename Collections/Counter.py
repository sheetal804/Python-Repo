'''
10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50
Explanation

Customer 1: Purchased size 6 shoe for $55.
Customer 2: Purchased size 6 shoe for $45.
Customer 3: Size 6 no longer available, so no purchase.
Customer 4: Purchased size 4 shoe for $40.
Customer 5: Purchased size 18 shoe for $60.
Customer 6: Size 10 not available, so no purchase.

Total money earned =  200
'''
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

