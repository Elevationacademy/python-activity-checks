import os
import sys
import pytest
import unittest

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
__location__ = os.path.dirname(os.path.dirname(__location__))
src_loc = os.path.join(__location__, 'src')

sys.path.insert(1, src_loc)
from exercise2 import find_movies_by_max_runtime_and_directors

class TestEx2(unittest.TestCase):
    def test_exercise2(self):
        assert type(find_movies_by_max_runtime_and_directors(100,
                            "Martin Scorsese")) is map, f"Expected type of returned item from find_movies_by_max_runtime_and_directors() to be a map, but instead received type of {type(find_movies_by_max_runtime_and_directors(100, 'Martin Scorsese'))}"
        assert list(find_movies_by_max_runtime_and_directors(120, "Martin Scorsese")) == [
            'Taxi Driver'], f"Expected find_movies_by_max_runtime_and_directors(120, 'Martin Scorsese') to return ['Taxi Driver'], but instead received {list(find_movies_by_max_runtime_and_directors(120, 'Martin Scorsese'))}"
        assert list(find_movies_by_max_runtime_and_directors(110, "Alfred Hitchcock", "Woody Allen")) == ['Midnight in Paris', 'Vicky Cristina Barcelona',
                                                                        'Psycho'], f"Expected find_movies_by_max_runtime_and_directors(110, 'Alfred Hitchcock', 'Woody Allen') to return ['Midnight in Paris', 'Vicky Cristina Barcelona', 'Psycho'], but instead received {list(find_movies_by_max_runtime_and_directors(110, 'Alfred Hitchcock', 'Woody Allen'))}"

