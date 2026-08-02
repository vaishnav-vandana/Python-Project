"PROJECT : ROCK , PAPER , SCISSORS "

import random 

user_wins = 0
computer_wins = 0
draws = 0

options = ["rock","paper","scissors"]

print("WELCOME TO ROCK PAPER SCISSORS GAME")

while True:
    user_input = input("Type Rock/paper/scissors or q to quit : ").lower().strip()
    # QUIT CONDITION
    if user_input == "q":
        break
    # INVALID SITUATION
    if user_input not in options:
        print("Invalid choice try again")
        continue
    computer_pick = random.choice(options)
    print(f"computer picked : {computer_pick}")
    
    # DRAW CONDITION
    if user_input == computer_pick:
        print ("DRAW")
        draws +=1
    # WIN CONDITION
    elif (
        (user_input == "rock" and computer_pick == "scissors") or
        (user_input == "paper" and computer_pick == "rock") or
        (user_input == "scissors" and computer_pick == "paper")
    ):
        print ("YOU WON")
        user_wins += 1
    # LOSE CONDITION 
    else:
        print("YOU LOSE")
        computer_wins += 1
print("YOU WON" ,user_wins ,"times")
print("COMPUTER WON" ,computer_wins,"times")
print("DRAW",draws,"times")