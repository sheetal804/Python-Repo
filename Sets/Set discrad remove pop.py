'''
9
1 2 3 4 5 6 7 8 9
10
pop
remove 9
discard 9
discard 8
remove 7
pop
discard 6
remove 5
pop
discard 5
'''

n=int(input())
l=set(map(int,input().split()))
for i in range(int(input())):
    eval('l.{0}({1})'.format(*input().split()+['']))
    eval('s.{0}({1})'.format(*input().split() + ['']))
print(sum(l))

