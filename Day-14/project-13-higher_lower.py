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

# Function to print the choises and ask to choose
def round(choise_A , choise_B):
    """UI for the game"""
    print(f"Compare A : {choise_A['name']}, a {choise_A['description']}, from {choise_A['country']}\n")
    print(vs)
    print(f"\nAgainst B : {choise_B['name']}, a {choise_B['description']}, from {choise_B['country']}")
    return input("Who has more followers? Type 'A' or 'B' : ").lower()
    
# Function for deciding result of a round
def round_result(choise_A , choise_B , player_choise):
    """Returns True for correct choise and visa versa"""
    A_follwers = int(choise_A['follower_count'])
    B_follwers = int(choise_B['follower_count'])
    if A_follwers > B_follwers :
        if player_choise == 'a':
            return True
        else :
            return False
    else :
        if player_choise == 'b':
            return True
        else :
            return False

# Fuction for game
def higher_lower():
    """starts the higher-lower game"""
    clear()
    print(logo)
    # Generate random choises from data for first round
    import random
    choises = random.sample(data,2)
    choise_A = choises[0]
    choise_B = choises[1]

    answer = True
    score = 0
    while answer:
        player_choise = round(choise_A,choise_B)
        answer = round_result(choise_A , choise_B , player_choise)
        if answer :
            score += 1
            choise_A = choise_B
            choise_B = random.choice(data)
            while choise_A == choise_B:
                choise_B = random.choice(data)
            clear()
            print(logo)
            print(f"You're right! Current score: {score}")
        else :
            clear()
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")

higher_lower()