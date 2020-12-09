import unittest
from .CakesDb import *

class TestEx6(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestEx6, self).__init__(*args, **kwargs)
        self.user_db = CakesDb("user_cakes_db.sqlite")

    def test_colums_count(self):
        pass

    def test_result_values(self):
        pass
