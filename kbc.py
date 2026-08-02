"EXCERCISE 3 :KAUN BANEGA CROREPATI "

import time 

que = [
    ["how many zeroes are there in hundred?", "seven", "four", "two", "six", 3],
    ["what is not the capital of india?", "delhi", "old delhi", "new delhi", "all", 2],
    ["who live in home?", "lion", "people", "jackel", "rabbit", 2],
  ]

print ("welcome to hot seat round 🎉:")
for i in range (len(que)):
    question=que[i]
        
    print (f"\nQuestion {i+1}: {question[0]}")
     
    print (f"a. {question[1]}    b. {question[2]}")
    print (f"c. {question[3]}    d. {question[4]}")

    reply= int(input("enter your answer(1-4):"))
    if reply==question[-1]:
        print("correct answer✅!")
        print ("congratulation !you may became crorepati ")
    else:
        print ("wrong answer❌!")
        print ("next time !")
        break 
        
import pygame        
pygame.init()
pygame.mixer.music.load('MUSIC AND PHOTOS/kbc-starting.mp3')
pygame.mixer.music.play()   
    
questions =[

    ["what is capital of maharashtra?", "raipur", "bhopal", "dispur", "mumbai", 4],   
    ["which is  the capital of india?", "delhi", "old delhi", "new delhi", "all", 3],
    ["who is sheep of desert?", "lion", "tiger", "camel", "rabbit", 3],
    ["what is fundamental unit of our life?", "blood", "motion", "eight", "cell", 4],
    ["what city is known as white city?", "kanpur", "jaipur", "raipur", "udaipur", 4],
    ["who is at present president of india ?", "rajaram", "rajendra prasad", "droupadi murmu", "narendra modi", 3],
    ["how many states  in america ?", "seventeen", "ninetynine", "eight", "fifty", 4],
    ["what is the capital of pakistan?", "gandhi nagar", "islambad", "dhaka", "london", 2],
    ["who is known as fathre of maths ?", "aryabhatta", "archimedes", "s.v patel", "ramanujan", 2],
    ["who wrote bhagvat geeta?", "valmiki", "ved vyasa", "lord ganesh", "both b and c",4],
    ["hyderabad is capital of which state?", "kerala", "tamil nadu ", "Karnataka", "telangana", 4],
    ["which is first british rular ?", "warren hastin", "loud mountbeen", "ganesh", "valmiki", 1],
    ["avatar of shivji ?", "hanumaan", "ram", "matsya", "all", 1],
    ["which is  our third planet ?", "earth", "moon", "sun ", "pluto", 1],
     
  ]

levels = [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,5000000,70000000]

for i in range (0,len(questions)):
    question=questions[i]   
    print (f"\n\nQuestion for rs.{levels[i]}:")
    print(question[0])     
    print (f"a. {question[1]}    b. {question[2]}")
    print (f"c. {question[3]}    d. {question[4]}")
    pygame.mixer.music.load('MUSIC AND PHOTOS/kbc-question.mp3')
    pygame.mixer.music.play()  

    pygame.time.delay(8000) 

    reply = int(input("Enter your answer (1-4) or 0 to quit: "))
  
    if (reply==0):
        money = levels[i-1] if i > 0 else 0 
        break

    if (reply==question[-1]):
        print (f"✅ correct answer you won Rs. {levels[i]}")
        if (i==4):
            money =10000
        elif (i==9):
            money =320000
        elif (i==13):
            money = 70000000 

            pygame.mixer.music.stop()
            
            pygame.mixer.music.load('MUSIC AND PHOTOS/7_crore_meme_sound_kbc.mp3')
            pygame.mixer.music.play() 

            
            while pygame.mixer.music.get_busy():
                time.sleep(0.5)

        else :
            money = levels[i]    
    else:
        print ("❌wrong answer !")
        break
else :
    money = levels [-1]

print (f"💼your take home money is rs : {money}")