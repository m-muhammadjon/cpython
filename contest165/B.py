def hosil(a, b, yil, cnt=0):
    if cnt == yil:
        return a + b
    cnt += 1
    return hosil(3 * a + 2 * b, 2 * a + 2 * b, yil, cnt)


n = int(input())
print(hosil(1, 1, n) % (10 ** 9 + 7))
