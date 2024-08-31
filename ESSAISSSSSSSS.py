import random
print("Welcome to the Guess the Number game! \n I'm thinking of a number between 1 and 100. Can you guess what it is?")
print(" READY!!! SO Let's start")
my_guess=input("ENTREZ UN GUESS\n")

def convertible(x):
    try :
      int(x)
      return 1
    except ValueError:
       return 0
   
   
while convertible(my_guess)==0:
    my_guess=input("ENTREZ UN nombre svp\n")
    
my_guess=int(my_guess)   
attempts=1
max_attempts=5
correct_number=random.randint(1,100)
cpt=1

while attempts < max_attempts :

    if my_guess==correct_number:
        print("CONHGRATULATIONS!!! U GUESSED RIGHT")
        break
    elif my_guess == correct_number -1 or my_guess == correct_number +1 :
        print("U RE SO NEAR TO FIND THE RIGHT NUMBER.PLEASE KEEP GOING")
    elif my_guess > correct_number +1 :
        print("The guess is too high")
    elif my_guess < correct_number-1 :
        print("The guess is too low")
    attempts+=1
    try:
        my_guess=int(input("RETENTEZ VOTRE CHANCE\n"))
        cpt+=1
        print(f"BE CAREFUL YOU HAVE {max_attempts-cpt} ATTEMPTS LEFT")
    except ValueError:
        print("Vous devez entrer un entier svp")
if attempts==max_attempts and my_guess!= correct_number :
    print(f"u reached the max of attempts\n The correct number was {correct_number}")
    print("THE GAME IS OVER. BETTER LUCK NEXT TIME IN SHAA ALLAH")
   
   
   
   
   
   
    

    


    
        
