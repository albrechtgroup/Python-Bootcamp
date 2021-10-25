# User input - built in python function
#   that promps the user and stores the 
#   result to a variable.
name = input("Enter your name here: ")

# Mileage Converter Exercise:
print("How many Kilometers did you cycle today?")
kms = input()
miles = float(kms)/1.60934
rounded_miles = round(miles, 2)
print(f"Your {kms}km ride is equal to {rounded_miles}miles ")

data = input("What is the Securitu Clearance?")
print("The Clearance password is " + data)

# Colt personally prefers the 'print statement'
print("What's your favorite color?")
data = input()
print("You said the color " + data)

# 'Psuedo code' = combination betw english
#     and computer language. (Below)

########################
# Conditional statements:
# Conditional logis using 'if' statements 
# represent different paths a program can 
# take based on some comparison of input
# * Psuedo Code Below *
# if some condition is True:
#   do something
# elif some other condition is True:
#   do something
# else: do something

if name == "Andrew Albrecht":
    print("Welcome Sir.")
elif name == "Mariya Milano":
    print("Welcome Maddam.")
else: 
    print("We're sorry, noone else is allowed on these premises.")

# Multiple 'elif'
color = input("What's your favorite color?")
if color == 'purple':
    print("Excellent choice!")
elif color == 'teal':
    print("Are you fucking serious?!")
elif color == 'seafoam':
    print("Get out of this building!")
else:
    print("You Monster!!")

# Truthiness & Falsiness:
x = 1
x is 1 # Output = True  Truthy
x is 0 # Output = False  Falsy

# Besides False conditional checks, other 
# things that are falsy are: empty objects, 
# empty strings, None and zero.

