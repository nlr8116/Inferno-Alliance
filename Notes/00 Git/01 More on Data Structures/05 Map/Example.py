# The map() function

# Takes in a function that we want to apply to 
# every item in a list (that it also takes in).

# Returns a list of equal size as the input list
# with the function having been applied to every item in
# the input list

foods = [
    "sushi", "burgers", "tacos", 
    "bbq", "squid", "cow tongue", 
    "deviled eggs", "spaghetti", "momo"
]

def make_sentence(food_item):
    return f"I like {food_item}"

# for loop way of mapping things
sentences = []
for food in foods:
    new_sentence = make_sentence(food)
    sentences.append(new_sentence)
print(sentences)

# same thing but with map()

sentences = list(map(make_sentence, foods))
print(sentences)

# same but with lambda inside of map
sentences = list(map(lambda food_item: f"I like {food_item}"  , foods))

