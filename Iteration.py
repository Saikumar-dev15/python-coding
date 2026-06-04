#Iterables = An object/collection that can be return its element one at a time,
#             allowing it to be iterated over in a loop. turple,str,dict also work 

#fruits = {"apple ", "orange", "banana", "coconut"}   #set

#for fruit in fruits:
#    print(fruit)


#Membership operators = used to test whether a value or variable is found in a sequence
#                       (str,list,tuple, set, or dictionary)
#                       1. in 
#                       2. not in

#word = "APPLE"
#letter = input ("Guess a letter in the secret word: ")

#if letter in word:
#    print(f"there is a {letter}")
#else:
#    print(f"{letter} is not there")



#word = "APPLE"
#letter = input ("Guess a letter in the secret word: ")

#if letter not in word:
#    print(f"{letter}  was not found")
#else:
#    print(f" there is a {letter}")



# List comprehension = Aconcise to create lists in python.
#                      Compact and Easier to read than traditional loops
#                      [expression for value in iterable if condition]


doubles = []                                  #Manual method
for x in range(1,11):
    doubles.append(x * 2)

#print(doubles)

doubles = [x * 2 for x in range(1, 11)]          #List comprehension method
triples = [y * 3 for y in range(1,11)]
squares = [z * z for z in range (1,11)]

#print(squares)

fruits = ["apple" , "orange", "mango", "banana"]
#fruits = [fruit.upper() for fruit in fruits ]
fruits = [fruit[0] for fruit in fruits ]          #it will print index 0 alphabets
#print(fruits)

numbers = [1 ,2, 3, -2, -6, -10]
positive_numbers = [num for num in numbers if num>=0]
negative_numbers = [ num for num in numbers if num<= 0]
even_numbers = [ num for num in numbers if num%2 == 0]
#print(even_numbers)

grades = [85, 42, 79 , 98, 56, 61, 31]
passing_grades = [grade for grade in grades if grade>=40]
#print(passing_grades)



#Match case statement (switch) : An alternative to using many 'elif' staements

def day_of_week(day):
    match day:
        case 1:
            return "It is Monday"        
        case 2:
            return "It is Monday"
        case 3:
            return "It is Monday"
        case 4:
            return "It is Monday"
        case 5:
            return "It is Monday"
        case 6:
            return "It is Monday"
        case 7:
            return "It is Monday"
        case _:
            return "Not a valid day"
        
#print(day_of_week(1))


def is_weekend(day):
    match day:
        case "sunday" | "saturday":
            return True        
        case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
            return False
        case _:
            return False
        
print(is_weekend("sunday"))





