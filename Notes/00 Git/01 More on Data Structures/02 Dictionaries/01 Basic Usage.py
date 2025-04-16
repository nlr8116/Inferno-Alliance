# A dictionary is a set of key:value pairs
josh = {
    # key       :  value
    "first_name": "Josh", 
    "last_name": "Coriell", 
    "height": 1
}

# Accessing Values in the dictionary
josh["first_name"]      # keys are used to access values
print(josh["first_name"])
first_name = josh["first_name"]
print(first_name)

# accessing a key that doesn't exist
#print(josh["major"])  # uncomment for an error
major = josh.get("major")   # .get() on a dictionary will not throw an error
major = josh.get("major", "this is the default")   


# updating or setting new values in the dictionary
josh["major"] = "Computer Science"
josh["major"] = "Forestry"
josh["major"] = "Architecture"

print(josh.get("major"))

print(josh)

