import os
import sys
import pytest
import unittest

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
__location__ = os.path.dirname(os.path.dirname(__location__))
src_loc = os.path.join(__location__, 'src')

sys.path.insert(1, src_loc)
from exercise3 import init_players

class TestEx3(unittest.TestCase):
    def test_exercise3(self):
        try:
            add_to_score = init_players(Shoobert=3, Danny=0)
        except:
            assert False, "Expected init_players() function to be able to receive key-value pair, but got an error"

        if not callable(add_to_score):
            assert False, f"Expected init_players() function to return a function, but got an {type(add_to_score)} instead"

        try:
            new_score = add_to_score("Danny", "Shoobert")
        except:
            assert False, f"Expected for a init_players() function to return a function that can receive unknown number of arguments, but got an error"

        assert new_score == {'Shoobert': 4, 'Danny': 1}, f"Expected init_players(Shoobert=3, Danny=0) to return a function that when sending ('Danny', 'Shoobert') to, should return {'Shoobert': 4, 'Danny': 1}, but instead received {new_score}"

        new_score = add_to_score("Shoobert")

        assert new_score == {'Shoobert': 5, 'Danny': 1}, f"Exercise 3 - accepted init_players(Shoobert=3, Danny=0) to return a function that when sending ('Danny', 'Shoobert') and than ('Shoobert') to, should return {'Shoobert': 5, 'Danny': 1}, but instead received {new_score}"