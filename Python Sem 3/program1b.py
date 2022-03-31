num=int(input("Number: "))
for i in range(2,num+1):
    flag=True;
    for j in range(2,i):
        if i%j==0:
            flag=False;
    if flag==True:
        print(i," is prime")
