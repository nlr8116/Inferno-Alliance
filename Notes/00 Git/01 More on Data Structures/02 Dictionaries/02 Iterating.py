# Iterating over dictionaries

techie = {
    "proper_name": "Tech XXII",
    "breed": "bulldog",
    "caretaker": "Dr. Tims",
    "height": 1,
    "weight": "heavy",
    "activity level": 0,
}

# iterating over keys
for key in techie:
    print(key)
    print(techie[key])
    
# iterating over keys and values
for key, value in techie.items():
    print(key, value)
    
# iterating over just the values
for value in techie.values():
    print(value)
    
# iterating over just the keys again
for key in techie.keys():
    print(key)