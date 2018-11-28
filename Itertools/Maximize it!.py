import itertools
# k=3
# m=1000
# l1=[5,4]
# l2=[7,8,9]
# l3=[5,7,8,9,10]
# l1=[x**2 for x in (l1)]
# l2=[x**2 for x in (l2)]
# l3=[x**2 for x in (l3)]

n=[[5, 4], [7, 8, 9], [5, 7, 8, 9, 10]]
print(n)
print(list(itertools.product(n)))

# from itertools import product
# K,M = map(int,input().split())
# N = (list(map(int, input().split()))[1:] for _ in range(K))
# results = (sum(num**2 for num in numbers) % M for numbers in product(*N))
# print(max(results))
