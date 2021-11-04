# Dictionaries {}: 
""" Consist of key: value pairs
    We use keys: to desciribe our data and the values 
    represent the data. 
    Keys are almost always numbers or strings """
instructor = {
    "name": "Colt",
    "ownsCat": True,
    "courses": 7,
    "favoriteLanguage": "Python",
    "isHalarious": False,
    73: "My favorite number!"
}

cat = {"name": "Matrix", "age": 3, "isCute": True}
print(cat)

# list of dictionaries
shoppingCart = [{"name": "Scooter", "price": 500}, {2}]

# Another way of creating a dictionary
# dict() function:
anotherDictionary = dict(key = 'value')
print(anotherDictionary)
# Output = {'key': 'value'}

# Example:
myCat = dict(name = "Matrix", age = 3)
print(myCat)
# Output = {'name': 'Matrix', 'age': 3}

# Accessing value out of dictionaries:
instructor["name"]

cat["name"]
print(cat["name"])

# Iterating dictionaries:
instructor = {
    "name": "Colt",
    "ownsCat": True,
    "courses": 7,
    "favoriteLanguage": "Python",
    "isHalarious": False,
    73: "My favorite number!"
}

# iterating/accessing BOTH key and value: .items()
for k,v in instructor.items():
    print(k,v)
    print(f"Key is {k} and Value is {v}")

# iterating over 'values': .values()
for val in instructor.values():
    print(val)

# iterating over 'keys': .keys()
for val in instructor.keys():
    print(val)

instructor = {
    "name": "Colt",
    "ownsCat": True,
    "courses": 7,
    "favoriteLanguage": "Python",
    "isHalarious": False,
    73: "My favorite number!"
}
7 in instructor.values()
# Output = True
"name" in instructor.values()
# Output = False
"name" in instructor.keys()
# Output = True


##############################
# Dictiaonary Methods:












##############################
# Cher Hin CHong:

#   dictionary = {}
# Do not have index numbers, no order
# key: value pairs, like objects in JS
city_weather = {"Singapore": 30, "Paris": 15, "Sydney": 19, "Tokyo": 15}
city_weather["Brooklyn"] = 77
# to add to dictionary or change exist value
# Output = {"Singapore": 30, "Paris": 15, "Sydney": 19, "Tokyo": 15, "Brooklyn": 77}
del city_weather["Singapore"]
# Output = {"Parris": 15, etc} minus Singapore
print(city_weather["Brooklyn"])
# Output = 77

# 'is'
num_1 = 13
print(type(num_1) is int)
# Output = True
num_2 = 11.3
print(type(num_2) is float)
# Output = True

# 'is not'
print(type(num_2) is not str)
# Output = True

# Membership Operators:
# Use to check if a value is found within a
# sequence


# 'not in'
print(text_2 not in text_1)
# Output = False, Hello is 'in' Hello World
print(text_3 in text_1)
# Output = False, lowercase hello is Not in






