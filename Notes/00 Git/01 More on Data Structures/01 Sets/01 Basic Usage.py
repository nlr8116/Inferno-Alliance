# Sets in python are collections of data
# that has no order and every item is unique

# define a set
a_set = {5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 2, 3, 4, 5}
another = {"hi","hi", "hello"}

print(a_set)
print(another)

# Converting from other iterables
a_list = [5, 5, 5, 5, 5, 5, 3, 2, -10]
converted = set(a_list)  # removes duplicates and order
print(converted)
converted_back = list(converted)
print(converted_back)

