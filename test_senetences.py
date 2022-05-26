from senetences import get_determiner, get_noun
import random 
import pytest


def test_get_determiner():
    single_determiners = ["a", "one", "the"]

    for _ in range(4):
        word = get_determiner(1)

        assert word in single_determiners
    
    plural_determiners = ["two", "some", "many", "the"]

    for _ in range(4):
        word = get_determiner(2)
        assert word in plural_determiners


def test_get_noun():
    single_determiners = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]

    for _ in range(4):
        word = get_noun(1)

        assert word in single_determiners

    plural_nouns = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "rabbits", "men", "women"]

    for _ in range(4):
        word = get_noun(2)
        assert word in plural_nouns





pytest.main(["-v", "--tb=line", "-rN", __file__])