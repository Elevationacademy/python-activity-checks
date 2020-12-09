import unittest
from .CakesDb import *

class TestEx2(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestEx2, self).__init__(*args, **kwargs)
        self.user_db = CakesDb("user_cakes_db.sqlite")

    def test_tables_fill(self):
        pass

    def test_names_values(self):
        pass

    def test_orders_values(self):
        pass
