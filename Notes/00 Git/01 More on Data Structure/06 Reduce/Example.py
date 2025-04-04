from functools import reduce 

#reduce takes in a function and a list 
#function you pass in has two parameters
#It will apply that function to everything passed to it in a list 
#it will reduce based of what passed in 
#will be passed in the nect item in the list 

#Instead of returning a list it returns a single item 

a_list = [3,5,7,9]
def multiply (a, b):
    return a*b

product = 1
for num in a_list:
    product *= num
print(product)

#using reduce 
product = reduce(multiply, a_list)
print(product)

#using lambda
print(reduce(lambda a,b: a*b, a_list))