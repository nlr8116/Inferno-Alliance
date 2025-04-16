# List comprehension allows us 
# to write for loops on one line
from random import randint

numbers = [ i for i in range(10)]
print(numbers)

numbers = [ i*2 for i in range(10)]
print(numbers)

numbers = [randint(0,100) for i in range(5)]
print(numbers)

even_numbers = [ akfhgkaj for akfhgkaj in range(20) if akfhgkaj % 2 == 0]
print(even_numbers)

pairs = [(x, y) for x in range(4) for y in range(3)]
print(pairs)

pairs = [(x, y) for x in range(4) for y in range(3) if x%2 == 0 if y%2 == 0]
print(pairs)


foods = ["pizza", "more pizza", "chick fil a", "chicken salad"]

result = [f"I like {food}" for food in foods]
print(result)

# for loop equivalent of list comprehension
result = []
for food in foods:
    result.append(f"I like {food}")
    
[print("hi") for _ in range(10)]