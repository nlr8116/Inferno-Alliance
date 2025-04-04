#Iterating over dictionaries 
techie = {
    "proper_name": "tech XXII",
    "breed": "Bulldog",
    "Caretaker": "Dr.Tims",
    "weight": "heavy",
    "activity level": 0,
}

#iterating over keys
for k in techie:
    print(k)
    print(techie[k])

#iterating over keys and values
for i, k in techie.items():
    print(i, k)

#iterating over just values
for value in techie.values():
    print(value)

#iterating over just the keys again 
for key in techie.keys():
    print(key)
