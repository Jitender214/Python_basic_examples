#scopes are in python LEGB rule format
#L: Local
#E: Enclosing function call
#G: Global
#B: Built in python

lambda num : num %2 ==0 # here num is in local scope

name = "This is Global scope name"
def greet():
    #enclosing
    name = "Jithu in functional scope"
    def hello():
        #local scope
        #name = 'local scope'
        print('Hello ' + name)
    hello()

greet()

#first name will look into local name space, mens with in a function(def ,lambda)
##not find then goes to next level
        #def hello():
         #   print('Hello ' + name)
# after goes to greet() enclosing function
#if you comment name in eclosing level then it search in global level scope

x =50
def myfunc():
    global x
    print(f'x value is {x}')
    x = 100
    print(f'after modify x value is {x}')

myfunc()

