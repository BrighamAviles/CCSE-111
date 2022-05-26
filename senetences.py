import random
verbs = []



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

    if tense is == "past":
        verbs.append("drank", "ate", "grew", "laughed", "thought",
         "ran", "slept", "talked", "walked", "wrote")

    elif tense is == "present" and quantity = 1:
        verbs.append("drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes")

    elif tense is == "present" and quantity != 1:
        

    else if tense == "future":

        
        













def get_preposition():









def get_prepositional_phrase(quantity):

