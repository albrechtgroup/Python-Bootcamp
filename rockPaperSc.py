import random
from typing import ChainMap
#######################
# Rock, Paper, Scissors VI

# print("Rock...")
# print("Paper...")
# print("Scissors")

# player1 = input("Player 1, make your selection.")
# player2 = input("Player 2, make your selection.")

# if player1 == player2:
#     print("Its a TIE!")
# elif player1 == "rock":
#     if player2 == "scissors":
#         print("Player1 Wins!!")
#     elif player2 == "paper":
#         print("Player2 wins!")
# elif player1 == "paper":
#     if player2 == "rock":
#         print("Player1 wins!")
#     elif player2 == "scissors":
#         print("Player2 wins!")
# elif player1 == "scissors":
#     if player2 == "rock":
#         print("Player2 wins!")
#     elif player2 == "paper":
#         print("Player1 wins!")
# else:
#     print("Something went wrong.")

# # Creating a random number
# num = random.randint(1, 100)
# print(num)

######################
# Version II
playerWins = 0
computerWins = 0
winningScore = 3

while playerWins < winningScore and computerWins < winningScore:
    print(f"Player Score: {playerWins} Computer Score: {computerWins}")
    print("*--== Rock ==--*")
    print("*--== Paper ==--*")
    print("*--== Scissors ==--*")

    player = input("(Enter your selection): ").lower()
    if player == "quit" or player == "q":
        break
    rand_num = random.randint(0, 2)
    if rand_num == 0:
        computer = "rock"
    elif rand_num == 1:
        computer = "paper"
    else:
        computer = "scissors"
    print(f"Computer selects: {computer}")

    if player == computer:
        print("Its a TIE!")
    elif player == "rock":
        if computer == "scissors":
            print("You Win!!!")
            playerWins += 1
        elif computer == "paper":
            print("Computer wins!")
            computerWins += 1
    elif player == "paper":
        if computer == "rock":
            print("You Win!!!")
            playerWins += 1
        elif computer == "scissors":
            print("Computer wins!")
            computerWins += 1
    elif player == "scissors":
        if computer == "rock":
            print("Computer wins!")
            computerWins += 1
        elif computer == "paper":
            print("You Win!!!")
            playerWins += 1
    else:
        print("Please Enter Valid Object.")
print(
    f"FINAL SCORES === Player: {playerWins} Computer: {computerWins}")
