'''
4
bcdef
abcdefg
bcde
bcdef

Output:
3
2 1 1

Explanation:
There are 3 distinct words. Here, "bcdef" appears twice in the input at the first and last positions.
The other words appear once each.
The order of the first appearances are "bcdef", "abcdefg" and "bcde" which corresponds to the output.
'''
from collections import OrderedDict
d=OrderedDict()
for _ in range(int(input())):
    item=input()
    d[item]=d.get(item,0)+1
print(len(d))
print(*d.values())