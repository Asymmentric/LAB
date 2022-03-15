file=open("F:\\file.txt",'r')
newFile=open("F:\\file2.txt","w")
newStr=file.read()
lineCount=1;
for i in newStr:
  if lineCount%2!=0:
    newFile.write(letter)
  if letter=="\n":
    lineCount+=1
    
print("Odd line copied")
newFile.close()
file.close()
