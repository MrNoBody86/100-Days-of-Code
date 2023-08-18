from art import logo
import random

def clear():
    """clears the terminal(only for vscode)"""
    import os
    import sys
    # Linux
    if sys.platform.startswith('linux'):
        os.system('clear')
    # Windows
    elif sys.platform.startswith('win32'):
        os.system('cls')

def guess_the_number() :
    clear()
    print(logo)

    #Choosing a random number between 1 and 100.
    print("Welcome to the Number Guessing Game!")
    print("The number I've chosen is between 1 to 100")
    chosen_number = random.randint(1,100)

    #set difficulty.
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard' : ").lower()
    if difficulty == 'easy' :
        no_of_attempts = 10
    else :
        no_of_attempts = 5

    #Repeat the guessing functionality if they get it wrong.
    while no_of_attempts != 0 :
        print(f"You have {no_of_attempts} attempts remaining to make the guess")

        #Let the user guess a number.
        guessed_number = int(input("Make a guess : "))
        
        #Function to check user's guess against actual answer.
        #Track the number of turns and reduce by 1 if they get it wrong.
        def check_guess():
            if chosen_number > guessed_number :
                print("Too low.")
                return no_of_attempts - 1
            elif chosen_number < guessed_number :
                print("Too high.")
                return no_of_attempts - 1
            else:
                print(f"You got it! The answer was {chosen_number}.")
                return no_of_attempts - 1
        
        no_of_attempts = check_guess()

        if no_of_attempts == 0 and chosen_number != guessed_number:
            print("You've run out of guesses. You lose.") 
        elif chosen_number != guessed_number:
            print("Guess again.")   


guess_the_number()