'''
5 2
a
a
b
a
b
a
b
Output:
1 2 4
3 5
Explanation:
a' appeared 3 times in positions 1,2  and 4.
'b' appeared 2 times in positions 3 and 5.
In the sample problem, if 'c' also appeared in word group B, you would print -1.
'''
from collections import defaultdict
l=defaultdict(list)
n,m = map(int,input().split())
for i in range(n):
    l[input()].append(i+1)
for _ in range(m):
    x=input()
    if(x in l):
        print(*l[x])
    else:
        print(-1)