if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    new_arr = list(arr)[:n]
    z=max(new_arr)
    while max(new_arr) ==z:
        new_arr.remove(max(new_arr))
    print(max(new_arr))


