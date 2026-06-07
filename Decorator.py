# @Property = Decorator used to define a method as a property (it can be accessed like an attribute)
#             Benefit: Add additional logic when read, write or delete attributes
#             Gives you getter , setter and deleter method


class Rectangle:
    def __init__(self, width , height):
        self._width = width
        self._height = height
     
    #getter  = to read
    @property
    def width(self):
        return f"{self._width: .1f}cm"    
    
    @property
    def height(self):
        return f"{self._height: .1f}cm"
    
    @width.setter                 #it is add logic
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else: 
            print("Width must be greater than zero")
            
            
    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else: 
            print("height must be greater than zero")
            
    
    
    @width.deleter
    def width(self):
        del self._width
        print("width has been deleted")
        
    @height.deleter
    def height(self):
        del self._height
        print("Height has been deleted")             

    
rectangle = Rectangle(3,4)

#rectangle.height =7

#print(rectangle.width)
#print(rectangle.height)

#del rectangle.width
#del rectangle.height




#Decorator = A Function that extends the behavior of another function
#            w/o modifying the base function 
#            Pass the base function as an argument to the decorator

#            @add_sprinkles
#            get_ice_cream("vanilla")

def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("*you add sprinkles 🎊")
        func(*args, **kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("*You add fudge 🍫")
        func(*args, **kwargs)
    return wrapper

@add_sprinkles
@add_fudge

def get_ice_cream(flavour):
    print("Here is your {flavour} ice cream🧁")
    
get_ice_cream("Vanilla")







