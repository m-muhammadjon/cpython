from datetime import date as dt

n = int(input())
data = dict()
out = dict()
for _ in range(n):
    name, date = map(str, input().split())
    data[name] = date.split('/')
    out[name] = 0
for name1, date1 in data.items():
    for name2, date2 in data.items():
        if name1 != name2:
            d1 = dt(int(date1[2]), int(date1[1]), int(date1[0]))
            d2 = dt(int(date2[2]), int(date2[1]), int(date2[0]))
            if abs((d1 - d2).days) <= 102 or date1[2] == date2[2]:
                out[name1] += 1

for key, value in out.items():
    print(key, value)
