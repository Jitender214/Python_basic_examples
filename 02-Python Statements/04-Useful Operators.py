word = 'abcde'
index_count = 0
for letter in word:
    print('index count {} and lette is {}'.format(index_count,letter))
    index_count = index_count+1
    #using this we can find how many times loop got triggered

#using enumarate function
word = 'abcde'
for letter in enumerate(word):#enumarate print the index count in the form of tuples
    print(letter)

mylist = [1,2,3]
mylist1 = ['a','b','c']
for item in zip(mylist,mylist1): #zip together these 2 lists
    print(item)
print(list(zip(mylist,mylist1)))

print('x' in ['x','y','z'])
print('x' in [1,2,3])

d = {'mykey':2,'mykey2':4}
print(2 in d.keys())
print(2 in d.values())

mylist = [10,20,30,40]
print(min(mylist))
print(max(mylist))

from random import shuffle
shuffle_mylist = [1,2,3,4,5,6,7,8,9]
shuffle(shuffle_mylist)#this will not return anything
print(shuffle_mylist)

from random import  randint
print(randint(0,30)) #randian will give the random integer
print(randint(0,30))
num = input('input some number here: ')
print(num)
name = input('enter your name: ')
print('entered name is : '+ name)
