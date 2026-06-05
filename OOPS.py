#object = A "bundle" of related attributed (variables) and methods (functions)
#         ex= phone, cup, book
#         you need a "class" to create many objects

#class = (blueprint) used to design the structure and layout of an object

#class variables = Shared among all instances of a class
#                  Defined outside the constructor
#                  Allow you to Share data among all objects create from the class

class Car:
    
    wheels = 4                                                                  #Class variable
    
    def __init__(self, model,year,color,for_sale):                             #constructor method
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"You drive the car {self.color}{self.model}")

    def stop(self):
        print(f"You stop the {self.color}{self.model}")
        
    def describe(self):
        print(f"{self.year} {self.color} {self.model}")





       
class Student:
    
    class_year = 2029
    num_students = 0
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students +=1
        
student1 =Student("Sai kumar", 19)
student2 =Student("RajP", 19)
student3 =Student("Shiva", 19)


#print(student2.name)
#print(student2.age)  
#print(Student.class_year)
#print(f"My graduating class of {Student.class_year} has {Student.num_students} students")      




