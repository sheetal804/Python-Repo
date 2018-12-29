import re
x=input()
print(x)
m = re.search(r'([a-zA-Z0-9])\1+', x)
print(m.group(1) if m else -1)