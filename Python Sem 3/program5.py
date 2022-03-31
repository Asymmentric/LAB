word=input("word:")
guess=['_']*len(word);

turns=len(word)
while turns>1:
    print(guess);
    print(turns,'chance left')
    g=input('Your guess:');
    if g in word:
        for i in range(len(word)):
            if g==word[i]:
                guess[i]=g;
    else:
        turns-=1;
    if list(word)==guess:
        print("Found")
        print(guess)
        break;
