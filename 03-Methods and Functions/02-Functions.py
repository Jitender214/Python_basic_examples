#function syntax
def name_of_function():
    '''
    Docstring explains function
    '''
print('hello')

#parameterized function
def name_of_function(name):
    '''
    Docstring explain function
    '''
    print('hello' + name) #its just printing not returning anything
    #res = name_of_function('Jithu') #here res will be None type

def add_func(num1,num2):
    return num1+num2
#add_func(2,3)

def check(mystring):
    if 'jithu' in mystring.lower():
        return True
    else:
        return False
#we need check the function from console like check('my name is jithu')
#if we give check('My name is Jithu') its return False because of Capital Jithu
#if we give mystring.lower() in then always its true

def check1(mystring):
    return 'jithu' in mystring.lower()

#if word start with vowel add 'ay' to the end
#if word doesnot start with vowel the,put the first letter at the end and add 'ay'

def pig_latin(word):
    first_letter = word[0]
    print(first_letter)
    if first_letter in 'aeiou':
        pig_word = word+'ay'
    else:
        pig_word = word[1:]+first_letter+'ay'
    return pig_word
#pig_latin('hello') - ellohay
#pig_latin('egg') - eggay