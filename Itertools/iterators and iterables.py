import itertools as it

s='a a c d'
s=s.replace(" ","")
k=2
c=0
p=list(it.combinations(sorted(s),k))
for i in p:
    if((set(i).__contains__('a'))==True):
        c+=1
print("{0:.4f}".format(c/len(p)))