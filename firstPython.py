print("====================")
# "Hello Mr. Albrecht"
print("'Hello Mr. Albrecht'")

# Mathmatical Order of Operations:
# p - Parnthesis
# e - Exponents
# m - Multiplication
# d - Division
# a - Addition
# s - Subtraction

print(1/3) # *division will always return a 
           #  float
print(60+9)

student_list = ["Mary", "John", "Mike", "Alice"]
index = 0
while index < len(student_list):
    print(student_list[index])
    index += 1

# GitBash is running this code!! Why??

###################
# Variables in Python:
python_is_awesome = 100
python_var = python_is_awesome
print(python_var)

all, at, once, variable_assign = 5, 10, 15, "All at once Variable assignment"
print(all)
print(at)
print(once)
print(variable_assign)

####################
# Python Naming Conventions for Variables:

# *Most Python develpers use underscore
#    'snake_case' instead of 'camelCase'.. 
# Most variable are in lowercase, with some
#    exceptions like 'constants' -which dont
#    change.
# CAPITAL_SNAKE_CASE usually refers to constants
# UpperCamelCase usually refers to a class.
# Variable that start and end w/ 2 underscores
#    called "dunder" (double underscore),
#    are supposed to be private and left alonte
#   __no_touchy__

#####################
# Data Types:

# Dynamic Typing:
# Python can assign variable to diff types.
i_am_a_string = "hello world"
i_am_a_string = 73
i_am_a_string = True

awesomeness = True
print(awesomeness)

# Output = True
awesomeness = None
print(awesomeness)
# Output = None
# None keyword is similar to null is JS
# None is a 'NoneType' only one of its kind
name = "Daisy"
age = 33
child = None

# Strings
# Escape characters or "Sequences"

# \n  creates a new line
new_line = "hello \n world"
print(new_line)


new_line = "hi\nthere"
print(new_line)

# Concatenation = adding strings together
str_one = "best"
str_two = "ass"
str_three = str_one + " " + str_two
print(str_three)


