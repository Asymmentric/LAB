import re
s="something abs@gfh.com"
s=s.split()
for i in s:
  if re.match('[a-zA-Z0-9_.]+@[a-zA-Z]+.[a-z]',i):
    print(i);
  
  
#pgm 2
pwd=input()
obj=re.match('^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*#$@_)[a-zA-Z0-9_@#$]{6,16}',pwd)
if obj:
  print("OK")
else:
  print("NO")
