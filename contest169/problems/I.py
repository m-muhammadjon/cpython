def rangee(s):
    f, l = s.split('-')
    strs = [str(x) for x in range(int(f), int(l) + 1)]
    return ' '.join(strs)


s = input().split(',')
out = ''
for i in s:
    if '-' in i:
        out += ' ' + rangee(i)
    else:
        out += ' ' + i

print(out.strip())