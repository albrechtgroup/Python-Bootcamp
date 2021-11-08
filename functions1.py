# Defining Functions:
from math import sin
from typing import get_origin


def say_hi():
    print('Hi!')

say_hi()

def sing_happy_birthday():
    print("Happy Birthday To You")
    print("Happy Birthday To You")
    print("Happy Birthday Dear YOU")
    print("Happy Birthday To You")

sing_happy_birthday()

# The Majical 'return' keyword:
# 'return' exits the function
# Outputs whatever value is placed after 'return'
# Pops the function off of the call stack.

def get_job():
    return 'Your Hired!!!'
    print("I am After the 'return'.")

goal = get_job()
print(goal)

# Coin flip function Exercise:
from random import random

def flip_coin():
    r = random()
    if r > 0.5:
        return "Heads"
    else: 
        return "Tails"

print(flip_coin())

# Parameters:
def square(num):
    return num * num
print(square(3)) # Output = 9
print(square(99)) # Output = 9801


def sing_happy_birthday(name):
    print("Happy Birthday To You")
    print("Happy Birthday To You")
    print(f"Happy Birthday Dear {name}")
    print("Happy Birthday To You")


sing_happy_birthday("Chuck")
sing_happy_birthday("Andy")

# Multiple Parameters:
def add(a,b):
    return a+b
print(add(234, 3473)) # Output = 3707

def multiply(first, second):
    return first * second

print(multiply(3, 11)) # Output = 33

# Naming your Parameters:
# Not Great
def print_full_name(string1, string2):
    return(f"Your full name is {string1} {string2}")
# Better naming
def print_full_name(first_name, last_name):
    return(f"Your full name is {first_name} {last_name}")

print(print_full_name("Andy", "Albrecht"))

# Parameters VS. Arguements:
""" A parameter is a variable in the method Definition
    When the method is called, the Arguements are the 
    data you pass into the method's parameters """
# Parameters = (first_name, last_name)
# Arguements = ("Andy", "Albrecht")

# Adding odd numbers together:
def sum_odd_numbers(numbers):
    total = 0
    for num in numbers:
        if num % 2 != 0:
            total += num
    return total

print(sum_odd_numbers([1,2,3,4,5,6,7])) # Output= 16

# Default Parameters:
def exponent(num, power=2):
    return num ** power

print(exponent(2,3)) # Output = 8
print(exponent(3)) # Output = 9
print(exponent(7)) # Output = 49

# For example .pop() by default will remove the 
# last element in a thing.

def add(a=10, b=20):
    return a+b

add() # Output = 30
add(37, 73) # Output = 110
print(add(37, 73))

# Why have Default Parameters?
# Allows you to be more defensive
# Avoids errors with incorrect parameters
# More Readable examples
 
def add(a,b):
    return a+b

def subtract(a,b):
    return a-b
# Below adds a Default function as one parameter:
def math(a,b, fn=add):
    return a-b

math(2, 2) # Output = 4 (No params so default of add)
math(2,2, subtract) # Output = 0

# Keyword Arguements:
def full_name(first, last):
    return f"Your name is {first} {last}"
# Order does Not matter below
print(full_name("Andy", "Albert"))


# Scope!
# Variable created in functions are scoped in that
# function.
instructor1= "DeeDee"
def say_hello():
    instructor2 = 'Colt'
    return f"Hello {instructor2}"
print(say_hello()) # Output = 'Hello Colt'
print(instructor1) # Output = 'DeeDee'  (Global)
# print(instructor2) # Output = NameError 

# Global scope:
# Variables defined Outside of the function
# Every variable in out examples up to now..

# nonlocal:
# Lets us modify a parent's variables in a 'child'
# (aka) nested function.
def outer():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner()
# Documenting Functions ( not comments)
def say_hello():
    """ A simple function that returns the string 'Hello' """
    return "Hello!"

say_hello.__doc__ # Output the 'comments' thing from 
                  # above function.



