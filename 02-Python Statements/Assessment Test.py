st = 'print only the words that starts with s in this sentense'
for words in st.split():
    print(words)
for words in st.split():
    if words[0] == 's':
        print('words starting with s : ' + words)
for words in st.split():
    if words.startswith('s'):
        print('words starting with s : '+ words)
#use range print all the even numbers from 0 to 10
mylist = range(0,11)
for num in mylist:
    if num%2==0:
        print(num)

for num in range(0,11,2):
    print(num)

#use list comprehensation to create list of all numbers between 1 to 50 that are divisible by 3
mylist = [num for num in range(1,50) if num%3==0]
print(mylist)

#go through the string below and if the length of a word is even print even
st = 'print only the words that starts with s in this sentense'
for words in st.split():
    if len(words)%2==0:
        print(words + ' is even')
#range letters from 0 to 50 and if div by 3 the print fizz, if dvi by 5 then print buzz if both print fizzbuzz
for num in range(0,50):
    if num %3==0:
        print('Fizz')
    elif num%5==0:
        print('Buzz')
    elif num%3==0 and num%5==0:
        print('FizzBuzz')
    else:
        print(num)

#use list comprehensation to create a list of the first letters of every word in the string below
st = 'Hi welcome to python programming'
print([letters[0] for letters in st.split()])