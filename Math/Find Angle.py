#n,m=int(input()),int(input())
from cmath import phase
n,m=10,10
x=complex(n,m)
print(phase(complex(n,int(abs(complex(n,m))/2))))
