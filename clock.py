# QUESTION 1:/EXERCISE 2: Create a python program capable of greeting you with good morning , good afternoon , good evening . Your program should use time module to get the current hour . 

print ("MY ANSWER:")
time = int(input ("enter the time : ")) 
name = input ("your name : ")
if (time>=0 and time<12):
    print ("good morning" , name )
elif(time >=12 and time <18 ):
    print ("good afternoon " ,name )
elif (time >=18 and time <24):
    print ("good evening ",name )
else :
    print ("jai shree krishna")

"OR"

print ("code with harry :")
import time 
timestamp= time.strftime('%H:%M:%S')
print (timestamp)
timestamp=time.strftime('%H')
print (timestamp)
timestamp=time.strftime('%M')
print (timestamp)
timestamp=time.strftime('%S')
print (timestamp)

# OUTPUT :
"""
MY ANSWER:
enter the time : 4                                                     # user input 
your name : KRISHN                                                     # user input 
good morning KRISHN
code with harry :
22:17:53
22
17
53
"""