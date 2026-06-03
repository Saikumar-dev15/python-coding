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
#import random 

#lowest_num = 1
#highest_num = 100
#answer = random.randint(lowest_num , highest_num)
#guesses = 0
#is_running = True

#print("Python number Guessing game")
#print(f"select a number between {lowest_num} and {highest_num}")

#while is_running:
    
#    guess = input("Enter your guess:  ")
    
#    if guess.isdigit():
#        guess = int(guess)                     # it will convert str to int.
#        guesses += 1                           #here guess count will be increased.
         
#        if guess < lowest_num or guess > highest_num:                               
#             print("That number is out of range")
#             print(f"please select a number blw {lowest_num} and {highest_num}")
#        elif guess < answer :
#            print("Too low! try again!")
#        elif guess > answer:
#            print("Too High! Try again!")
#        else:
#            print(f"correct! the answer was {answer}")
#            print(f"number of guesses: {guesses}")
#            is_running = False                                 #to exit the loop.
#    else:
#        print("Invalid number")
#        print(f"please select a number blw {lowest_num} and {highest_num}")





#ROCK PAPER SCISSORS GAME

#import random

#options = ("rock", "paper", "scissors")
#player = None
#computer = random.choice(options)
#running = True


#def new_func():
#    if not input("play again? (y/n): ").lower() == "y":
#        running = False

#while running:
#    while player not in options:
#        player = input("Enter a choice (rock, paper, scissors): ")

#    print(f"player: {player}")
#    print(f"Computer: {computer}")

#    if player == computer:
#        print("Tie")

##    elif player == "rock" and computer == "scissors":
#        print("you win")
#    elif player == "paper"  and computer == "rock":
#        print("you win")
#    elif player == "scissors" and computer == "paper":
#        print("you win")
#    else:
#        print("you loose")
        
#    new_func()
#print("Thanks for playing!")





#DICE ROLL PROGRAM

import random

#print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")

#● ┌ ─ ┐ │ └ ┘


"┌───────────────┐"
"│               │"
"│               │"
"│               │"
"└───────────────┘"

dice_art = {
    1: ("┌───────────────┐",
        "│               │",
        "│       ●       │",
        "│               │",
        "└───────────────┘"),
    2: ("┌───────────────┐",
        "│   ●           │",
        "│               │",
        "│          ●    │",
        "└───────────────┘"),
    3: ("┌───────────────┐",
        "│   ●           │",
        "│       ●       │",
        "│           ●   │",
        "└───────────────┘"),
    4: ("┌───────────────┐",
        "│   ●       ●   │",
        "│               │",
        "│   ●       ●   │",
        "└───────────────┘"),
    5: ("┌───────────────┐",
        "│ ●         ●   │",
        "│       ●       │",
        "│ ●          ●  │",
        "└───────────────┘"),
    6: ("┌───────────────┐",
        "│  ●    ●     ● │",
        "│               │",
        "│  ●     ●    ● │",
        "└───────────────┘")    
}

dice = []
total = 0
num_of_dices = int(input("How many dices?: "))

for die in range(num_of_dices):
    dice.append(random.randint(1,6))
    
#for die in range(num_of_dices):
#    for  line in dice_art.get(dice[die]):                           # To get the picture of the every dice             #  
#        print(line)
 
for line in range(5):                                               # Total range 1 to 6 = 5 index
    for die in dice:
        print(dice_art.get(die)[line], end=" ")                     #it will print all dices in single row....... 
    print()    
    
for die in dice:
    total += die
print(f"Total number : {total}")


