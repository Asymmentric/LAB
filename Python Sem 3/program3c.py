b=input("Input string:")
c=""
b=b.split()
for i in b:
    if i=='the':
        c+=""
    else:
        c+=" "+i
print(c)
