import sys

chop = ['the', 'of', 'a']
lines = sys.stdin.readlines()
s = ''
for i in lines:
    print(i.strip())
    s = s + ' ' + i.strip()
s = s.replace('.', '')
s = s.replace(',', '')
s = s.lower().split()
for item in chop:
    while item in s:
        s.remove(item)
data = dict()
for word in set(s):
    data[word] = s.count(word)
print(sorted(data.items(), key=lambda item: item[1])[-1][0].upper().strip())
