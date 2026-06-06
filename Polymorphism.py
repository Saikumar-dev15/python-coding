#Polymorphism = Greek word that means to "have many forms or faces"
#               poly = Many
#               Morphe = Form

#               Two ways to Achieve Polymorphism
#               1. Inheritance = An object could be treated of the same type as a parent class
#               2. "Duck typing" = Object must have necessary attributes/methods.


from abc import ABC, abstractmethod

class Shape:
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
        
    def area(self):
            return 3.14 *self.radius ** 2

class Square(Shape):
    def __init__(self,side):
        self.side = side
       
    def area(self):
        return self.side ** 2 
        

class Triangle(Shape):
    def __init__(self,base, height):
        self.base = base
        self.height = height
        
    def area(self):
        return self.base * self.height * 0.5
    
    
class Pizza(Circle):
    def __init__(self,Topping, radius):
        super().__init__(radius)
        self.topping = Topping
    

shapes = [Circle(4), Square(5), Triangle(6,7), Pizza("perperoni", 15)]

#for shape in shapes:
#    print(f"{shape.area()}cm^2")




#"Duck Typing" = Another way to achieve polymorphism besides Inheritance
#                Object must have the minimum neccesary attributes/methods
#                "If it looks like a duck and quacks like a duck, it must be a duck"

class Animal:
    alive = True
    
class Dog(Animal):
    def speak(self):
        print("Barks!..")
        
class Cat(Animal):
    def speak(self):
        print("Meow!..")
        
class Car:
    
    alive = False
    def speak(self):
        print("Honk!....")      
 
animals   = [Dog(), Cat(), Car()]

def new_func(animal):
    print(animal.alive)

for animal in animals:
    animal.speak() 
    new_func(animal)  
       
        