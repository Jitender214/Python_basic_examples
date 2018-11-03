mystring = 'Hello'
mylist = []

for letter in mystring:
    mylist.append(letter)
print(mylist)

#using list comprehension
mylist = [letter for letter in mystring]
print(mylist)

mylist1 = [x for x in 'abcde']
print(mylist1)

mylist2 = [num for num in range(1,20)]
print(mylist2)

mylist2 = [num**2 for num in range(1,20)]
print(mylist2)

mylist2 = [num for num in range(1,13) if num % 2==0]
print(mylist2)

mylist3 = []
for x in [1,2,3]:
    for y in [10,20,30]:
        mylist3.append(x*y)
print(mylist3)
