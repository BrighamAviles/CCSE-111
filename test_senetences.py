from senetences import get_determiner
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



pytest.main(["-v", "--tb=line", "-rN", __file__])