for i in range(int(input())):
    a=int(input())
    a_set=set(map(int,input().split()))
    b=int(input())
    b_set=set(map(int,input().split()))
    if(a_set.difference(b_set)==set()):
        print("True")
    else:
        print("False")
'''
for _ in range(int(input())):
x, a, z, b = input(), set(input().split()), input(), set(input().split())
print(a.issubset(b))
'''
