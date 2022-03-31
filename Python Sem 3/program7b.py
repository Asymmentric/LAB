import re
pwd=input('Password:')
obj=re.match('^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[@#$_])[a-zA-Z0-9@#_$]{6,16}$',pwd)
if obj:
    print("ok")
else:
    print("No")
