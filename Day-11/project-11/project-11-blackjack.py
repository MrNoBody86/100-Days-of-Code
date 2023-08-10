############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

###############################################################

import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

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

def Score_calculator(player):
    """Calcutes current score of the player."""
    player["score"] = sum(player["card"])
    if 11 in player["card"] and player["score"] > 21 :
        player["card"][player["card"].index(11)] = 1
      
def hit(player):
    """Adds a card."""
    player['card'].append(random.choice(cards))
    Score_calculator(player)

def view_current_score():
    """Print the current score to the user."""
    print(f"    Your cards: {user['card']}, current_score: {user['score']}")
    print(f"    Computer's first card: {computer['card'][0]}")

def end_game():
    """Print specific stament everytime the game ends."""
    print(f"    Your final hand: {user['card']}, final score: {user['score']}")
    print(f"    Computer's final hand: {computer['card']}, final score: {computer['score']}")

play = True
clear()
while play :
    re = input("Do you want to play a game of Blackjack? Type 'y' or 'n':").lower()
    user = {
        "card" : [],
        "score" : 0,
    }
    computer = {
        "card" : [],
        "score" : 0,
    }
    if re == 'y' :
        clear()
        print(logo)
        for _ in range(2):
            hit(user)
            hit(computer)
        view_current_score()
        if user['score'] == 21 :
            end_game()
            if computer["score"] == 21 :
                print("Draw.")
            else:
                print("Win with a Blackjack.")
        else:
            another_card = True
            while another_card :
                ac = input("Type 'y' to get another card, type 'n' to pass:").lower()
                if ac == 'y' :
                    hit(user)
                    if user["score"] > 21 :
                        end_game()
                        print("You went over. You lose.")
                        break
                    elif user["score"] == 21 :
                        if computer["score"] < 22 :
                            while computer["score"] < 17:
                                hit(computer)
                            if computer["score"] == 21 :
                                end_game()
                                print("Draw.")
                                break
                            else :
                                end_game()
                                print("You win!")
                                break
                        else:
                            end_game()
                            print("You win!")
                            break
                    else :
                        view_current_score()
                else :
                    another_card =False
            if ac == 'n' :
                while computer["score"] < 17:
                    hit(computer)
                end_game()
                if computer["score"] > 21 or user["score"] > computer["score"]:
                    print("You win!")
                elif computer["score"] == user["score"] :
                    print("Draw.")
                else :
                    print("You lose.")
    else :
        play = False