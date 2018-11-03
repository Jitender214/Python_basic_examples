class UserdefindExp(Exception):
    pass

class NameEception(UserdefindExp):
    pass

def testexp():
    try:
         mystring = 'Jithu'
         enterstr = input("enter name ")
         if mystring == enterstr:
             print('name matches')
         else:
             raise NameEception
    except NameEception:
        print("Please enter correct name")
    finally:
        print("in finally block")

class AgeException(Exception):
    pass

def myexp():
    try:
        age = 12
        if(age<18):
            raise AgeException
        else:
            print("Correct age")
    except AgeException:
        print("Age should be greater than or equal to 18")
    finally:
        print("End of the program")


