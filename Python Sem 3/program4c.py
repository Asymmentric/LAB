d=input("String:")
letter={}
for i in d:
    if i in letter.keys():
        letter[i]+=1;
    else:
        letter[i]=1;

print(letter)
