#using map we can pass function as an argument and the iterables(list,tuples) as arguments
#map(function,*iterables)
def myfunc(string):
    if len(string)%2==0:
        return 'Even word'
    else:
        return string[0]

my_string = ['Jithu','Chinna','Jit']
print(map(myfunc,my_string)) #this will give the location of object
print(list(map(myfunc,my_string)))#this will print the result in list

for result in map(myfunc,my_string):
    print(result)
############################################

def square(num):
    return num**2

print(list(map(square,[1,3,4,6])))
#############################################

def check_even(num):
    return num%2 ==0

mynum = [2,5,6,8]
print(list(map(check_even,mynum)))
for my_list in map(check_even,mynum):
    print(my_list)
#map appiled check_even function to eveny element in the mynum list
###########################################
def myfunc(nums):
    return nums%2 ==0

mynums = [1,2,3,4,5,6]
print(filter(myfunc,mynums))##this will give the location of object
print(list(filter(myfunc,mynums)))#this will print the list
for my_list in filter(myfunc,mynums):
    print(my_list)
#filter is going to filter the elements of mynums based on myfunc funtion condition
#############################################

#lambda expression know as an anonymous function
#because its some functionality only use at one time bcoz of that reason we dont use def keyword
square = lambda num : num **2 #this is lambda expression now
#return keywords not required bcoz its assume its going to return something otherside to the colon
print(square(5))


#we can use lambda expression in map and filters also
def myfunc(nums):
    return nums%2 ==0

mynums = [1,2,3,4,5,6]
print(list(filter(myfunc,mynums)))

#above function program converting to lambda expression
print(list(filter(lambda num:num%2==0,mynums)))
##########################################

def check_even(num):
    return num%2 ==0
mynum = [2,5,6,8]
print(list(map(check_even,mynum)))
#above function program converting to lambda expression
print(list(map(lambda num: num%2==0,mynum)))