import re
s='this is abc@gmail.com'
words=s.split()
for word in words:
    if re.match('[a-zA-Z0-9_.]+@+[a-zA-Z]+.[a-zA-Z]',word):
        print(word)
