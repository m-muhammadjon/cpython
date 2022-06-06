from decimal import getcontext, Decimal

getcontext().prec = 5
n = int(input())
xs = list(map(int, input().split()))
ys = list(map(int, input().split()))
s = 0
for i in range(n):
    s += abs(xs[i] - ys[i]) ** 2
print(Decimal(s) ** Decimal(0.5))
