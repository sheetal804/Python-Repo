import textwrap
def merge(s,k):
    s1=textwrap.wrap(s,k)
    for item in s1:
        l = textwrap.wrap(item, 1)
        print(''.join((set(l))))


if __name__ == '__main__':
    s="AABCAAADA"
    k=3
    print(merge(s,k))