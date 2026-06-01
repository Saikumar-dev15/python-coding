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

groceries = [["apple" , "orange" , "banana", "cocunut"],
             ["carots", "potatos", "brinjal",  "Tomato"],

["chicken", "mutton", "fish", "rabit"]]
for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()



