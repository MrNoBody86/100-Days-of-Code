import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
RPS = [rock , paper, scissors]

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

if player >=3 or player < 0 :
    print("You typed an invalid number,you lose!")
else:
    print(RPS[player])

    computer = random.randint(0,2)

    print(f"Computer chose: \n{RPS[computer]}\n")

    if player == 0 and computer == 2:
        print("You win!")
    elif computer == 2 and player == 0:
        print("You lose")
    elif player < computer :
        print("You lose")
    elif player > computer :
        print("You win!")
    elif player == computer :
        print("It's a draw")

# if player == 0 :
#     if computer == 0:
#         print("It's a draw.")
#     elif computer == 1 :
#         print("You lose.")
#     else :
#         print("You win.")
# elif player == 1:
#     if computer == 0:
#         print("You win.")
#     elif computer == 1 :
#         print("It's a draw.")
#     else :
#         print("You lose.")
# elif player == 2:
#     if computer == 0:
#         print("You lose.")
#     elif computer == 1 :
#         print("You win.")
#     else :
#         print("It's a draw.")
# else :
#     print("Wrong choice.")