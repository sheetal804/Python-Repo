# def isan(s):
#     for i in range(len(s)):
#         if(s[i].isalnum()):
#             return True
#     return
# def isa(s):
#     for i in range(len(s)):
#         if(s[i].isalpha()):
#             return True
#     return
# def isd(s):
#     for i in range(len(s)):
#         if(s[i].isdigit()):
#             return True
#     return
# def isl(s):
#     for i in range(len(s)):
#         if(s[i].islower()):
#             return True
#     return
# def isu(s):
#     for i in range(len(s)):
#         if(s[i].isupper()):
#             return True
#     return
if __name__ == '__main__':
    string = "q9A"
    # print(isan(s))
    # print(isa(s))
    # print(isd(s))
    # print(isl(s))
    # print(isu(s))
    print(any(s.isalnum() for s in string))
    print(any(s.isalpha() for s in string))
    print(any(s.isdigit() for s in string))
    print(any(s.islower() for s in string))
    print(any(s.isupper() for s in string))

