
s=[['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41.0], ['Harsh', 39.0]]

'''

arr = map(int, input().split())
    new_arr = list(arr)[:n]
    z=max(new_arr)
    while max(new_arr) ==z:
        new_arr.remove(max(new_arr))
    print(max(new_arr))
'''
names,score=zip(*s)
names=list(names)
score=list(score)
z=min(score)
t=[]
while min(score)==z:
    score.remove(z)
minimum=min(score)
for i in range(len(s)):
    if(s[i][1]==minimum):
        t.append(s[i][0])
t.sort()
for word in t:
    print(word)