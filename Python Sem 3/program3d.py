a={
    'alice':{
        'apple':5,
        'prawn':12
    },
    'bob':{
        'ham':3,
        'apple':1
    },
    'carol':{
        'cup':3,
        'pies':2
    }
}
count=0;
for i in a.values():
    if 'apple' in i:
        count+=i['apple']

print(count)        
