# while loops will continue to execute a block of code while some condition remains true

#syntax
#while some_boolean_condition:
#do something
#else
#some different

x = 0
while x < 4:
    print(f'x value is {x}')
    x = x+1
else:
    print('x is not less than 5')

x = [1,2,3]
for num in x:
    #if we put comment after for loop indentation is expecting something afert the colon
    #will get error if we write pass then we dont get any error, its does nothing at all
    pass
print('end of my script')

name = 'Jithu'
for letters in name:
    if letters == 'i':
        continue #continue goes to the top of the closet enclosing loop
    print(f'letters are: {letters}')

for letters in name:
    if letters == 'i':
        break #breaks out of the current closet enclosing loop
    print(f'{letters}')

