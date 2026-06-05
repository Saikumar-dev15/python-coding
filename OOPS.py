#object = A "bundle" of related attributed (variables) and methods (functions)
#         ex= phone, cup, book
#         you need a "class" to create many objects

#class = (blueprint) used to design the structure and layout of an object


class Car:
    def __init__(self, model,year,color,for_sale):                             #constructor method
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print("You drive the car {self.model}")

    def stop(self):
        print("You stop the car {self.model}")
       
car1 = Car("Mustang", 2026, "Orange", False)
car2 = Car("BMW", 2025, "Orange", True)

#print(car2.model)
#print(car2.year)
#print(car2.color)
#print(car2.for_sale)
        
car1.drive() 
car1.stop()
 