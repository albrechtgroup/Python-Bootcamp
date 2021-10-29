import random

randomNumber = random.randint(1, 10) 
guess = None

while guess != randomNumber:
    guess = input("Pick a number from 1 to 10: ")
    guess = int(guess)
    if guess < randomNumber:
        print("Too LOW.")
    elif guess > randomNumber:
        print("Too HIGH.")
    else:
        print("You just won 1 MILLION DOLLARS!*!*!*")
print(randomNumber)
# handle user guesses
#    if they guess correct, tell them they won,
#    otherwise tell them they are too high or low


# Another Version with ending:
randomNumber = random.randint(1, 10)

while True:
    guess = input("Pick a number from 1 to 10: ")
    guess = int(guess)
    if guess < randomNumber:
        print("Too LOW.")
    elif guess > randomNumber:
        print("Too HIGH.")
    else:
        print("You just Won 3 MILLION DOLLARS *!*!*!*")
        playAgain = input("Would you like to play again? (y/n) ")
        if playAgain == "y":
            guess = input("Pick a number from 1 to 10: ")
            guess = None
        else:
            print("Thank You for playing.")
            break
