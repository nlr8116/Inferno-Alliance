# The filter() function
# Used to filter out items in a list

# The filter() function takes 2 arguments
# The first argument is a function that return a Boolean
# The second argument is a list (or really an iterable)

# The filter() function returns a 
# (most-likely) smaller list of items.
# Technically it returns a filter object 
# that we convert to a list.

names = [
    'Aaron', 'Aayusha', 'Ashish', 
    'Josh', 'Joseph', 'Jadon', 
    'Jacob', 'William', 'William'
]

def starts_with_a(name):
    """Returns True if `name` starts with an `A`"""
    if name[0] == 'A':
        return True 
    else:
        return False 
    
# Filtering with a for loop (the typical way)
a_names = []
for name in names:
    if starts_with_a(name):
        a_names.append(name)
        
print(a_names)

# Filtering with the filter() function
a_names = list(filter(starts_with_a, names))
print(a_names)

# Filtering with filter() function and lambda function
a_names = list(filter(     lambda name: name[0] == 'A'     ,    names    ))
print(a_names)


# Another example
numbers = [1, 2, 3, 5, 6, 7, 43, 5, 35, 6, 53, 23, 678, 9876, 78]
even_numbers = list(filter(  lambda num: num % 2 == 0   ,   numbers  ))
print(even_numbers)

    
    
