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

questions = ("How many elements are in the periodic table?: ",
              "which  animal lays larger eggs?:  ",
              "what is the most abundant gas in earth's atmosphere?: ",
              "how many bones are in the human body?: ",
              "which planet in the solar system is the hottest?: ")

options = (("A.115 ", "B.116 ", "C.117 ", "D.118 "),
           ("A. whale", "B.crocodile ", "C. Ostrich ", "D. hen "),
           ("A. Nitrogen ", "B. Oxygen ", "C. Co2 ", "D. hydrogen "),
           ("A. 208", "B.207 ", "C.206 ", "D.209 "),
           ("A.Mercury ", "B.Mars ", "C.earth ", "D.venus "))

answers = ("D", "C", "A", "C", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("-------------------")
    print(question)
    for option in options[question_num]:
        print(option)
        
    guess = input("Enter (A,B,C,D):  ").upper() 
    guesses.append(guess)
    if guess == answers[question_num]:
        score +=1
        print("CORRECT!")
    else:
        print("INCORRECT")
        print(f"{answers[question_num]} is the correct answer")
    question_num +=1    
    
    
print("----------------------")
print("      RESULTS         ")
print("----------------------")

print("answers:  ", end=" ")
for answer in answers:
    print(answer, end=" ")
print()


print("guesses:  ", end=" ")
for guess in guesses:
    print(guess, end=" ")
print()

score = score/ len(questions)*100

print(f"Your final score : {score}%")