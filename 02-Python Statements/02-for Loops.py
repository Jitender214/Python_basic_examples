# we use for loop to iterate the elements from the object

#syntax:
#my_iterate = [1,2,3]
#for itr_name in my_iterate:
#print(itr_name)

mylist = [2,4,5,7,9,10]
for num_list in mylist:
    print(num_list)

for num in mylist:
    if num % 2 == 0:
        print(f'number is even: {num}')
    else:
        print(f'number is odd: {num}')

mylist_sum =0
for num_list in mylist:
    mylist_sum = mylist_sum+num_list
print(mylist_sum)

mystr = 'Hello world'
for letters in mystr:
    print(letters)

my_list = [(1,2),(3,4),(5,6),(7,8)]
for items in my_list:
    print(items)

my_list1 = [(1,2,3),(4,5,6),(7,8,9)]
for a,b,c in my_list1: # iterate all but we print only b,c values
    print(b,c)

my_dict = {'k1':'value1','k2':'value2'}
for dict_items in my_dict: #it will iterate only keys
    print(dict_items)

for dict_items in my_dict.items(): # dict.items() will iterate keys & values
    print(dict_items)

for key,value in my_dict.items():
    print(value)