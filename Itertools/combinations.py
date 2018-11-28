from itertools import combinations
# s,k=input().split()
#print(*[''.join(i) for i in combinations(sorted(s),int(k))],sep="\n")
k=3
s='HACK'
for i in range(int(k)+1):
    for j in combinations(sorted(s),i):
        print(''.join(j))