print(0.25+10*10)
print(4*25+0.25)

print(4*(6*5))
print(4*6+5)

print(type(3+1.5+4))
print(3**3)
print(100 ** 0.5)

str = 'hello'
print(str[1])
print(str[::-1])

print(str[4])
print(str[-1])

my_list = [0,0,0]
print(my_list)

tuple = (0,0,0)
mylist = list(tuple)
print(mylist)

list1 = [1,2,[3,4,'hello']]
list1[2][2] = 'goodbye'
print(list1)

list2 = [5,3,1,2,4]
list2.sort()
print(list2)

dict = {'k1':{'k2':'hello'}}
print(dict['k1']['k2'])

dict2 = {'k1':[{'nestkey':['this is deep',['hello']]}]}
print(dict2['k1'][0]['nestkey'][1][0])

l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]
print(l_one[2][0] >= l_two[2]['k1']) #3>=4