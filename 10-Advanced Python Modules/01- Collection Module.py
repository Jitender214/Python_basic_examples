#Collection module is built-in module that implement specialized container datatypes providing alternatives to pythons
#general purpose built-in containers.

#Counter

from collections import Counter
list = [1,1,1,3,3,3,3,4,4,13,13,13,13,13,6,6]
print(Counter(list))
#output is : Counter({13: 5, 3: 4, 1: 3, 4: 2, 6: 2})
#Counter does count the no of occurences of each of the elements in list

str = "adadddhiiiijjkkk"
print(Counter(str))
#Counter({'d': 4, 'i': 4, 'k': 3, 'a': 2, 'j': 2, 'h': 1})

s = 'How many times does each word show up in this sentense word word how times '

words = Counter(s.split())
print(words)
c = Counter(words)
print(c.most_common(2))#most common word are
print(sum(c.values()))


#Defaultdict
#defaultdict is a dictionary like object which provides all methods provided by dictionary but takes
#first argument (fedault_factory) as default data type for the dictionary

#defaultdict will never raise a KeyError. any error that doesnot exist gets the value returnd by the default factory

from collections import defaultdict

#normal dictionary
d = {'k1':1}
print(d['k1'])
#print(d['k2'])#KeyError: 'k2'

d = defaultdict(object)
print(d['one'])#it will assign what ever the factory default condition - in this case object
for item in d:
    print(item)
#we can also use defaultdict to initialize the values

d1 = defaultdict(lambda: 0)#lamda
d1['one']
d1['two'] = 2
print(d1)


#OrderedDict
#An OrderedDict is a dictionary subclass that remembers the order in which its contents are added


#Normal dictionary
nor_dic = {}
nor_dic['a'] = 1
nor_dic['b'] = 2
nor_dic['c'] = 3
nor_dic['d'] = 4
nor_dic['e'] = 5
print(nor_dic)

for k,v in nor_dic.items():
    print (k,v)
#this doesnot report the order

from collections import OrderedDict
dic = OrderedDict()
dic['a'] = 1
dic['b'] = 2
dic['c'] = 3
dic['d'] = 4
dic['e'] = 5
print(dic)

for k,v in dic.items():
    print (k,v)

normal_d1 = {}
normal_d1['a'] = 1
normal_d1['b'] = 2
normal_d2 = {}
normal_d2['b'] = 2
normal_d2['a'] = 1
print(normal_d1 == normal_d2)# True

order_d1 = OrderedDict()
order_d1['a'] = 1
order_d1['b'] = 2
order_d2 = OrderedDict()
order_d2['b'] = 2
order_d2['a'] = 1
print(order_d1 == order_d2) #False bcoz added in diff order


#Namestuples
from collections import namedtuple
Dog = namedtuple('Dog','age breed name')#two orguments - one is name of the class, pass string various attributes
d = Dog(age=2,breed='Lab',name='Sammy')
print(d)
print(d.age)
print(d[2])










