str = 'Welcome'

str1 = str + ' to python programming' # concatenation
print(str1)

print('2'+'3')

mystring = 'My name is Jitender'
print('in upper case: '+ mystring.upper())
print('in lower case: '+ mystring.lower())
list = [mystring.split()] # its splitting by space
print(list)
print (mystring.split())
list = [mystring.split('e')]
print(list)

print('this is string {}'.format('in PYTHON')) #using format obj into string using .format method
print('{} {} {} {} '.format('my','name','is','jithu'))
print('with index: '+'{3} {2} {0} {1} '.format('my','name','is','jithu'))
print('with assignning keywords: '+ '{m} {n} {i} {j} '.format(m='my',n='name',i='is',j='jithu'))

name = 'jithu'
age = '28'
print('Hello , my name is {name} and age is {age}')
print(f'Hello , my name is {name} and age is {age}') #using formating string literal

print('i am going to inject %s here' %'something') #using %s to inject string in print stmt

result = 1000/77
print(result)
print('after formatting result is {r:1.3f}'.format(r=result))#{value:width:precision f}
