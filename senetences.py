import random




def get_determiner(quantity):
    words = ["the", "a", "one", "two", "some", "many"]

    if quantity == 1:
          words = ["a", "one", "the"]
    else:
        words = ["two", "some", "many", "the"]

    word = random.choice(words)
    return word

def get_noun(quantity):
    words = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman", "birds", "boys", "cars", "cats", "children", "dogs", "girls", "rabbits"]

    if quantity == 1:
        words = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    else:
        words = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "rabbits", "men", "women"]

    word = random.choice(words)
    return word

def get_verb(quantity, tense):














def get_preposition():









def get_prepositional_phrase(quantity):

