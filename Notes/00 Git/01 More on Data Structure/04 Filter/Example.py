#The filter() function/class
# Used to filter out items in a list 

# the filter function takes two arhuments 
# the first argument is a function that returns a boolean, 
# the second argument is a list (or a iterable)

# the filter function returns a smaller list of items 
#(most-likely), returns a filter object that we convert to a list

names =['aaron','Aayusha',"Ashish",'John','joseph','jacob',"william",'nico']

def starts_with_a(name:str) -> bool:
    """"""
    if name[0] == 'A':
        return True
    else:
        return False
    
a_names = []
for name in names:
    if starts_with_a(name):
        a_names.append(name)

print(a_names)

#Filtering with filter function
a_names = list(filter(starts_with_a, names))

print(a_names)

#Filtering with filter function and lambda function
a_names = list(filter(lambda name: name[0] == "A", names))
print(a_names)

#Another example
numbers = [1,2,4,5,6,7,754,2]
fit_nums = list(filter(lambda num: num%2 == 0 , numbers))
print(fit_nums)

