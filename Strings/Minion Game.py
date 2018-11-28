s="BANANA"
s=s.lower()
Kevin=0
Stuart =0
vowels="aeiou"
for i in range(len(s)):
    if(s[i] in vowels):
        Kevin+= len(s)-i
        print("charter=",s[i],"Kevin=",Kevin)
    else:
        Stuart+=len(s)-i
        print("charter=",s[i],"Stuart=",Stuart)
if(Kevin>Stuart):
    print("Kevin ",Kevin)
else:
    print("Stuart ",Stuart)
'''
Stuart 12
Stuart 12

'''