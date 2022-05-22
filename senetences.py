import random




def get_determiner(quantity):
    words = ["the", "a", "one", "some", "many"]

    if quantity == 1:
          words = ["a", "one", "the"]
    else:
        words = ["two", "some", "many", "the"]

    word = random.choice(words)
    return word





