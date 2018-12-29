# string_input=input()
# lower=[]
# upper=[]
# digiteven=[]
# digitodd=[]
# for i in string_input:
#     if(i.islower()):
#         lower.append(i)
#     elif(i.isupper()):
#         upper.append(i)
#     elif(i.isdigit()and int(i)%2==0):
#         digiteven.append(i)
#     elif(i.isdigit()and int(i)%2!=0):
#         digitodd.append(i)
# s=*sorted(lower),*sorted(upper),*sorted(digitodd),*sorted(digiteven)
# print(''.join(s))
myList = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1357902468"
print(*sorted(input(), key = myList.index), sep ="")