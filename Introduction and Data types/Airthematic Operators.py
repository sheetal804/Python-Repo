'''
Read two integers from STDIN and print three lines where:

The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers.
The first line should contain integer division,  a//b . The second line should contain float division,  a/b .
You don't need to perform any rounding or formatting operations.

'''
if __name__ == '__main__':
    a=int(input())
    b=int(input())
    print(a+b)
    print(a-b)
    print(a*b)
    print(a//b)
    print(a/b)

