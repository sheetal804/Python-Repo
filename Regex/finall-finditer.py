# import re
# re.findall(r'\w','http://www.hackerrank.com/')
#
# import re
# re.finditer(r'\w','http://www.hackerrank.com/')
# map(lambda x: x.group(),re.finditer(r'\w','http://www.hackerrank.com/'))
#

import re
s = '[qwrtypsdfghjklzxcvbnm]'
a=re.findall('(?<=[qwrtypsdfghjklzxcvbnm])([aeiou]{2,})[qwrtypsdfghjklzxcvbnm]',input(),re.I)
#a = re.findall('(?<=' + s +')([aeiou]{2,})' + s, input(),re.I)
#print(a)
print('\n'.join(a or ['-1']))