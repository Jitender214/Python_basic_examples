my_dic = {'key1':'value1','key2':'value2','key3':'value3'}
print(my_dic)

print(my_dic['key2']) #based on key we can get value

price_lookup = {'apples':80,'oranges':50,'bananas':40}
print(price_lookup['oranges'])

# calling nested object inside the dictionary
dict = {'k1':123,'k2':[1,2,3],'k3':{'insideKey1':30,'insideKey2':40}} #inside dictionary list and dict example
print(dict['k2'])
print(dict['k3'])
print(dict['k3']['insideKey1']) #to call inside dic value using key
print(dict['k2'][2])

dic = {'key1':['a','b','c']} #inside list C value want to make it as Captial C
print(dic['key1'][2].upper())

new_dic = {'k1':100,'k2':200}
print(new_dic)
new_dic['k3'] = 300 #add new key and value to dictionary
print(new_dic)
new_dic['k1'] = 'NEW VALUE' #overriding exxising key value
print(new_dic)

new_dic1 = {'k1': 100, 'k2': 200, 'k3': 300}
print(new_dic1.keys()) #to see all the keys of a dictionary
print(new_dic1.values()) # to see all the values of dict
print(new_dic1.items()) # to see actual paring of dict

new = {1:2,3:5}
print(new)
print(new[1])
