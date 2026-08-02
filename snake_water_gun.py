"PROJECT  : SNAKE,WATER,GUN"
import random 

option= ["snake", "water", "gun"]
krishn_wins=0 
user_wins=0

user_input= ["snake", "water", "gun"]

while True :  
    user_input= input("Type snake/water/gun or q for quite : ").lower()


    if user_input=="q":
        break

    if user_input not in option :
        continue

    krishn_input=random.choice(option)
    print(f"krishn choose = {krishn_input}")

    if user_input==krishn_input:
        print("draw")
    elif user_input=="snake" and krishn_input=="water":
        print("you won!")
        user_wins+=1
    elif user_input=="water" and krishn_input=="gun":
        print("you won!")
        user_wins+=1
    elif user_input=="gun" and krishn_input=="snake":
        print("you won!")
        user_wins+=1
    else:
        print("you lost!")
        krishn_wins+=1

print("you won" ,user_wins,"times" )
print("krishn won ", krishn_wins,"times")