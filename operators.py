friends = 4
#friends +=1
#friends **=2
remainder = friends % 4

#print(remainder)
x= 3.14 
y=-2
#result = round(y)
#result = abs(y)
#result = pow(4,3)
#result = max(x,y)
#print(result)


import math
#print(math.pi)
#print(math.e)
#results = math.sqrt(4)
#results =math.ceil(x)
#results = math.floor(x)
#print(results)

#exercise on circumference of a circle
#radius = float(input("Enter the radius of the circle: "))
#circumference = 2* math.pi *radius
#print(f"the circumference is: {round(circumference, 2)}")

#exercise on area of a circle
#radius = float(input("Enter the radius of the circle: "))
#area = math.pi * math.pow(radius,2)
#print(f"the area is: {round(area, 2)}")


#if else staements

#age = int(input("enter your age:"))
#if age>=19:
#    print("you are now signrd up!:")
#elif age<10:
#    print("your are too young to sign up")
#elif age>=16 and age<19:
#    print("you should wait for a few years to signup")#
#else:
#    print("you must be to cross 19+ years old to sign up")


#response = input("would you like food?  (y/n):")
#if response == "y":
#    print("here is your food")
#else:
#    print("okay, we will have next time ")



#python calculator 

#operator = input("enter a operator (+,-,*,/)")
#num1 = float(input("enter first number: "))
#num2 = float(input("enter second number:"))
#print(f"you entered: {num1} {operator} {num2}")
#if operator == "+":
#    result = num1 + num2
#    print(f"the addtion value is : {result}")
#elif operator == "-":
#    result = num1 - num2
#    print(f"the subtraction value is : {result}")
#elif operator == "*":
#    result = num1 *num2
#    print(f"the multiplication value is : {result}")
#else:
#   result =num1 / num2
#    print(f"the division value is : {result}")
    
    
    
#python weight converter

#weight = float(input("enter your weight"))
#unit = input("enter the weight in (K or L): ")    # in kilograms or pounds
#if unit == "K":
#    weight = weight * 2.20462
#    unit = "lbs"
#elif unit == "L":
#    weight = weight / 2.20462
#    unit = "kg"
#else:
#    print("unit is invalid")
    
#print(f"your weight is : {round(weight, 3)} {unit}")


#python temperature converter

#temp = float(input("enter the temperature:"))
#unit = input("enter the unit (K or F): ")   # in kelvin or fahrenheit
#if unit == "K":
#    temp = temp-273.15
#    unit = "F"
#elif unit == "F":
#    temp = (temp - 32) * 5/9
#    unit = "K"
#else:
#    print("unit is invalid")
    
#print(f"the temperature is : {round(temp,2)} {unit}")
 
#logic operators = evaluate multiple conditions at the same time
                   #or = at least one condition is true
                   #and = all conditions must be true   
                   #not = reverses the result, returns false if the result is true
 
temp = 25
#is_raining = True
is_sunny = True

#if temp > 20 and is_sunny:
 #   print("it is hot outside ")
#    print("use sunscreen and wear a hat") 
#else:
#    print("it is cold outside ")
#    print("wear a jacket and wear cotton clothes to warm up")
 
 
 #conditional expressions = A one line if else statement that evaluates something based on a condition being true or false(ternary operator)
 #                           print or assign one of the two values based on a condition
                           
                           
num =5
a = 6
b=7
age = 25
user_role = "guest"

#print("positive " if num>0 else "negative   ")
#result = "even" if num%2==0 else "odd"
#max_num =  a if a>b else b
#min_num = a if a<b else b
#status = "Adult" if age >=18 else "Minor"
#role = "Guest" if user_role =="guest" else "Admin"
#print(role)

                   
    
