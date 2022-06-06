for i in range(9):
    s = list(map(int, input().split()))
    if 0 in s:
        print(45 - sum(s))
        exit()
