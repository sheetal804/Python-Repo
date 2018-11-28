'''
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
'''
n=5
k=(n-1)*2
c='-'
p=1
for i in range(1,n*2):
    s=""
    for j in range(p):
        s = s + str(chr(ord('a') + (n - 1 - j))) + "-"
    s1 = (s[:-2])
    s2=s[:-1] + s1[::-1]
    if(i<n):
        print((c*k).rjust(1)+s2+(c*k).ljust(1))
        k=k-2
        p=p+1
    elif(i>n):
        print((c * k).rjust(1) +s2+ (c * k).ljust(1))
        k = k + 2
        p=p-1
    elif(i==n):
        print(s2)
        k=2
        p=p-1
