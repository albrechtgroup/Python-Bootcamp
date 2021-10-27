import random

#####################
# Bouncer Exercise:
age = input("How old are you: ")
if age:
    age = int(age)
    if age >= 18 and age < 21:
        print("You may enter, but need a wristband.")
    elif age >= 21:
        print("You are good to go, and Cheers!")
    else:
        print("You are too young, get the Hell outta here, Damn kids!!")
else:
    print("Please enter an age. Dumb shit.")


#######################
# Rock, Paper, Scissors
print("Rock...")
print("Paper...")
print("Scissors")

player1 = input("Player 1, make your selection.")
player2 = input("Player 2, make your selection.")

if player1 == player2:
    print("Its a TIE!")
elif player1 == "rock":
    if player2 == "scissors":
        print("Player1 Wins!!")
    elif player2 == "paper":
        print("Player2 wins!")
elif player1 == "paper":
    if player2 == "rock":
        print("Player1 wins!")
    elif player2 == "scissors":
        print("Player2 wins!")
elif player1 == "scissors":
    if player2 == "rock":
        print("Player2 wins!")
    elif player2 == "paper":
        print("Player1 wins!")      
else:
    print("Something went wrong.")

# Creating a random number
num = random.randint(1, 100)
print(num)

