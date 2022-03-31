e=input("Input ; separated emails:");
st=0;
nd=e.find(";")
while(nd!=-1):
    print(e[st:nd]);
    st=nd+1 
    nd=e.find(";",st)
