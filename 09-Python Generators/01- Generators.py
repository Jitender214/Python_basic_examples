#Generators functions allow us to write a function that can send back a value and then later resume to pick up
#where if left off.

#allows us to generate a sequence of values over time

#generators functions will automatically suspend and resume their execution and state around the past point of value generation

def create_cube(n):
    result = []
    for i in range(n):
        result.append(i**3)
    return result
#we are keeping the entire result in memory

for number in create_cube(10):
    print(number)


def create_cube_yield(n):
    for i in range(n):
        yield i**3

for numbers in create_cube_yield(10):
    print(numbers)
#with yield also we are getting same result
#with this yield result will not store in memory - memory efficient
#exmaple with create_cube(10000) then result store in memory


def gen_fibon(n):
    a =1
    b=1
    output = []
    for i in range(n):
        output.append(a)
        a,b = b,a+b
    return output

for nums in gen_fibon(10):
    print(nums)
#output store in memory


#same result with yield but its memory efficient because we are yielding
def gen_fibon_yield(n):
    a =1
    b=1
    for i in range(n):
        yield a
        a,b = b,a+b

for num in gen_fibon_yield(10):
    print(num)

##iter() function
#basically allows us to iterate the normal object

s = 'hello'
for letters in s:
    print(letters)

#next(s)# this gives the error - 'str' object is not an iterator
#now we are turning s in to iterator

s_iter = iter(s)
print(next(s_iter))