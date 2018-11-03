# tuples also same as list but tuples are immutables
my_tuple = (1,2,3,'four',5.23)
print(my_tuple)
print(len(my_tuple))

print(my_tuple[3])
print(my_tuple[-3])

my_tup = ('a','b','h','r','a')
print(my_tup.count('a')) #we can print number of times a occurs in tuple

my_tup = (1,2,3)
my_tup[0] = 'New' #'tuple' object does not support item assignment - we can't assign values again one tuple is created
print(my_tup)
