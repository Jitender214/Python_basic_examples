print('Hello')
print("Hello")

print('Hello \n world') #after space it will print in next line
print('Hello \nworld')

print('Hello \tworld') #after tab it will print

print(len('python programming'))

mystring = "Hello my name is jitender"
print(mystring)

print(mystring[4],mystring[6]) #index starts from 0
print(mystring[-3],mystring[-7]) #Reverse indexing starts from -1

mystr = 'abcdefghijk'
print('my str is: ' + mystr)
print('after 2 index : ' + mystr[2:])
print('after 5 index : ' + mystr[5:])
print('before 8 index : ' + mystr[:8])
print('before 1 index : ' + mystr[:4])
print('print between the index letter : ' + mystr[4:8])
print('print between the index letter : ' + mystr[1:4])

print('printing with step size 2 : ' + mystr[::2])
print('printing with step size 4 : ' + mystr[::4])
print('starting from index 2 & stopping at index 8 with step size 2 : ' + mystr[2:8:2])
print('starting from index 2 & stopping at index 8 with step size 2 : ' + mystr[2:10:3])

print('reversing a string : ' + mystr[::-1])
