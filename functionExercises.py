######################
# Function Exercises:

""" Write a function called 'product' that accepts two
    parameters and returns the product of the two 
    parameters(multiply them together) """
from math import prod

def product(a, b):
    return a*b
print(product(2, 2))



""" Write a function called 'return_day'. This function
    takes in one parameter(a num from 1-7) and returns
    the day of the week(1 is Sunday, 2 is Monday, etc.) 
    If the number is less than 1 or greater than 7, 
    the function should return 'None' """
# Hint: Store the days of the week in a list
# Here's a solution that uses what we've learned so far.
""" Keep track of the days in a list.
Check to make sure num isn't < 0 or > 6.
Return the corresponding day. Use days[num-1] because return_day(1) should return 0th item in list. """
def return_day(num):
    days = ["Sunday", "Monday", "Tuesday",
            "Wednesday", "Thursday", "Friday", "Saturday"]
    # Check to see if num valid
    if num > 0 and num <= len(days):
        # use num - 1 because lists start at 0
        return days[num-1]
    return None



""" Write a function called 'last_element'. This 
    function takes in one parameter(a list) and returns
    last value in the list. It should return None if
    empty. """
# First check to see if the list exists(if it has data in it).  If it does, return the - 1 item(last item).  Otherwise, return None.
def last_element(l):
    if l:
        return l[-1]
    return None



""" Write a function called 'number_compare'. This 
    function takes in two parameters(both numbers). 
    If the first is greater than the second, this
    function returns "First is greater". If the 2nd
    number is greater than first, the function returns
    "Second is greater" Otherwis the function returns
    "Numbers are equal" """
def number_compare(a, b):
    if a > b:
        return "First is greater"
    elif b > a:
        return "Second is greater"
    return "Numbers are equal"



""" Write a function called 'single_letter_count". 
    This func takes in two parameters(2 strings)
    The first param should be a word and the 2nd
    a letter. The func returns the num of times
    that letter appears in the word. The function 
    should be case-sensitive(input doesnt matter)
    If the letter is not found in the word, the 
    function returns zero """
# Hint: take advantage of count() method.
# In my solution, I use the built-in count()  to count the number of times letter  appears in string .  I also downcase both string and letter  to make it case-insensitive(you could also upcase both instead)
def single_letter_count(string, letter):
    return string.lower().count(letter.lower())



""" Write a function called 'multiple_letter_count'
    This function takes in one parameter(a string)
    and returns a dictionary with the keys being
    the letters and values being the count of letter
    """
# Hint: Use a dictionary comprehension and count()
# I used a dictionary comprehension. For each letter in the input string, I make the key the letter itself("a" for example), and the corresponding value is the result of running count() of that letter in the string.
def multiple_letter_count(string):
    return {letter: string.count(letter) for letter in string}



""" Write a function called 'list_manipulation'. This
    function should taek in four parameters(a list,
    command, location and value) """
# It's basically just a large if-elif-else statement:

def list_manipulation(collection, command, location, value=None):
    if(command == "remove" and location == "end"):
        return collection.pop()
    elif(command == "remove" and location == "beginning"):
        return collection.pop(0)
    elif(command == "add" and location == "beginning"):
        collection.insert(0, value)
        return collection
    elif(command == "add" and location == "end"):
        collection.append(value)
        return collection


""" Write a function called 'is_palindrome. A Palindrome
    is a word, phrase, number, or other sequence of
    characters which reads teh same backward or
    forward. This function should take in one parameter
    and returns True or False depending on whether
    it is a Palindrome. """
def is_palindrome(string):
    return string == string[::-1]



""" Writer a function called 'frequency'. This function
    accepts a list and a search_term(this will always
    be a primitive value) and returns the number of
    times the search_term appears in the list. """
def frequency(collection, searchTerm):
    return collection.count(searchTerm)



""" Write a function called 'multiply_even_numbers'. This
    function accepts a list of numbers and returns
    the product of all even numbers in the list. """
""" In my solution, I start with a variable called total.
Since we're working with multiplication, I start it off as 1.
Then I iterate through the list, checking if each num is cleanly divisible by 2
If it is , I multiply total by the number
At the end, after the loop finishes, I return total """
def multiply_even_numbers(lst):
    total = 1
    for val in lst:
        if val % 2 == 0:
            total = total * val
    return total



""" Write a function called 'capitalize'.This function
    accepts a string and returns the same string with
    the first letter capitalized. You may want to use
    slices to help you out. """
""" My solution works by:
Slicing the first character(up to index 1) and capitalizing it
Adding that to the rest of the string(from index 1 onward) """
def capitalize(string):
    return string[:1].upper() + string[1:]



""" Write a function called 'compact'. This function 
    accepts a list and  returns a list of values that
    are 'truthy' values, wihtout any of the falsey
    values. """
def compact(l):
    return [val for val in l if val]



""" Write a function called 'intersection'. This 
    function should accept two lists and return a
    list with the values that are in both input 
    lists. """
def intersection(l1, l2):
    in_common = []
    for val in l1:
        if val in l2:
            in_common.append(val)
    return in_common



""" Write a function called 'partition'. This func
    accepts a list and a callback funct(which you 
    can assume returns True or False). The function 
    should iterater over each element in the list and
    invoke the callback func at each iteration. """

""" "Traditional" Version:
Here's my solution that doesn't use a list comprehension:

I have two lists, to hold the true and false values
I loop through the list, calling fn with each value in the list
If the result is True, I append the value to the trues  list
Otherwise, I append the value to the falses  list
At the end I return a list that contains both the trues and falses  lists """

def partition(lst, fn):
    trues = []
    falses = []
    for val in lst:
        if fn(val):
            trues.append(val)
        else:
            falses.append(val)
    return [trues, falses]


