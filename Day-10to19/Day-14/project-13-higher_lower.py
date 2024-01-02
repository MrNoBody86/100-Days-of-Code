# Higher Lower Game

# import ascii art
from art import logo , vs

# import game data 
from game_data import data

# clear the terminal
def clear():
    """clears the terminal"""
    import os
    import sys
    # Linux
    if sys.platform.startswith('linux'):
        os.system('clear')
    # Windows
    elif sys.platform.startswith('win32'):
        os.system('cls')

# Function to print the choices and ask to choose
def round(choice_A , choice_B):
    """UI for the game"""
    print(f"Compare A : {choice_A['name']}, a {choice_A['description']}, from {choice_A['country']}\n")
    print(vs)
    print(f"\nAgainst B : {choice_B['name']}, a {choice_B['description']}, from {choice_B['country']}")
    return input("Who has more followers? Type 'A' or 'B' : ").lower()
    
# Function for deciding result of a round
def round_result(choice_A , choice_B , player_choice):
    """Returns True for correct choice and visa versa"""
    A_followers = int(choice_A['follower_count'])
    B_followers = int(choice_B['follower_count'])
    if A_followers > B_followers :
        if player_choice == 'a':
            return True
        else :
            return False
    else :
        if player_choice == 'b':
            return True
        else :
            return False

# Function for game
def higher_lower():
    """starts the higher-lower game"""
    clear()
    print(logo)
    # Generate random choices from data for first round
    import random
    choices = random.sample(data,2)
    choice_A = choices[0]
    choice_B = choices[1]

    answer = True
    score = 0
    while answer:
        player_choice = round(choice_A,choice_B)
        answer = round_result(choice_A , choice_B , player_choice)
        if answer :
            score += 1
            choice_A = choice_B
            choice_B = random.choice(data)
            while choice_A == choice_B:
                choice_B = random.choice(data)
            clear()
            print(logo)
            print(f"You're right! Current score: {score}")
        else :
            clear()
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")

higher_lower()