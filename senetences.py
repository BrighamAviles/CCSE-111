import random




def get_determiner(quantity):
    words = ["the", "a", "one", "some", "many"]

    if quantity == 1:
          words = ["a", "one", "the"]
    else:
        words = ["two", "some", "many", "the"]

    word = random.choice(words)
    return word

def get_noun(quantity):

    words = [ "bird", "boy", "car", "cat", "child","dog", "girl", "man", "rabbit", "woman", "birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]

    if quantity == 1:
        words = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    else:
        words = [ "birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]

    word = random.chice(words)
    return word



