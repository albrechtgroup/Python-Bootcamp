###################################
# *args:
# A special operator that we can pass to functions.
# Gathers remaining arguements as a tuple.
def sum_all_nums(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_all_nums(3,7,11,13,23,33))
print(sum_all_nums(3,7))

def ensure_correct_info(*args):
    if "Colt" in args and "Steele" in args:
        return "Welcome back Colt!!"
    
    return "Not sure who you are."

print(ensure_correct_info()) # Not sure who you are.
print(ensure_correct_info(3, True, "Steele", "Colt"))
# Output = Welcome back Colt!!

# 'args' is a common name, can be anything you want.
def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num
    return total


print(sum_all_nums(3, 7, 11, 13, 23, 33))
print(sum_all_nums(3, 7))


def contains_purple(*args):
    if "purple" in args:
        return True

    return False

########################################
# **kwargs: 'keyword' args
# A special operator that we can pass to functions.
# Gathers remaining 'keyword' arguements as a 
# dictionary instead of a tuple.
def fav_colors(**kwargs):
    print(kwargs)

fav_colors(colt="purple", ruby="red", ethel="teal")
# Output = {'colt': 'purple', 'ruby': 'red', 'ethel': 'teal'}

# Parameter Ordering:
""" 1. parameters 
    2. *args 
    3. default parameters
    4. **kwargs  """

# Using * as an Arguement: Arguement Unpacking:
# We can use * as an arguement to a function
# to 'unpack' values.
def sum_all_value(*args):
    print(args)
    total = 0
    for num in args:
        total += num
    print(total)

nums = (1,2,3,4,5,6,7)
print(sum_all_nums(*nums))
# Output = 28

