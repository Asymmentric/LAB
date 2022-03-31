num=input('Num:')
l=[1,0]
if num.isdigit():
    for i in range(int(num)-2):
        l.insert(0,l[0]+l[1])
else:
    print("invalid input")
print(l)
