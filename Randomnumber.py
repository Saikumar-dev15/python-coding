import random
#print(help(random))

#number = random.randint(1,6)    #it will give random number from 1 to 6.
low =1
high = 100
#number = random.random()      #it will give random from 0 to 1 with decimals
#options = ("rock", "paper", "scissors")
#option = random.choice(options)              #choice is useful creating games.
#cards = ["2", "3", "4", "5", "6","7","8","9","10","J","Q","K","A"]
#random.shuffle(cards)
#print(cards)




#python number guessing game 
import random 

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num , highest_num)
guesses = 0
is_running = True

print("Python number Guessing game")
print(f"select a number between {lowest_num} and {highest_num}")

while is_running:
    
    guess = input("Enter your guess:  ")
    
    if guess.isdigit():
        guess = int(guess)                     # it will convert str to int.
        guesses += 1                           #here guess count will be increased.
         
        if guess < lowest_num or guess > highest_num:                               
             print("That number is out of range")
             print(f"please select a number blw {lowest_num} and {highest_num}")
        elif guess < answer :
            print("Too low! try again!")
        elif guess > answer:
            print("Too High! Try again!")
        else:
            print(f"correct! the answer was {answer}")
            print(f"number of guesses: {guesses}")
            is_running = False                                 #to exit the loop.
    else:
        print("Invalid number")
        print(f"please select a number blw {lowest_num} and {highest_num}")