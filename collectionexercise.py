# shopping cart program 

#foods = []            #[]-list for duplicates concerns
#prices = []           #[]-list for sequence order
#total = 0

#while True:
#    food = input("Enter a food to buy (q to quite): ")
#    if food == "q":
#        break
#    else:
#        price = float(input(f"enter the price of a {food}: $"))
#        foods.append(food)
#        prices.append(price)

#print("---- YOUR CART ----")
#for food in foods:
#    print(food, end=" " )

#for price in prices:
#    total += price
    
#print()    
#print(f"your total is : ${total}") 




#2D collection 
# 2dlist= [list1, list2, list3]

#fruits = ["apple" , "orange" , "banana", "cocunut"]
#vegetables = ["carots", "potatos", "brinjal",  "Tomato"]
#meats = ["chicken", "mutton", "fish", "rabit"]

#groceries = [fruits, vegetables, meats]
#print(groceries[0][1])        # it will give specific quntity
#print(groceries[1][1])

#groceries = [["apple" , "orange" , "banana", "cocunut"],
#             ["carots", "potatos", "brinjal",  "Tomato"],

#["chicken", "mutton", "fish", "rabit"]]
#for collection in groceries:
#    for food in collection:
#        print(food, end=" ")
#    print()


#num_pad = ((1,2,3),
#           (4,5,6),
#           (7,8,9),
#           ("*",0,"#"))

#for row in num_pad:
#    for num in row:
#        print(num, end=" ")
#    print()



#play quizz game

#questions = ("How many elements are in the periodic table?: ",
#              "which  animal lays larger eggs?:  ",
#              "what is the most abundant gas in earth's atmosphere?: ",
#              "how many bones are in the human body?: ",
#              "which planet in the solar system is the hottest?: ")

#options = (("A.115 ", "B.116 ", "C.117 ", "D.118 "),
#           ("A. whale", "B.crocodile ", "C. Ostrich ", "D. hen "),
#           ("A. Nitrogen ", "B. Oxygen ", "C. Co2 ", "D. hydrogen "),
#           ("A. 208", "B.207 ", "C.206 ", "D.209 "),
#           ("A.Mercury ", "B.Mars ", "C.earth ", "D.venus "))

#answers = ("D", "C", "A", "C", "B")
#guesses = []
#score = 0
#question_num = 0

#for question in questions:
#    print("-------------------")
#    print(question)
#    for option in options[question_num]:         # options will display according to our question number.
#        print(option)
        

#    guess = input("Enter (A,B,C,D):  ").upper()     
#    guesses.append(guess)                          
#    if guess == answers[question_num]:           
#        score +=1
#        print("CORRECT!")
#    else:
#        print("INCORRECT")
#        print(f"{answers[question_num]} is the correct answer")
#    question_num +=1    
    
    
#print("----------------------")
#print("      RESULTS         ")
#print("----------------------")

#print("answers:  ", end=" ")
#for answer in answers:
#    print(answer, end=" ")
#print()


#print("guesses:  ", end=" ")
#for guess in guesses:
#    print(guess, end=" ")
#print()

#score = score/ len(questions)*100

#print(f"Your final score : {score}%")




#Dictionary = a collection of {key: value} pairs
#             ordered and changeable. No duplicates

capitals = {"USA": "Washington D.C" ,
            "INDIA": "New Delhi",
            "China": "Beijing",
            "RUSSIA": "Moscow"}

#print(dir(capitals))
#print(help(capitals))
#print(capitals.get("USA"))

#if capitals.get("INDIA"):
#    print("THAT CAPITAL  EXISIT")
#else:
#    print("That capital is doesn't exist")

#capitals.update({"Germany": "Berlin"})
#capitals.update({"USA": "Detroit"})
#capitals.pop("China")
#captials.clear()
#print(capitals)
#keys = capitals.keys()
#for key in capitals.keys():
#    print(key)

#values = capitals.values()
#for value in capitals.values():
#    print(value)

#items = capitals.items()
#for key, value in capitals.items():
#    print(f"{key}: {value}")
    
    
#concession stand program

menu = {"pizza": 3.00,
        "nachos":4.50,
        "popcorn": 6.00,
        "fries":2.50,
        "chips":1.00,
        "soda":3.00,
        "lemonade":4.25}
     
cart = []
total = 0

print("----------MENU----------")
for key, value in menu.items():
    print(f"{key}: ${value:.2f}")
print("--------------------------------")

while True:
    food=input("select the item (q or quite): ").lower()         #lower() will convert all the capital to small letters.
    if food == "q":
        break
    elif menu.get(food) is not None:          #this will run if the condition is != q and check the menu list and add in cart.
        cart.append(food)
        
for food in cart:
    total += menu.get(food)                  #it will finalise the bill of our food.
    print(food, end=" ")
print()
print(f"Total is: {total: .2f}")