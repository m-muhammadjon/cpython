n = int(input())
if n < 0:
    n = 2 ** 32 + n
s = '{:032b}'.format(n)
c = 0
ans = 0
for i in range(0, 32):
    if s[i] == '1':
        c += 1
    else:
        ans = max(ans, c)
        c = 0
ans = max(c, ans)
print(ans)
