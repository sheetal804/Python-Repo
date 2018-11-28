'''
It's so we can't have the satisfaction of one-liners like
print(len(set(map(int, input().split()))|set(map(int, input().split()))))

e="(set(input().split())if input()!='-1'else '')";print(len(eval(e)|eval(e)))

16
 1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
 4
 intersection_update 10
 2 3 5 6 8 9 1 4 7 11
 update 2
 55 66
 symmetric_difference_update 5
 22 7 35 62 58
 difference_update 7
 11 22 35 55 58 62 66
'''

# n=int(input())
# h=set(map(int,input().split()))
n=10
h={1,2,3,4,5,6,7,8,9,10}
for i in range(int(input())):
    cmd,args=input().split()
    h1=set(map(int,input().split()))
    eval('h.'+cmd+'({})'.format(h1))
print(sum(h))
