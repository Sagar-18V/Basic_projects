import os
dir="MC BC"
pare="C:\Users\sagar\Downloads\beginner-projects-master\mine\CREATING.py"

path=ps.path.join(pare,dir)

os.mkdir(path)
print("'%s' created"%dir)

mode=0o666
os.mkdir(path,mode)
print("'%s' created"%dir)