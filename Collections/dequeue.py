'''
6
append 1
append 2
append 3
appendleft 4
pop
popleft

Sample Output : 1 2
'''
from collections import deque
d = deque()
for _ in range(int(input())):
    s=input().split()
    eval('d.'+s[0]+"("+''.join(s[1:])+")")
print(*d)