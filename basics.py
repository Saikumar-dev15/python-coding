#variable = a container for a value (string, integer, float, boolean)

#strings
first_name = "Sai"
food = "Burger"
email = "kurapatilakshmisaikumar@gmail.com"
#print(f"Hello {first_name}")
#print(f"You like {food}")
#print(f"your e mail: {email} ")

#integers
age = 25
quantity = 3
no_of_students = 30
#print(f"you are {age}years old")
#print(f"you are buying {quantity} items")
#print(f"your sec has {no_of_students} boys")

#float
price = 10.99
Gpa = 3.2
distance = 5.5
#print(f"The price is ${price}")
#print(f"your gpa is: {Gpa}")
#print(f"you ran {distance} km")

#boolean
is_student = False 
#if is_student:
 #    print("you are a student")
#else:
 #    print("you are not a student")    
for_sale =True
#if for_sale:
 #   print("That item is for sale")
#else:
 #   print("that item is not available")
is_online = False
#if is_online:
 #   print("you are online")
#else:
 #   print("your are offline")



#Typecasting = the processing of converting a variable from one data type to another
#               str(), int(), float(), bool()
name = "Sai coding "
age = 25
gpa = 3.2
is_student = True

#print(type(is_student))
gpa = int(gpa)
age = str(age)
name = bool(name)
gpa +=1
#print(name)



#input() =A function that prompts the user to enter data Returns the entered data as a string 
#name = input("what is your name?: ")
#age = int(input("how old are you ?: "))
#age = int(age)
#age +=1

#print(f"Hello {name}! ")
#print("Happy Birthday!")
#print(f"your age is {age}")


#exercise 1 Rectangle Area calc

#length = float(input("enter the length: "))
#width = float(input("enter the width: "))
#area = length*width
#print(f"The area is: {area}cm²")       #Alt+0178 -cm2


#exercise 2 shopping cart program

item = input("what item would you like to buy: ")
price = float(input("what is the price?: "))
quantity = int(input("how many would you like to buy?: "))
total = price*quantity
print(f"you have bought {quantity} x {item}/s")
print(f"your total bill: {total}")
      