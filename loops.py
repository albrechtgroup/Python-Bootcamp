######################
# 'for' loops:
for count in range(7):
    print(count+1)

for number in range(1, 11):
    print(number)

for letter in "coffee":
    print(letter)

# range()
  
# range(7) gives you integers 0-6
# range(1, 8) will give you integers 1-7
# range(1, 10, 2) will give you odds from 1-10
# range(7, 0, -1) will give you integers from 7-1


# Repeater Exercise:
times = input("How many times do I have to tell you?!? ")
times = int(times)

for time in range(times):
    print("CLEAN UP YOUR ROOM!!!")
    if time >= 4:
        print("Do you even listen to me anymore?")
        break


# Modulo example:
# num % 2 == 0  EVEN-when num is divided by two,
#               the remainder should equal zero.
# num % 2 == 1  ODD- 

# Unlucky Numbers Exercise:
# for num in range(1, 21):
#     if num == 4 or num == 13:
#         print(f"{num} is UNLUCKY!!!")
#     elif num % 2 == 0:
#         print(f"{num} is even")
#     else:
#         print(f"{num} is odd")
    
# OR: shorter, cleaner version:
for num in range(1, 21):
    if num == 4 or num == 13:
        state = "unlucky"
    elif num % 2 == 0:
        state = "even"
    else:
        state = "odd"
    print(f"{num} is {state}")
    

########################
# 'while' loops:
# they continue to execute while a certain condition
# is truthy, and will end when they become falsy.

count = 1
while count <= 10:
    print(count)
    count = count + 1
# Output = 1,2,3,4,5,6,7,8,9,10

student_list = ["Mary", "John", "Mike", "Alice"]
index = 0
while index < len(student_list):
    print(student_list[index])
    index += 1

msg = input("What's the secret password?")
while msg != "bananas":
    print("WRONG!")
    msg = input("What's the secret password?")
print("CORRECT!!!")

# Emoji art exercise:
# with 'for' loop
for num in range(1, 11):
    print("$" * num)

# with 'while' loop
times = 1
while times < 11:
    print("$" * times)
    times += 1

# Stop copying me exercise:
# repeat everything until the user says 'stop copying me'
msg = input("Say Something: ")

while msg != "stop copying me":
    print(msg)
    msg = input()

# the 'break' keyword:
# Gives us the ability to exit out of loops
# whenever we want.
for x in range(1, 101):
    print(x)
    if x == 3:
        break
