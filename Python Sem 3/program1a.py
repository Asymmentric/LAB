num=input("number:")
while(len(num)>1):
    sum=0;
    for i in num:
        sum+=int(i)
    num=str(sum)
if(sum==1):
    print('magic number')
else:
    print("Not a magic number")
