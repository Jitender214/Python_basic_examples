def square(n):
    for i in range(n):
        yield i**2

for numbers in square(10):
    print(numbers)

import random
random.randint(1,10)

def random_num(low,high,n):
    for num in range(n):
        yield random.randint(low,high)

for num in random_num(1,10,12):
    print(num)

s = 'hello'
s = iter(s)
print(next(s))
print(next(s))

#generator comprehension just like list comprehension
#but generator comprehension not stored in memory

my_list = [1,2,3,4,5]
gencomp = (list for list in my_list if list>3)

for i in gencomp:
    print(i)