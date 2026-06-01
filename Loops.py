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

while  True:
    principle = float(input("enter the principle amount: "))
    if principle < 0:
        print("principle amount must be greater than 0")
    else:
        break
    
while True:
    rate = float(input("enter the  rate interest: "))
    if rate < 0:
        print("intrest rate  must be greater than 0")
    else:
        break

while True:
    time = float(input("enter the time in years: "))
    if time < 0:
        print("time period must be greater than 0")
    else:
        break

total = principle*(1+rate/100)**time
print(f"Balance after {time} years/s is: {total:.2f}")
