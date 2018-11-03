try:
    for i in ['a','b','c']:
        print(i**2)
except TypeError:
    print("Type Error - we can't add characters")
finally:
    print("always it will run")

try:
    x = 5
    y = 0
    z = x/y
except ZeroDivisionError:
    print("ZeroDivision Error - can't divide by zero")
finally:
    print("always execute")

def square_root():
    while True:
        result = 0
        try:
            num = int(input("Enter a number for Square root : "))
            result = num**num
        except:
            print("Please enter a number instead of String")
            continue
        else:
            break
        finally:
            print("always it will execute")
    print(result)
