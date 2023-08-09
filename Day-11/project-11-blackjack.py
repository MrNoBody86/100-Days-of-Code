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

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run
import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user = {
    "card" : [],
    "score" : 0,
}

computer = {
    "card" : [],
    "score" : 0,
}


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

def deal():
    """At the start of the game distributes two cards to each player"""
    user["card"].append(random.choice(cards))
    user["card"].append(random.choice(cards))
    computer["card"].append(random.choice(cards))
    computer["card"].append(random.choice(cards))
    Ace_value(user)
    Ace_value(computer)
    

def Score_calculator(player):
    """Calcutes current score of the player."""
    player["score"] = 0
    for card in player["card"]:
            player["score"] += card

def Ace_value(player):
    """Dicides the value of ace if present."""
    Score_calculator(player)
    for card in player["card"] :
        if card == 11 and player["score"] > 21 :
            i = player["card"].index(card)
            player["card"][i] = 1
        
            
def hit(player):
    """Adds a card."""
    player['card'].append(random.choice(cards))
    Ace_value(player)

def view_current_score():
    """Print the current score to the user."""
    print(f"    Your cards: {user['card']}, current_score: {user['score']}")
    print(f"    Computer's first card: {computer['card'][0]}")

def end_game():
    """Print specific stament everytime the game ends."""
    print(f"    Your final hand: {user['card']}, final score: {user['score']}")
    print(f"    Computer's final hand: {computer['card']}, final score: {computer['score']}")

play = True
while play :
    re = input("Do you want to play a game of Blackjack? Type 'y' or 'n':").lower()
    if re == 'y' :
        clear()
        deal()
        print(logo)
        view_current_score()
        if user['score'] == 21 :
            hit(computer) 
            end_game()
            if computer["score"] == 21 :
                print("Draw.")
            else:
                print("Win with a Blackjack")
        else:
            another_card = True
            while another_card :
                ac = input("Type 'y' to get another card, type 'n' to pass:").lower()
                if ac == 'y' :
                    hit(user)
                    if user["score"] > 21 :
                        end_game()
                        print("You went over. You lose.")
                        exit()
                    elif user["score"] == 21 :
                        if computer["score"] == 21 :
                            end_game()
                            print("Draw.")
                            exit()
                        elif computer["score"] < 21 :
                            while computer["score"] < 21:
                                hit(computer)
                            if computer["score"] == 21 :
                                end_game()
                                print("Draw.")
                                exit()
                            else :
                                end_game()
                                print("You win!")
                                exit()
                        else:
                            end_game()
                            print("You win!")
                            exit()
                    else :
                        view_current_score()
                        result = input("Type 'y' to get another card, type 'n' to pass:").lower()
                else :
                    another_card =False
            if result == 'n' :
                if computer["score"] < 21 :
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
        


            



