################################
# list Comprehension:
nums = [1, 2, 3]
[x*10 for x in nums]
# Output = [10, 20, 30]

numbers = [1, 2, 3, 4, 5]
doubleNumbers = [num * 2 for num in numbers]
print(doubleNumbers)
# Output = [2, 4, 6, 8, 10]

name = 'Andy'
[char.upper() for char in name]
# Output = [A, N, D, Y]

friends = ['ashley', 'matt', 'micheal']
[friend[0].upper() for friend in friends]
# Output = ['Ashley', 'Matt', 'Micheal']

[num*10 for num in range(1, 6)]
# Output = [10, 20, 30, 40, 50]

# converting data types. Numbers to strings:
numbers = [1, 2, 3, 4, 5]
stringList = [str(num) for num in numbers]
print(stringList)

# list Comprehension with Conditional logic:
numbers = [1, 2, 3, 4, 5, 6]
evens = [num for num in numbers if num % 2 == 0]
odds = [num for num in numbers if num % 2 != 0]
print(odds)

# Nested lists:
nestedList = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
nestedList[0][1]
# Output = 2
nestedList[1][-1]
# Output = 6

nestedList = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for l in nestedList:
    for val in l:
        print(val)
# Output = 1 thru 9 each on seperate lines

# Nested list Comprehension:
nestedList = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
[[print(val) for val in l] for l in nestedList]
# Output = 1 thru 9 each on seperate lines. Same above

board = [[num for num in range(1, 4)] for val in range(1, 4)]
print(board)

toe = [["X" if num % 2 != 0 else "O" for num in range(1, 4)] for val in range(1, 4)]
print(toe)


################################
# Dictionary Comprehension:
# Syntax  {__:__for __in__}

numbers = dict(first=1, second=2, third=3)
squared_numbers = {key: value ** 2 for key,value in numbers.items()}
print(squared_numbers)

# Conditional logic with dictionaries:
num_list = [1,2,3,4]
{ num:("even" if num % 2 ==0 else "odd") for num in num_list }
# Output in 'Powershell' = 
# {1: 'odd', 2: 'even', 3: 'odd', 4: 'even'}


#################################
# Set Comprehension:
{x**2 for x in range(10)}
# Output = {0, 1, 64, 4, 36, 9, 16, 49, 81, 25}
# The numbers 0-9 squared..

# This creates a dictianary version of above
{x:x**2 for x in range(10)}
# Output = 
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}


