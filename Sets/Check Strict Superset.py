# def checkstrict():
#     x = set(input().split())
#     for _ in range(int(input())):
#         a = set(input().split())
#         if (x.issuperset(a) == False):
#             return False
#     return True
# x=checkstrict()
# print(x)


x=set(input().split())
print(all(x.issuperset(set(input().split()))for _ in range(int(input()))))
