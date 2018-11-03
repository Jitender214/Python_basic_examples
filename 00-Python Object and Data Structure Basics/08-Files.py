myfile = open('C:/Users/jbandari/Desktop/Python/Practice/test.txt')
print(myfile.read()) # this will read everything in the text file
print(myfile.read()) # again if try to read then will get empty string -
# there is a cursor at begining of the file after reading it come to end of the file
# if order to read it again we need to reset the cursor back to zero again
myfile.seek(0)
print(myfile.read())

myfile.seek(0)

content = myfile.read()
print(content)

myfile.seek(0)
print(myfile.readline())
myfile.close()

with open('C:/Users/jbandari/Desktop/Python/Practice/test.txt') as my_new_file:
    contents = my_new_file.read()
    print(contents) #no worry to close bcoz file used in this block of code

with open('C:/Users/jbandari/Desktop/Python/Practice/myfile.txt',mode='r') as file:
    print(file.read())
    #file.write("FOURTH LINE") not writable because mode is only readable

with open('C:/Users/jbandari/Desktop/Python/Practice/myfile.txt',mode='a') as file:
    file.write('FOURTH LINE') # with mode a , content will append to the file

with open('C:/Users/jbandari/Desktop/Python/Practice/myfile.txt',mode='r') as file:
    print(file.read())

with open('C:/Users/jbandari/Desktop/Python/Practice/jithu.txt',mode='w') as file:
    file.write("JITHUUUUUUUUUUUUUUUUUUUU") # with W mode it will overwrite the file if file doesn't exist then it will create
    print('file creared')
