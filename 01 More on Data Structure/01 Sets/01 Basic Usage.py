#sets in python are collections of data That has no order and every item is unique 

#define a set
a_set = {1, 2, 3, 4, 5}
another = {'Hi', 'Hi', "hello"}

print(a_set)
print(another)

#converting from, iterables
a_list= [1,2,3,4,5,5,5,-5,5,5,5,5, -10]
converted = set(a_list) # removes duplicates and order 
print(converted)
converted_back = list(converted)
print(converted_back)