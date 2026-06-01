#name = input("Enter your name: ")
#phone_number = input("Enter your phone number: ")
#result = len(name)
#result = name.find("a")
#result = name.rfind("a")      #find the last index of a
#result = name.capitalize()     #first letter will be captial
#result = name.upper()          #all letters will be upper case
#result = name.lower()          #all letters will be lower case
#result = name.isdigit()         #check if all characters are digits
#result = name.is alpha()        #check if all characters are alphabetic
#phone_number = phone_number.count()   #count the number of characters in the phone number
#phone_number = phone_number.replace("-","")   #remove the dashes from the phone number
#print(phone_number)



#Exercise on string manipulation
#validation user input exercise
#1. username is no more than 10 characters
#2. username should not contain spaces
#3  username must not contain digits

#username =input("Enter your name: ")

#if len(username)>12:
#    print(" your username should be no more than 12 characters")
#elif not username.find(" ")==-1:
#    print("your username should not contain spaces")
#elif not username.isalpha():
#    print("your username should not contain digits")
#else:
# #print(f"welcome {username}")



#indexing =accessing elements of a sequence using[]
#            [start: end: step]
#credit_number = "1234-5678-9012-3456"
#print(credit_number[:4])   
#print(credit_number[0:4])
##print(credit_number[5:])
#print(credit_number[-1])
#print(credit_number[::3])  #print every 3rd character in the string


#format specifiers = {value:flags} format a value based on what flags you use
#.(number)f = round to that mant decimal places(fixed point)
#:(number) =allocate that many spaces
#:03 = allocate and zero pad that many spaces
# :< = left align
# :> = right align
# :^ = center align
# :+ = show the sign of a numberpositive  
# := = show the sign of a number at the beginning of the output
# :  = show a space before positive numbers and a minus sign before negative numbers
# :, = comma separator


price1 = 3786.1415
price2 = -93748.456
price3 = 12897.34

#print(f"price1: {price1:.3f}")  #round to 3 decimal places
#print(f"price1: {price1:10}")   #allocate 10 spaces for the price1
#print(f"price1: {price1:<10}")
#print(f"price1: {price1:>10}")   
#print(f"price1: {price1:+}")    #show the sign of the number
#print(f"price1: {price1: }")
#print(f"price1: {price1:,}")
print(f"price1: {price1:+,.2f}")   #show the sign of the number, round to 2 decimal places and use comma as a thousand separator
print(f"price2: {price2:+,.2f}")   #show the sign of the number, round to 2 decimal places and use comma as a thousand separator
print(f"price3: {price3:+,.2f}")   #show the sign of the number, round to 2 decimal places and use comma as a thousand separator