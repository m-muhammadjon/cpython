import sys;import math;q = sys.stdin.readlines()
p=[1 for i in range(0,1000)];p[0]=p[1]=0
for i in range(2,math.ceil(math.sqrt(1000))+1):
    for j in range(i*2,1000,i):p[j]=0
for x in q:
    for w in x.strip().split(' '):
        if w.strip() and p[int(w.strip())]==1:print(w, end=' ')
