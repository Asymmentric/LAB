import os
path=os.walk("G:\\Test")
ttlFiles=0
ttlSub=0
for root,subdir,files in path:
  print("Root:",root)
  print("subdir:",subdir)
  print("Files:",files)
  ttlFiles=len(files)
  ttlSub=len(subdir)
 
print("Files:"ttlFiles)
print("Subdir:"ttlSub)
