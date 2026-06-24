# function = a BLOCK OF REUSABLE CODE 
#            PLACE () after the function name to invike it

#def happy_birthday(name , age):
#    print(f"Happy birthday to {name}! ")
#    print(f"how old are you {name} and your {age} right now!!...  ")
#    print(f"have a good day  {name} ")
#    print()        

#happy_birthday("Sai" , 19 )
#happy_birthday("Joe", 20)


#def display_invoice(username, amount, due_date):
#    print(f"Hello {username}")
#    print(f"your bill of ${amount: .2f} is due: {due_date}")
    
#display_invoice("Sai" , 20.43, "02/26" )

 
# Return = statement used to end a function
#          and send a result back to the caller

#def add(x,y):
#    z=x+y
#    return z

#def subtract(x,y):
#    z=x-y
#    return z

#def multiply(x,y):
#    z=x*y
#    return z

#def divide(x,y):
#    z=x/y
#    return z

#print(add(1,2))
#print(subtract(4,2))
#print(multiply(1,3))
#print(divide(4,2))


#def create_name(first, last):
#    first = first.capitalize()
#    last = last.capitalize()
#    return first + " " + last

#full_name = create_name("spongebob","squarepants")

#print(full_name)



#Default arguments = A default value for certain parameters
#                    default is used when that arguments is omitted make your functions more flexible, reduces # of arguments
#                    1.position 2.Default 3. keyword 4. arbitary


#POSITION
#def net_price(list_price, discount, tax):
#    return list_price * (1- discount)* (1 + tax)
#print(net_price(500, 0, 0.05))


#DEFAULT
#import time

#def count(end, start=0):                            #non-default argument follows default argument..
#    for x in range(start, end+1):                 # it will increase the count numbers
#        print(x)
#        time.sleep(1)
#    print("DONE..!!")

#count(30,15)



#KEYWORD
#Keyword arguments = an arguments preceded by an identifier
#                    helps with readability 
#                    order of arguments doesn't matter


#def hello(greeting, title, first, last):
#    print(f"{greeting} {title}{first} {last}")
    
#hello("hello","Mr.",last="Squarepants",first="Spongebob",)



#def get_phone(country, area, first, last):
#    return f"{country}-{area}-{first}-{last}"
#phone_num = get_phone(country=1, area=123, first=456, last=7890)
#print(phone_num)



#ARBITRARY ARGUMENTS
# *args = allows you to pass multiple non-key  arguments
# **kwargs = allow you to pass multiple keyword- arguments

#def add(*args):
#    total =0 
#    for arg in args:
#        total += arg
#    return total
#print(add(1,2,4,5))

#def display_name(*args):
#    for arg in args:
#        print(arg, end=" ")

#display_name("Mr.", "Sai", "Kumar", "choudary")


# **kwargs
#def print_address(**kwargs):
#        for value in kwargs.values():
#            print(value)
            
#print_address(street="123 fake st.",
#              city="Hydrabad",
#              state="Telangana",
#              pincode="508218")


#exercise on both *args and **kwargs
#def shipping_label(*args, **kwargs):
#    for arg in args:
#       print(arg, end=" ")
#    for value in kwargs.values():
#       print(value, end=" ")
    
#shipping_label("Mr.", "Sai", "Kumar", "choudary",
#               street="123 fake st.",
#               city="Hydrabad",
#               state="Telangana",
#               pincode="508218")

    
    
    
#Tables
def Table(num):
   for i in range (1,11):
      print(f"{num} x {i} = {num*i}")
      
Table(27)