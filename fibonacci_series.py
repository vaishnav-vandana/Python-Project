"""
QUIZ QUIZ / EXERCISE   : WRITE A PROGRAM TO PRINT THE FIBONACCI SEQUENCE 
f(0) = 0 
f(1) = 1
f(2) = f(1)+f(0)
f(n)= f(n-1)+ f(n-2)
"""

# print("my code :")                                            # i use print statement that's wrong , by this this program didnot run 
# def fibonacci (n):
#     if (n<=0):
#         print(0)
#     elif (n==1):
#         print(1) 
#     else:
#         print(fibonacci(n-1)+fibonacci(n-2))
# n= int (input ())
# for i in range (n):
#     print (fibonacci(i))

print("MY ANSWER :")
def fibonacci (n):
    if n<=0 :
        return(0)
    elif n==1 :
        return(1)
    else :
        return(fibonacci(n-1)+fibonacci(n-2))
n = int (input ("Enter the number : "))
for i in range (n):
    print (fibonacci(i))
    
# OUTPUT :
"""
MY ANSWER : 
Enter the number : 5                                                 # user input 
0
1
1
2
3
"""