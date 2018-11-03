#Decorators allows you to decorate a function

#Python has decorators that allow you to tack on extra functionality to an already existing functionality

#they use the @ operator and are then placed on top of the original function.

def hello():
    print("this is hello() function ")

    def greet():
        return "\t this is greet() function inside hello"
    def welcome():
        return "\t this is welcome function inside hello"

    print(greet())
    print(welcome())
    print("End of hello() function")
#if we call greet and welcome() then will get error because those are inside hello() - scope is limited to hello function
#greet() then - greet is not defined


def hello1(name='Jithu'):
    print("this is hello() function ")

    def greet():
        return "\t this is greet() function inside hello"
    def welcome():
        return "\t this is welcome function inside hello"
    print("i ma going to return a function()")
    if name == 'Jithu':
        return greet()
    else:
        return welcome()
#this is an idea able to return a function with in another function
my_new_func = hello1('Jithu') # this will return greet function
my_another_func = hello1('Chinna') #this  will return welcome function

#passing function as an argument to another function
def hi():
    return "Hi hello...."

def bye(some_def_func):
    print("Bye function calling Hi function")
    print(some_def_func())

bye(hi)


def new_decorator(original_func):

    def wrap_func():
        print("some extra code here, before the original function")

        original_func()

        print("some code after the original function")

    return wrap_func()

def original_func():
    print("i am the original function")

decorated_func = new_decorator(original_func)
decorated_func

@new_decorator
def original_func():
    print("i am the original function with @ operator")

original_func



