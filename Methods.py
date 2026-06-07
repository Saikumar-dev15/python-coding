#Static methods = Amethod that belong to a class rather than any object from that class (instance)
#                 Usually  used for general utility functions

#Instance methods = Best for operation on inheritce of the class(object)
#static methods = best for utility function that do not need accesss to class data

class Employee:
    def __init__(self, name, position):
        self.name = name 
        self.position = position
        
    def get_info(self):
        return f"{self.name} = {self.position}"
    
    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_positions
    
employee1 = Employee("Sai kumar", "Manager")    
employee2 = Employee("Shiva", "Cashier")
employee3 = Employee("Jack", "Cook")


print(Employee.is_valid_position("Manager"))
print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())