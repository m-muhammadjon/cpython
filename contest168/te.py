import subprocess
p=subprocess.run('python K.py', input="""5 4 
3   2 1
3 5 6 7
1
3
5 6 7""", shell=True, text=True)
print(p.stdout)