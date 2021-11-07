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

# .clear() will clear the entire
instructor.clear()

# .copy() will copy the entire dictionary
d = dict(a=1,b=2,c=3)
c = d.copy()
print(c)
# Output = {'a': 1, 'b': 2, 'c': 3}
c is d
# Output = False

# .fromkeys Creates key-value pairs from comma 
#  seperated values.
# Usually used to generater default values.
{}.fromkeys("a", "b")
# Output = {'a': 'b'}
{}.fromkeys(["email"], 'unknown')
# Output = {'email': 'unknown'}
{}.fromkeys("a", [1,2,3,4,5])
# Output = {'a': [1, 2, 3, 4, 5]}
kv3 = {}.fromkeys("a", [1, 2, 3, 4, 5])
print(kv3)
# Output = {'a': [1, 2, 3, 4, 5]}

# .get() 
# Retreives a key in an object and returns 'None'
# instead of 'KeyError' if key does not exist.
d = dict(a=1, b=2, c=3)
d['a']
# Output = 1  
d['b']
# Output = 2

# .pop()
# Different in .pop for lists in that we must provide
# the 'key' of what we want to remove.
d.pop('b')
# Output = 2  (the value of 'b')
print(d)
# Output = {'a': 1, 'c': 3}
 
# popitem() Removes a random key in a dictionary.

# .update() Updates keys and values in a dictionary
#  with another set of key/value pairs

###############################
# Spotify Playlist:
playlist = {
    'title': 'Patagonia bus', 
    'author': 'Colt Steele', 
    'songs': [
        {'title': 'song1', 'artist': ['That Ass'], 'duration': 3.7}, 
        {'title': 'song2', 'artist': ['Waist', 'DjCat'], 'duration': 2.5},
        {'title': 'song3', 'artist': ['Beetlejuice'], 'duration': 5.25}
    ]
}
print(playlist)

playLength = 0
for song in playlist['songs']:
    playLength += song['duration']
print(playLength)

# print(song['duration'])
