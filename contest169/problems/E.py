n, k = map(int, input().split())
days = list(map(int, input().split()))
cons = sorted(list(map(int, input().split())), reverse=True)
cnt = 1
days2 = []
for i in range(len(days) - 1):
    if days[i + 1] == 1:
        days2.append(cnt)
        cnt = 1
    else:
        cnt += 1
# if days[-1] == 1 and days.count(1) != 1:
days2.append(cnt)

print(days2)
days2 = sorted(days2, reverse=True)
res = 0
for x in cons:
    for item in days2:
        print(x, item)
        if x <= item:
            res += 1
            days2.remove(item)
            break
        elif x > item:
            break
print(res)
