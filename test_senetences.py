from senetences import get_determiner
import random 
import pytest


def test_get_determiner():
    determ = get_determiner(1)

    words = ["a", "one", "the"]
    assert determ in words

