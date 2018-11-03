#syntax
#class name_of_the_class():
#def __init__(self,param1,param2):
#self.param1=param1
#self.param2=param2
#def some_method(self):
#perform some action
#print(self.param1)

class Dog():
    #class level attribute
    #same for any instance of a class
    #even if dont define it, its available for us
    class_level_attribute = 'class-level'
    def __init__(self,name):
        #Attributes
        #we take in the argument
        #assign it using self.attribute_name
        self.name = name

my_dog = Dog(name='puppy')
print(type(my_dog))
print(my_dog)
print(my_dog.name)
print(my_dog.class_level_attribute)


#Actions/Operations  --> Methods()

class Dog1():
    def __init__(self,name):
        self.name=name

    def hungry(self):
        #self connect to actual object
        print("feed the dog")
    def bark(self,number):
        print("Bow Bow my name is {} and number is {}".format(self.name,number))
        #we are not calling self.number bcoz ots provided by method itself

my_dog = Dog1('Puppy')
my_dog.bark(5)
my_dog.hungry()


class circle():
    #class level attribute
    pi = 3.14
    def __init__(self,radius=1):
        self.radius = radius
        #if we have an attribute it doen't neccesary to define in particuler parameter call
        self.area = self.radius*self.radius*self.pi
        #pi is class level attribute we can call it using self.pi bcoz self refers to particular instance
        #we can call Circle.pi bcoz its class level attribute
        #self.area = self.radius * self.radius * Circle.pi

    def get_circumference(self):
        return self.radius * self.pi *2
        #return self.radius * Circle.pi * 2

my_cicle = circle()
#if we do not pass anything then it will take default value which we provided radius =1
print(my_cicle.radius)
print(my_cicle.get_circumference())

my_cicle = circle(20)
#overridden the default value of  of radius
print(my_cicle.radius)
print(my_cicle.get_circumference())

print(my_cicle.area)

