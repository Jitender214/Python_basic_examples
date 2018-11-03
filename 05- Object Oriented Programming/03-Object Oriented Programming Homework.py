class Line():

    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return ((x2-x1)**2 + (y2-y1)**2)**0.5

    def slope(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return (y2-y1) / (x2-x1)


c1 = (3,2)
c2 = (8,10)

myline = Line(c1,c2)
print(myline.distance())
print(myline.slope())

class Cylinder():

    pi = 3.14
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        h = self.height
        r = self.radius
        return self.pi*r*r*h
        #return self.height * 3.14 * (self.radius)**2

    def surface(self):
        h = self.height
        r = self.radius
        return 2*self.pi*r*r + 2*self.pi*r*h
        #top = 3.14 * (self.radius**2)
        #return (2*top) + (2*3.14*self.radius*self.height)

mycylinder = Cylinder(2,3);
print(mycylinder.volume())
print(mycylinder.surface())

class Account():
     def __init__(self,name,balance):
         self.name = name
         self.balance = balance
         #print(f" name is {self.name} balance is {self.balance}")

     def __str__(self):
         return f" account owner name is {self.name} \n account balance is {self.balance}"

     def deposit(self,amount):
         self.balance = self.balance + amount
         print(f" Deposit accepted total balance is {self.balance}")

     def withdraw(self,amount):
         if self.balance >= amount:
             self.balance = self.balance - amount
             print(f" Withdraw accepted remaining balance is {self.balance}")
         else:
             print("Funds unavilable")

acc = Account('Jithu',100)
print(acc)
print(acc.name)
print(acc.balance)

acc.deposit(50)
acc.withdraw(30)
acc.withdraw(130)
