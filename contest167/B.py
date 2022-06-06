def sum(num):
    s = 0
    while num > 0:
        s += num % 10
        num //= 10
    return s


def count(num):
    return len(str(num))


a = int(input())
b = int(input())
if sum(a) == sum(b):
    if count(a) == count(b):
        print(max(a, b))
    elif count(a) > count(b):
        print(a)
    else:
        print(b)
elif sum(a) > sum(b):
    print(a)
else:
    print(b)
