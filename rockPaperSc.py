import random
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

player = input("Player, make your selection.").lower()
rand_num = random.randint(0, 2)
if rand_num == 0:
    computer = "rock"
elif rand_num == 1:
    computer = "paper"
else:
    computer = "scissors"
print(f"Computer selects {computer}")

if player == computer:
    print("Its a TIE!")
elif player == "rock":
    if computer == "scissors":
        print("You Win!!!")
    elif computer == "paper":
        print("Computer wins!")
elif player == "paper":
    if computer == "rock":
        print("You Win!!!")
    elif computer == "scissors":
        print("Computer wins!")
elif player == "scissors":
    if computer == "rock":
        print("Computer wins!")
    elif computer == "paper":
        print("You Win!!!")
else:
    print("Please Enter Valid Object.")

# Creating a random number
num = random.randint(1, 100)
print(num)
