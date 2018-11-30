x,k = map(int,raw_input().split())
if(eval(raw_input().replace('x',str(x)))==k):
    print("True")
else:
    print("False")