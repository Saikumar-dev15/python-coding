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

def add(x,y):
    z=x+y
    return z

def subtract(x,y):
    z=x-y
    return z

def multiply(x,y):
    z=x*y
    return z

def divide(x,y):
    z=x/y
    return z

print(add(1,2))
print(subtract(4,2))
print(multiply(1,3))
print(divide(4,2))
