n=2
w = len(bin(n)[2:])
for i  in range(n):
    print(str((i+1)).rjust(w),oct(i+1)[2:].rjust(w),hex(i+1)[2:].upper().rjust(w),bin(i+1)[2:].rjust(w),sep=" ")