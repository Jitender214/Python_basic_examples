# we have three keywords to handle the exception
#try - this is the block of code to be attempted(may lead to an error)
#except - block of code will execute in case there is an error in try block
#finally - a finally block of code to be executed,regardless of an error

try:
    #code here - may have an error
    result = 10+10 #this will give 20
    #result = 10+'10' # and this give print not adding correctly with interrupting the remaining lines of code
except:
    print("not adding correctly")
else:
    print("add went well")
    print(result)

try:
    f = open('testfile',mode='w')
    f.write("write a something into file")
except TypeError:
    print("there was a type error")
except OSError:
    print("you have and OS error")
finally:
    print("always i will execute")

try:
    f = open('testfile',mode='r')
    f.write("write a something into file")
except TypeError:
    print("there was a type error")
except:
    print("text file mode ir read, so can't write into it")
finally:
    print("always i will execute")


def ask_for_int():
    try:
        result = int(input("Please enter a number: "))
    except:
        print("This is not a number")
    finally:
        print("End of try and except, finally")

def test():
    try:
        result = 10/10
    finally:
        print("added successfully")
    return result
