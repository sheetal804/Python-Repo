from itertools import groupby
data='1222311'
print(*[(len(list(k)),int(g)) for g,k in groupby(data)])
# for g,k in groupby(data):
#     print(len(list(k)),g)