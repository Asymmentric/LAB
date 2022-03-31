import json
import difflib
file=open('meaning.json')
words=json.load(file)
user_word=input()
if user_word in words.keys():
	print(user_word,":",words[user_word])
else:
	best=difflib.get_close_matches(user_word,words)
	if len(best)>0:
		best=best[0]
		print("did you mean ",best,"?y/n")
		YorN=input()
		if YorN=='y' or YorN=='Y':
			print(best,":",words[best])
		else:
			print("No match found")
	else:
		print("no match found")
		
