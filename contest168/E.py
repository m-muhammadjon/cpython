s=input()
while 'C' in s:s=s.replace('C','A')
print('Yes')if s.count('A')==s.count('B')else print('No')