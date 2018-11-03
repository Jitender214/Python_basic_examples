def myfunc(a,b,c,d,e):
    return sum((a,b,c,d,e))*0.05
#if we need run the above function then myfunc(2,3,5,6,6)
#we need to give the args with specific number

#*args allowses to to set the oribitory number of args in function

def myfunc1(*args):
    return sum(args)*0.05
#here we can give any number of paramaeters as args

def myfunc2(*args):
    return 'jithu' in args

def myfunc3(*args):
    print(args)
    for words in args:
        if words == 'hello':
            print(words)
        else:
            print('word is not therr in args')
#if we print *args it turn back tuples ('hello','bye') - no need to define before


#if we print **kwargs then it give dictionary {'k1':v1,'k2':v2}
def myfunction(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print('My selected fruit is {}'.format(kwargs['fruit']))
    else:
        print('i didnot find any fruit here')

def myfunc(*args,**kwargs):
    print(args)
    print(kwargs)
    print('i would like to have {}{}'.format(args[0],kwargs['food']))
    print(f"i like to have {args[0]}{kwargs['food']}")
#ouput of the program
#myfunc(10,20,fruit='apple',food='eggs')
#(10, 20)
#{'fruit': 'apple', 'food': 'eggs'}
#i would like to have 10eggs
#i like to have 10eggs
