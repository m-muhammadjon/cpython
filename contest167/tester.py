import subprocess
txt = """the at  on to of is that
The state finals of the Texas Computer Education
Association Computer Programming Contest is today.
Teams from all over the state of Texas are
participating in the event. In last year contest,
each team brought their own computer."""
p = subprocess.run('python I.py', input=txt, text=True, shell=True)
p.stdout