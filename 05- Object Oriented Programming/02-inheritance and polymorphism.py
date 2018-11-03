class Animal():
    def __init__(self):
        print("Animal Base class is created")

    def hungry(self):
        print("feed the animal")

    def who_am_i(self):
        print("i am an animal")

my_animal = Animal()#init method automatically executed when we create object for the class
my_animal.hungry()
my_animal.who_am_i()

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog Dirived class is created ")
    def who_am_i(self):
        print("i am a Dog")

my_dog = Dog()
#after created object for dirived class then all the base class method available for dirived class
my_dog.who_am_i() # this will override the method of base class
my_animal.who_am_i()
my_dog.hungry()

#######################################################################

class Dog():
    def __init__(self,name):
        self.name = name
    def bark(self):
        return self.name + " says Bow"

class Cat():
    def __init__(self,name):
        self.name = name
    def bark(self):
        return self.name + " says Meow"

niko = Dog("Niko")
felix = Cat("Felix")
print(niko.bark())
print(felix.bark())
#each of class has bark method and when we call bark method of each object that returned the result unique to the object

def pet_speak(pet):
    print(pet.bark())

pet_speak(niko)
pet_speak(felix)


class Animal():
    def __init__(self,name):
        self.name = name

    def speak(self):
        raise NotImplementedError ("subclass must have to this abstract method")

#my_animal = Animal('puppy')
#my_animal.speak()
#in the base class it self speak method is doesnot doing anything
#its expecting to inherit the animal and override the speak method

class Dog(Animal):
    def speak(self):
        return self.name + " says Bow"

class Cat(Animal):
    def speak(self):
        return self.name + " says Meow"


fido = Dog("Fido")
isis = Cat("Isis")
print(fido.speak())
print(isis.speak())


#Real time example is open a file
#method name called open in base class for opening the file
#diff types of files word,pdf,excel...


################################################################
mylist = [1,2,3]
print(len(mylist))

#if we want to check the length of created object of class
class Sample():
    pass

mysample = Sample()
#len(mysample) #it will give error as object of type 'Sample' has no len()

class Book():

    def __init__(self,name,author,pages):
        self.name= name
        self.author= author
        self.pages= pages

    def __str__(self):#we can use this special method related to string call
        return f"{self.name} by {self.author}"
    def __len__(self):
        return self.pages

mybook = Book('Python','Jose',200)
print(mybook)#it will print index location of book obj
#print function ask the book object do you have a string representation of your self if yes then it Puthon by Jose as output
#if i cast mybook into string
print(str(mybook)) #it will print the string version
print(len(mybook))



