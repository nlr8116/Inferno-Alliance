#A Lambda function is an anonymous function

#Standard way to define functions
def say_something (word):
    print(word)

#equevalent way as a labda function
say_somethin = lambda word : print(word)

say_somethin("hi")
say_something("hello")

#another example
def add(x, y):
    return x + y

add_num = lambda x , y: x + y

print(add_num (1,2))
print(add(3,2))