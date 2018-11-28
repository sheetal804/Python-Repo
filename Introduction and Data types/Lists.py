x=['insert', '0', '5']
#print(x[0])
'''

n = input()
l = []
for _ in range(n):
    s = raw_input().split()
    cmd = s[0]
    args = s[1:]
    if cmd !="print":
        cmd += "("+ ",".join(args) +")"
        eval("l."+cmd)
    else:
        print l
        12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
'''
list = []
if(x[0]=="print"):
    print(list)
elif(len(x[0])>3):
    print(eval("list.{0}({1}, {2})".format(x[0], x[1], x[2])))
else:
    print("h")
