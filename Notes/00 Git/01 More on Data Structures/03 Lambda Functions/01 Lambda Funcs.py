# A lambda function is an anonymous function

# standard way to define a function
def say_something(word):
    print(word)
    
# equivalent way as a lambda function
say_smthin = lambda word: print(word)

say_something("hi")
say_smthin("hello")

lambda word: print(word)

# another example
def add(x, y):
    return x + y

add_nums = lambda x, y: x + y 

print(add(1, 2))
print(add_nums(1, 2))

