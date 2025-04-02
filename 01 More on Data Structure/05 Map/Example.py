#the map() function 
# Takes in a function that we want to apply to every item in a list
# Returns a list of equal size as the input list with the function having been applied to every item in the input list 

foods  =["sushi",'burgers','tacos','bbq','squid','cow tounge','deviled eggs', 'spaghetti','momp']

def make_sentence(food_item):
    return f"I like {food_item}."

#for loop way of mapping things
sentences = []
for food in foods:
    new_sentence = make_sentence(food)
    sentences.append(new_sentence)
print(sentences)

sentences = list(map(make_sentence, foods))
sentences = list(map(lambda food:f"I like {food}.", foods))
print(sentences)