import random
import data
print("Welcome to the Hangman game")
name=input("What is your name?")
print("Hey {}! Welcome to the game, you will be given clues and you have to guess the word. You'll get only 3 chances to guess the word.".format(name.upper()))
response=input("Are you ready to play! Yes or No? ")
counter=0
flag=0
vowels=['a','e','i','o','u']
if response=="Yes" or "yes":
    while response=="Yes" or response=="yes":
        f=0
        v=0
        flag=0
        counter=0
        states=0
        chem=0
        print("Game Menu: \n1:Guess the fruit \n2:Guess the colour \n3:Guess the indian state \n4:Guess the element of periodic table")
        choice=int(input("Enter your choice(1 or 2 or 3 or 4)? "))
        if choice==1:
            ans=random.choice(data.fruits)
        elif choice==2:
            ans=random.choice(data.colours)
        elif choice==3:
            ans=random.choice(list(data.indian_states.keys()))
            states=1
        elif choice==4:
            ans=random.choice(list(data.chemistry.keys()))
            chem=1
        else:
            print("Invalid choice. Try again")
            f=1
        if f==0:
            print("The game is started. Your clues are:")
            if states==1:
                for i in ans:
                    if i in vowels:
                        v+=1
                print("The capital of the state is:",data.indian_states.get(ans))
                print("The no. of vowels in the word are:",v)
            elif chem==1:
                for i in ans:
                    if i in vowels:
                        v+=1
                print("The atomic number of the element is:",data.chemistry.get(ans))
                print("The no. of vowels in the word are:",v)
            else:
                for i in ans:
                    last=i
                for i in ans:
                    if i in vowels:
                        v+=1
                print("The last letter of the word is ",last)
                print("The no. of vowels in the word are ",v)
            guess=input("Now, enter your guess: ")
            if ans==guess or ans==guess.lower():
                print("Wow..!Your guess was correct.")
                print("You win")
                flag=1
            else:
                while counter!=4:
                    counter+=1
                    print("Oh no..!Your guess was wrong.")
                    guess=input("Make a new guess:")
                    if ans==guess or ans==guess.lower():
                        print("Wow..!Your guess was correct.")
                        print("You win")
                        flag=1
                        break
            if flag==0:
                print("You lost..! The correct word was ",ans)
            response=input("Wanna play again? Yes or No: ")
            if response=="no" or response=="NO":
                print("Thanks {} for playing.".format(name))
else:
    print("Thanks {} for your response.".format(name))

    
            
            
    
