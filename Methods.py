#Static methods = Amethod that belong to a class rather than any object from that class (instance)
#                 Usually  used for general utility functions

#Instance methods = Best for operation on inheritce of the class(object)
#static methods = best for utility function that do not need accesss to class data
#class methods =  Best for class-level data or require access to the class itself


class Employee:
    def __init__(self, name, position):
        self.name = name 
        self.position = position
    
    #Instance Method        
    def get_info(self):
        return f"{self.name} = {self.position}"
    
    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_positions
    
employee1 = Employee("Sai kumar", "Manager")    
employee2 = Employee("Shiva", "Cashier")
employee3 = Employee("Jack", "Cook")


#print(Employee.is_valid_position("Manager"))
#print(employee1.get_info())
#print(employee2.get_info())
#print(employee3.get_info())



#class Methods = Allow operations related to the class itself
#                Take (cls) as the first parameter, which represents the class itself

class Student:
     
    count = 0
    total_gpa = 0
     
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa
        
    #Instance Method    
    def get_info(self):
        return f"{self.name} {self.gpa}"
    
    @classmethod
    def get_count(cls):
        return f"Total # of  student: {cls.count}"
    
    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0 
        else: 
            return f"{cls.total_gpa/ cls.count}"
        
    
    
student1 = Student("Sai kumar", 8.9) 
student2 = Student("Anu", 8.4) 
student3 = Student("raja", 9.6) 
   
    
#print(Student.get_count())
#print(Student.get_average_gpa())


#Magic Methods = Dunder methods (double underscore)   __init__, __str__ , __eq__
#                They are automatically called by many of python's  built-in operations
#                They allow developers to define or customize the behavior of objects

class Book:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author =  author
        self.num_pages = num_pages
        
    def __str__(self):
        return f"'{self.title}' by {self.author} "
    
    def __eq__(self, other):                                                     # other means another book      
        return self.title == other.title and  self.author == other.author
        
    def __it__(self, other):
        return self.num_pages > other.num_pages
    
    def __gt__(self, other):
        return self.num_pages <  other.num_pages
    
    def __add__(self, other):
        return self.num_pages + other.num_pages
    
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author
    
    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"Key '{key}' was not found"
        
    
    
        
book1 = Book("The Hobbit", "J.R.R Tolkien", 310)
book2 = Book("Harry potter", "J.K Rowling", 223)
book3 = Book("The Lion", "C.S Lewis", 172)

#print(book1)
#print(book1 == book2)
#print(book2 > book3)
#print(book1 + book2)
#print("Lion" in book3)
print(book1['title'])



    
    