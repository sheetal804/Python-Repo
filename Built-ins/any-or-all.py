'''
Input:
The first line contains an integer N. N is the total number of integers in the list.
The second line contains the space separated list of N integers.

Output
Print True if all the conditions of the problem statement are satisfied. Otherwise, print False.

Sample Input

5
12 9 61 5 14
Sample Output

True

Explanation

Condition 1: All the integers in the list are positive.
Condition 2: 5 is a palindromic integer.

Hence, the output is True.

Can you solve this challenge in 3 lines of code or less?
There is no penalty for solutions that are correct but have more than 3 lines.

'''
n=int(input())
l=list(map(int,input().split()))
print(all(i > 0 for i in l)and any(str(j)==''.join(reversed(str(j))) for j in l))
