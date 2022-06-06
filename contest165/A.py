def f(n, cnt=0):
    if n == 1:
        return cnt
    cnt += 1
    if n % 2 == 1:
        return f(3 * n + 1, cnt)
    return f(n / 2, cnt)


n = int(input())
print(f(n))
