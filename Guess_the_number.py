import random
print("Welcome to the game")
response=input("Ready to play? yes or no? ")
while response=="yes" or response=="Yes":
    num=random.randrange(100)
    guess=int(input("Time to giess the number(0-100). Please provide your guess!"))
    if guess==num:
        print("Your guess was correct. Congrats!")
    elif guess>num:
        print("your guess was much larger. The answer is: ",num)
    elif guess<num:
        print("your guess was much smaller. The answer is: ",num)
    else:
        print("your guess was out of the range.Try again!")
    response=input("Wanna play again? yes or no? ")

print("Thanks for playing..!")
              
          
    
