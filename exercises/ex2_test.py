import unittest
from .CakesDb import *
from .SqlAnswerFileReader import *

class TestEx2(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestEx2, self).__init__(*args, **kwargs)
        self.eval_query = TestAnswers[2]
        user_cakes_db.exec_query("DELETE FROM CakeOrders;")
        user_cakes_db.exec_query(self.eval_query)

    def test_tables_fill(self):
        test_query = "SELECT OrderId from CakeOrders;"
        actual_names, actual_rows = user_cakes_db.select_query(test_query)
        expected_names, expected_rows = solution_cakes_db.select_query(test_query)

        assert len(actual_rows) == len(expected_rows),\
            f"Wrong number of rows expecting {len(actual_rows)} got {len(expected_rows)}"

        assert sorted(actual_rows) == sorted(expected_rows), \
            f"Wrong OrderId value found"



    def test_names_values(self):
        pass

    def test_orders_values(self):
        pass
