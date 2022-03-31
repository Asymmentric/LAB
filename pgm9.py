file1=open("file1.txt")
file2=open("file2.txt",'w')
str1=file1.read()
str2=""
line=1;
for letter in str1:
    if letter=='\n':
        line+=1;
    if line%2!=0:
        str2+=letter
        
file2.write(str2)
file2.close()
file1.close()
