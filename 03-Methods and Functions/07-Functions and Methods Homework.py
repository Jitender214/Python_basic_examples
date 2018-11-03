#check whether the number is in given range b/w low and high
def num_check(num,low,high):
    return num in range(low,high)
#num_check1(3,1,10) --> True
#num_check1(13,1,10) --> False

def num_check1(num,low,high):
    if num in range(low,high):
        print(f'num is in given range {num}')
    else:
        print(f'num is out of range {num}')
#num_check1(3,1,10) --> num is in given range 3
#num_check1(13,1,10) --> num is out of range 13

#
string = 'Hello Welcome To Python Program'
def up_low(string):
    d = {"upper":0,"lower":0}
    for letters in string:
        if letters.isupper():
            d["upper"]+=1
        elif letters.islower():
            d["lower"] +=1
        else:
            pass
    print(f'no of upper letters {d["upper"]}')
    print(f'no of lower letters {d["lower"]}')


#write a function that takes the list and returns a new list with unique elements
list1 = [1,1,1,2,2,3,3,4,4,5,5,5,2]
def unique_list(list1):
    myset = set(list1)
    print(myset)
    my_unique_list = list(myset)
    print(my_unique_list)

def unique_list1(list1):
    x=[]
    for num in list1:
        if num not in x:
            x.append(num)
    return x

#write a function to multiply all the numbers in a list
list = [1,2,3,-4]
def multiply(list):
    value = 1
    for nums in list:
        value = value*nums
    return value

def multiply1(list):
    total = list[0]
    for nums in list:
        total *=nums
    return total

#check whether a passed string is string is palindrome or not
s = 'helleh'
def palindrome(s):
    if s[0::] == s[::-1]:
        return True
    else:
        return False


