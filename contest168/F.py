s=list(input())
while 1:
    if 'A' in s and 'B' in s:
        s.remove('A');s.remove('B')
    elif 'C' in s and 'B' in s:
        s.remove('C');s.remove('B')
    else:
        break
print('Yes') if len(s)==0 else print('No')