n=int(input())+1;a=int(input());b=int(input());
while 1:
    if n%a==0 and n%b==0:
        break
    n+=1
print(n)