import os 
path=os.walk("C:\\Users\\arunm\\Desktop\\VVCE\\Sem 3\\Python Lab\\Danish")
ttlFiles=0
ttlSub=0
for root,subd,files in path:
    print("Root:",root)
    print("Folder:",subd)
    print("Files:",files)
    ttlFiles+=len(files)
    ttlSub+=len(subd)
    
print('Total Subd:',ttlSub)
print('Total files:',ttlFiles)
