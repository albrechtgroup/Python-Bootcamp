############################
# lists = [], Very similar to arrays in JS
tasks = ["Install Python 3", "Learn Python", "Take a break."]
print(tasks)

fruits = ["apples", "oranges", "strawberries", "pears"]
print(fruits[2])
# Output = strawberries
fruits[3] = "grapes"
print(fruits)
# re-assigns pears to  equal grapes in the list

# range() will list the range of values in ()
# range(start,stop,step)
tasks = list(range(1, 7))
print(tasks)

# Accessing values using 'for' loop:
numbers = [1, 2, 3, 4, 5, 6, 7]
for number in numbers:
    print(number)

colors = ["purple", "blue", "green", True, 7.37]
for color in colors:
    print(color)

# Accessing values using 'while' loop:
numbers = [1, 2, 3, 4, 5]
i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1

colors = ["purple", "blue", "green", True, 7.37]
index = 0
while index < len(colors):
    print(colors[index])
    index += 1
###########################
# List Itteration Exercise:
sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
# Define your code below:
result = ''
for s in sounds:
    result += s.upper()

result = ''
for s in sounds:
    result += s
result = result.upper()

print(result)

################
# List Methods:

fruits = ["apples", "oranges", "strawberries", "pears"]
# .append() will add to the End of list
fruits.append("pineapple")
# Output = fruits = ["apples", "oranges", "strawberries", "pears", "pineapple"]

# del() well, it deletes from the list at index
del fruits[3]
print(fruits)
# Output = list with index 3 deleted

# .insert() will insert into the list at
# the given index
fruits.insert(3, "insert me at index 3")
print(fruits)

scores = [67, 93, 77, 84, 87]
scores.insert(1, 81)
# Output = adds the score 81 to posit 1 in the list
scores.insert(-1, 91)
# Output = adds the score 91 to the 2nd to last position
print(scores)
# Output = [67, 81, 93, 77, 84, 87] 

numbers = [1, 2, 3, 4]
# extend() will add All values passed in to end of
# list.
numbers.extend([5, 6, 7, 8, 9])
print(numbers)
# Ouput = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# len() tells us how many values in the list
print(len(numbers))

# .clear() will remove ALL items from the list
first_list = [1, 2, 3, 4]
first_list.clear()
print(first_list)
# Output = [] empty list

# .pop() will remove the item at the given posit in
# the list, and return it.
# If no index is specified, removes and returns the
# last item in the list
first_list = [1, 2, 3, 4]
first_list.pop()
# Output = 4
first_list.pop(1) 
# Output = 2
print(first_list)
# Output = [1, 3]

amazonList = ["scooter", "speakers", "sexy", "pepper"]
purchased = amazonList.pop()
print(purchased)
# Output = pepper
print(amazonList)
# Output = list without "pepper"

# .remove() will remove the item given in ()
deletedItem = amazonList.remove("sexy")
print(amazonList)
# Output = list without "sexy"

# .index() returns the index of (x) in list
amazonList.index("speakers")

# .count() returns the number of times (x) in list
text = "Count the number of u's in me."
print(text.count("u"))
# Output = 3

# .reverse() will reverse the elements of list
# (in place). Will update/change the list
first_list = [1, 2, 3, 4]
first_list.reverse()
print(first_list)
# Output = [4, 3, 2, 1]

# .sort() sorts the items of list (in place) Ascending
another_list = [7, 3, 13, 1]
another_list.sort()
print(another_list)
# Output = [1, 3, 7, 13] 

names = ["Mariya", "Jackie", "Andy", "Dana"]
names.sort()
print(names)
# Output = names in order acending A-Z
# ["Andy", "Dana", "Jackie", "Mariya"]

# .join() will join list items into a string
words = ["Coding", "is", "fun!"]
" ".join(words)
# Output = "Coding is fun!"

man = ["Mr", "Albrecht"]
". ".join(man)

# .split() will split a string into a list

#######################
# List Methods Exercise:
# Create a list called instructors
instructors = []

# Add the following strings to the instructors list
# "Colt"
# "Blue"
# "Lisa"
instructors.extend(["Colt", "Blue", "Lisa"])

# Remove the last value in the list
instructors.pop()

# Remove the first value in the list
instructors.pop(0)

# Add the string "Done" to the beginning of the list
instructors.insert(0, 'Done')

###################
# Slices make new lists using slices of old list
# some_list[start:end:step]

# Starting index:
first_list = [1, 2, 3, 4]
first_list[1:]
# Output = [2, 3, 4]
first_list[3:]
# Output = [4]

first_list[-1:]
# Output = [4]
first_list[-3:]
# Output = [2, 3, 4]

# Ending index: exclusive
second_list = [1, 2, 3, 4]
second_list[:2]
# Output = [1, 2]
second_list[:4]
# Output = [1, 2, 3, 4]
second_list[1:3]
# Output = [2, 3]

second_list[:-1]
# Output = [1, 2, 3]
second_list[1:-1]
# Output = [2, 3]

# 'step' in python is basically the number to count
#  at a time. Same as step with range()


# Hello Andy
text = "Hello Andy"
print(text[:5])
# Output = Hello
print(text[:4])
# Output = Hell
print(text[-4:])
# Output = Andy, -Negative numbers start
# string from the Right going Left
# starting at -1, instead of 0

name = "Hello, My name is Andy"
print(name[18:22])
# Output = Andy
# Starting index is Inclusive,
# while the ending index is Exclusive.
print(name[6:])
# Output = My name is Andy

# Tricks with Slices: 
# Reversing lists/strings
string = "This is fun!"
string[::-1]

# Modifying portions of a list
numbers = [1, 2, 3, 4, 5]
numbers[1:3] = ['a', 'b', 'c']
print(numbers)
# Output = [1, a, b, c, 4, 5]

# Swapping values:
names = ["James", "Michelle"]
names[0], names[1] = names[1], names[0]
print(names)
# Output = ["Michelle", "James"]




