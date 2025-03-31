# a dictionary is a sey of key: value pairs 

nico = {
    #Key    :   #Item
    "first name": "Nico", 
    "Last Name": "Relle", 
    "Height": "6'0"}

#Accessing Values in the dictionary 
print(nico["Height"]) # Keys are used to access values 

#accessing a key that doesn't exist
#print(nico["major"]) #Will run an error 
print(nico.get("major"))# Will return none type if it has no value 
print(nico.get("major", "this is the default")) # also add a default if no value is there 

#updating or setting new value in the dictionary 
nico["major"] = "Computer Science"
print(nico.get("major"))
print(nico)
