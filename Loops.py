#while loop = a statement that will execute its block of code, as long as its condition remains true

#name = input("enter your name: ")

#while name == "":
#    print("you did not enter your name")
#    name = input("enter your name: ")
#print(f"Hello {name} ")
    
#age = int(input("enter your age: "))
#while age <=0:
#     print("your age can't be negative")    
#     age = int(input("enter your age: "))
#print(f"your age is {age}")

#food = input("enter a food you like (q to quite): ")
#while not food == "q":
#    print(f"you like {food}")
#    food = input("enter a food you like (q to quite): ")
#print("bye")


# python compound interest calculator

principle = 0
rate =0
time = 0

#while  True:
#    principle = float(input("enter the principle amount: "))
#    if principle < 0:
#        print("principle amount must be greater than 0")
#    else:
#        break
    #
#while True:
#    rate = float(input("enter the  rate interest: "))
#    if rate < 0:
#        print("intrest rate  must be greater than 0")
#    else:
#        break

#while True:
#    time = float(input("enter the time in years: "))
#    if time < 0:
#        print("time period must be greater than 0")
#    else:
#        break

#total = principle*(1+rate/100)**time
#print(f"Balance after {time} years/s is: {total:.2f}")









# for loops = execute a block of code a fixed number of times
#              you can iterate over a range , string , sequence, etc


#credit_card = "1234-5678-9012-3456"

#for i in range(1,10,3):
#for i in credit_card:
#for i in range(1,21):
#    if i == 13:                           #it will break the loop at 13.
#        print("unlucky number")
#        break
#    else: 
#        print(i)


#import time 
#my_time = int(input("enter the time in seconds: "))
#for i in range(my_time , 0 , -1):
#    seconds = i%60
#    minutes = int(i/60)%60
 #   hours = int(i/3600)
 #   print(f"{hours:02}:{minutes:02}:{seconds:02}")
 #   time.sleep(1)
#print("Time is up!") 


#Nested loops = a loop inside a loop(outer , inner)
#                 outerloop:
                      #inner loop:
    #print(i , end="")   # it will print the numbers in the same line

#rows =int(input("enter the number of rows: "))
#columns = int(input("enter the number of columns: "))
#symbol = input("enter a symbol to use: ")

#for i in range(rows):
#    for j in range(columns):
 #       print(symbol, end="")
 #   print()
 
 
 
#collection = single "variable" used to store multiple values
# List = [] ordered and changeable. Duplicates ok
# set = {}unorderdand immutable, but add/remove ok. no duplicates
# tuple = ()   ordered and unchangeable, Duplicates ok .Faster


#List concept
#fruit = ["apple" , "orange", "banana" , "grape" , "apple"]
#print(dir(fruit))                                         #it will show all the methods that we can use with the list
#print(help(fruit))                          #it will show the documentation of the list
#print(fruit[::-1])
#print("apple" in fruit)

#fruit[1] = " pine apple"
#fruit.append("orange")
#fruit.remove("banana")
#fruit.insert(0,"watermelon")
#fruit.sort()
#fruit.reverse()
#print(fruit.count("apple"))
#print(fruit)

#for i in fruit:
#    print(i)

#SET concept
fruit = ["apple" , "orange", "banana" , "grape" , "apple"]
#print(dir(fruit))
#print(help(fruit))
#fruit_set = set(fruit)
#print(fruit_set)
#fruit.add("pineapple")
#fruit.remove("banana")
#print(fruit)


#Tuple concept
fruit = ["apple" , "orange", "banana" , "grape" , "apple"]
#print(dir(fruit))
#print(help(fruit))
#print(len(fruit))

#print(fruit.index("apple"))
print(fruit.count("apple"))


