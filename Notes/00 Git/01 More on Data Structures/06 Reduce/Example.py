from functools import reduce

# reduce() takes in a function and a list
# The function you pass in has 2 parameters 
# It will apply that function to everything in the list
# The prior result from the function you passed in
# will be passed in with the next item in the list

# Instead of returning a list like map() and filter()
# it returns a single item

a_list = [3, 5, 7, 9]

def multiply(a, b):
    print(a, b)
    return a * b 

# Using reduce 
product = reduce(multiply, a_list)
print(product)


# Example with for loop
product = 1
for i in range(len(a_list)):
    product *= a_list[i]
print(product)

# With lambda function
product = reduce(lambda a, b: a * b, a_list)
print(product)