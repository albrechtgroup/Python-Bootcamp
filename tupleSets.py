######################
# Tuples ():
# An ordered collection or grouping of items.
# like a list but uses ()
# BUT, tuples are Immutable = Cannot be changed.

numbers = (1, 2, 3, 4)

# Why use a Tuple??
# They are faster than lists
# It makes your code safer
# Can use them as Valid keys in a dictionary
# Common to use for info that NEVER changes, below..
months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

# Create them using () or the tuple function. 
# Access them just like lists.
firstTuple = (1, 2, 3, 3, 3)
firstTuple[1]
# Output = 2
firstTuple[2]
# Output = 3
firstTuple[-1]
# Output = 3
secondTuple = (3, 4, 7)
secondTuple[0]
# Output = 3
secondTuple[-1]
# Output = 7

# Tuples can be used as keys in a dictionaries:
locations = {
    (35.68595, 39.6917): "Tokyo Office",
    (40.7128, 74.0060): "New York Office",
    (37.7749, 122.4194): "Los Angelas Office"
}
print(locations)
# Some dictionary methods like .items() return tuples
cat = {"name": "Biscuit", "age": 2.5, "favorite_toy": "my chapstick"}
cat.items()
# Output = dict_items([('name', 'biscuit'), ('age', 2.5), ('favorite_toy', 'my chapstick')])

# Tuple looping and methods:
# We can use a 'for' loop to iterate over a tuple 
# just like a list.
names = ('Cole', 'Blue', 'Rusty', 'Lassie')
for name in names:
    print(name)

for month in months:
    print(month)

# Only 2 Methods:
# .count() returns the number of times a value 
# appears in a tuple.
x = (1,2,3,3,3)
x.count(1) # Output = 1
x.count(3) # Output = 3

# .index() returns the index at which a value is 
# found in a tuple.
t = (1,2,3,3,3)
t.index(1) # Output = 0
## Output = ValueError
t.index(3) # Output = 2 - only the first matching 
           #              index is returned.

# nested tuples:
nums = (1,2,3,(4,5),6,7)
print(nums)

print(nums[3])

##########################
# Sets {}:
# Elements in sets are Not ordered.
# Cannot access items in a set by index.
# Similar rules to dictionaries does Not use 
# key: value pairs.
# Cannot be changed, must be removed, then
# added.
""" Sets can be useful if you need to keep track of 
    a collection of elements, but dont care about 
    ordering, key or values, and no duplicates  """

# Sets cannot have duplicate values.
s = set({1, 2, 3, 4, 5, 5, 5})
# Output = {1, 2, 3, 4, 5}

# Creating a new set:
s = set({1, 4, 5})
# Creates a set with the same values as above:
s = {1, 4, 5}

4 in s # Output = True
8 in s # Output = False

# Accesing values in a set:
numbers = {1, 2, 3, 4,}
for number in numbers:
    print(number)

# Common-Use case for sets:
cities = ["New York City", "Tokyo", "Boulder", "Los Angelas", "Boulder", "Shanghai", "Satiago", "Tokyo", "Florence"]
print(set(cities))

# Set Methods and Set Math:
# .add() method adds elements to a set.
s = set([1, 2, 3])
s.add(4)
print(s)
# Output = {1, 2, 3, 4}
s.add(4) 
# Outoput = Same
# It the element in the set already exists, the 
# value does Not change.

# .remove() method to remove from set
set1 = {1,2,3,4,5,6,7}
set1.remove(3)
print(set1)

# .copy Creates a copy of the set:
s = set([1,2,3])
another_s = s.copy()
print(another_s)

another_s is s  # Output = False. A copy, not same

# .clear() Removes ALL the contents in a set:

# Set Math: 
math_students= {"Matthew", "Helen", "Prashant", "James", "Aparna"}
biology_students = {"Jane", "Matthew", "Charlotte", "Mesut", "Oliver", "James"}

# Set Union:
# tells me how many students Total
math_students | biology_students
# Output = lists combined with no duplicates of names

# Set Intersections:
# Which of these students are in Both classes
math_students & biology_students
# Output = {'James', 'Matthew'}



