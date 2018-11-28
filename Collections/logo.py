'''
aabbbccde

Ouput:
b 3
a 2
c 2

Explanation:
aabbbccde
Here, b occurs 3 times. It is printed first.
Both a and c occur 2 times. So, a is printed in the second line and c in the third line because a comes before c in the alphabet.

Note: The string S has at least 3 distinct characters.

from collections import Counter, OrderedDict

class OrderedCounter(Counter, OrderedDict):
    pass
[print(*c) for c in OrderedCounter(sorted(input())).most_common(3)]
'''
from collections import Counter,OrderedDict
import operator
s=sorted(input())
d=dict(sorted(Counter(s).items(), key= operator.itemgetter(1), reverse= False)[0:3])
for i,y in d.items():
    print(i,y)


