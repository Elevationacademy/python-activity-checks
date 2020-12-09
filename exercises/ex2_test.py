import unittest
from CakesDb import *

class TestEx1(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestEx1, self).__init__(*args, **kwargs)
        self.user_db = CakesDb("user_cakes_db.sqlite")

    def test_tables_fill(self):
        expected_query = "SELECT table FROM sqlite_master WHERE name = 'CakeOrders'


    def test_names_values(self):
        expected_query = "SELECT CompanyName, ContactName, Phone from Customers where ContactTitle = 'Owner' and Country = 'Mexico'"
        actual_query = self.ReadAnswerFile('q1')
        expected_names, exected_rows = nw.select_query(expected_query)
        actual_names, actual_rows = nw.select_query(actual_query)

        assert len(expected_names) == len(actual_names),\
            f"Wrong number of columns, expecting {len(expected_names)} but it is {len(actual_names)} "

        assert len(exected_rows) == len(actual_rows),\
            f"Wrong number of rows,  expecting {len(exected_rows)} but it is {len(actual_rows)} "

        assert sorted(expected_names) == sorted(actual_names), \
            f"Wrong column selected,  expecting {expected_names} but it is {actual_names} "

    def test_orders_values(self):
        expected_query = "SELECT "
        actual_query = self.ReadAnswerFile('q2')
