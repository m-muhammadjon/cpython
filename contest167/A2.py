import math

n = int(input())

p = [1 for i in range(0, n + 1)]
p[0] = p[1] = 0
for i in range(2, math.ceil(math.sqrt(n)) + 1):
    for j in range(i * 2, n + 1, i):
        p[j] = 0
if p[n] == 1:
    print('Yahyobek')
else:
    print('Asilbek')

