my_list = [1,2,3,4,5]
print(my_list)

my_list = ['string',100,13.5]
print(my_list)
print(type(my_list))
print(len(my_list))#length of list

my_list = ['one','two','three','four']
print(my_list[0])
print(my_list[1:]) #slicing using index
print(my_list[-2:])#reverse slicing

another_list = ['five','six']
new_list = my_list+another_list #concetenation of list
print(new_list)

new_list[0] = 'ONE IN CAPS' #modifying the list
print(new_list)
print(new_list.__contains__('six')) #contains checks the element is there in list or not

new_list.append('seven') #append will add new element to list
print(new_list)

new_list.pop() #pop remove the item from end of the list
print(new_list)

popped_item = new_list.pop()
print(popped_item)

new_list.pop(2) #removing the particular element from the list
print(new_list)

letters_list = ['a','e','r','k','b']
print(letters_list.sort()) #it will just sort the list doesn't return anything thats why None in result
print(letters_list)

num_list = [4,1,7,2,8]
num_list.sort()
my_sorted_list = num_list
print(my_sorted_list)

num_list.reverse()
print(num_list)

