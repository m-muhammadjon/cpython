s=str(bin(int(input())))[2:];c=0;a=0
for i in range(len(s)):
    if s[i] == '1':
        c+=1
    else:
        a=max(a,c);c=0
a=max(a,c);print(a)