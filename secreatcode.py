# "'EXCERCISE 4 : Write a python program to translate a message into secreate code language . Use the rules below to translate normal english into secret code langauge . '"
# # CODING 
# "'If the word contains atleast 3 chaacters, remove the first letter and append it at the end now append three random charracters at the starting and the end . else : simply reverse the string '"
# # DECODING :
# "'If the word contains less than 3 charracters reverse it , else : remove 3 random charracters from start and end . now remove the last letter and append it to the beginning .'"

" IMPORTING FUNCTION "
import pygame 
import random
import string 
import time 

pygame.init()

" CREATING WINDOW  "
screen_width = 1200 
screen_height = 700 
gamewindow = pygame.display.set_mode((screen_width , screen_height))
pygame.display.set_caption (" SECREAT CODE ")

"COLOR"
white = (255,255,255)
black = (0,0,0)
red = (255,0,0 )

font = pygame.font.SysFont(None , 50)

"FUNCTION DISPLAY ON SCREEN"
def text_screen (text , color , x , y ):
    screen_text = font.render(text , True , color)
    gamewindow.blit(screen_text, (x,y))
    
def encode_decode (text, code = True):
    words = text.split ()
    nwords = []
    
    if code:
        for word in words :
            if len(word)>=3:
                a = ''.join(random.choices(string.ascii_lowercase, k=3))
                b = ''.join(random.choices(string.ascii_lowercase, k=3))
                scnew  = a + word[1:] + word[0] + b
                nwords.append(scnew)
            else:
                nwords.append(word[::-1])
    else :
        for word in words:
            if len(word)>=3:
                scnew = word[3:-3]
                scnew = scnew[-1] + scnew[:-1]
                nwords.append(scnew)
            else :
                nwords.append(word[::-1])
            
    return " ".join(nwords)

"MAIN LOOP"
running = True 
user_text = ""
result = ""
code = True 

while running:
    gamewindow.fill(white)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                result = encode_decode(user_text ,code)
                user_text = result
            elif event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]
            elif event.key == pygame.K_TAB:
                code = not code              # switch mode
            else:
                user_text += event.unicode  
# DISPLAY TEXT 
    text_screen ("Type messeage : " , black ,50, 100)
    hidden_text = "*"*len(user_text)
    text_screen(hidden_text ,black, 50, 150)
    
    mode = "ENCODE MODE" if code else "DECODE MODE"
    text_screen(mode + " PRESS ENTER TO PROCESS" , black , 50 , 320)
    
    text_screen("Result:" , black , 50 , 420)
    text_screen(result, black, 50, 480)
    
    pygame.display.update()
    
pygame.quit()