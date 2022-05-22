from senetences import get_determiner, get_noun, get_verbs
import random 
import pytest


def test_get_determiner():
    determ = get_determiner(1)

    words = ["a", "one", "the"]
    assert determ in words

