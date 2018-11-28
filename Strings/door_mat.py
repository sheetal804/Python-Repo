n=9
m=27
'''
------------.|.------------              =12,9,6,3---    =1,3,5,7
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---             =7,5,3,1
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------
thickness=5
c='H'
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))
'''
c='-'
c1='.|.'
k=int((m-3)/2)
k1=1
cal=int((m-7)/2)
for i in range(1,n+1):
    if(i==(int(n/2)+1)):
        print((c*cal).rjust(1)+"WELCOME"+(c*cal).ljust(1))
        k=3
        k1=n-2
    elif(i<=int(n/2)):
        print((c*k).rjust(1)+(c1*k1).center(1)+(c*k).ljust(1))
        k=k-3
        k1=k1+2
    elif(i>=(int(n/2))):
        print((c * k).rjust(1) + (c1 * k1).rjust(1) + (c * k).ljust(1))
        k=k+3
        k1=k1-2