x,k = map(int,input().split())
if(eval(input().replace('x',str(x)))==k):
    print("True")
else:
    print("False")