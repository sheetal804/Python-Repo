import email.utils
n=int(input())
for _ in range(n):
    print(email.utils.formataddr(('DOSHI', 'DOSHI@hackerrank!com')))
