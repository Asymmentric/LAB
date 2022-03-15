import json
import difflib
file=open("F://words.json")
words=json.load()
userword=input("Word:")
if userword in words.keys():
  print(userword,": ",words[userword])
else:
  best=difflib.get_close_matches(userword,words.keys())
  if(len(best)>0):
    best=best[0]
    print("Did you mean ",best,"?y/n")
    yORn=input();
    if yORn=='y':
      print(best,": ",words[best])
    else:
      print("No matches")
  else:
    print("No matches")
