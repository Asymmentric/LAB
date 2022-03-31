import random
options=['rock','paper','scissor']
while True:
    print(options)
    user=input('Choose:');
    sys=random.choice(options)
    print("user:",user,"System:",sys)
    if(user==sys):
        print('Draw')
    elif((user=='rock' and sys=='scissor')):
        print('User wins')
    elif(user=='paper' and sys=='rock'):
        print('User Wins')
    elif(user=='scissor' and sys=='paper'):
        print('User Wins')
    elif(user!=('rock' or 'paper' or 'scissor')):
        print("invaliD input")
    else:
        print("System wins")
