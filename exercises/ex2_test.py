import unittest
from .CakesDb import *
from .SqlAnswerFileReader import *

class TestEx2(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestEx2, self).__init__(*args, **kwargs)
        self.eval_query = TestAnswers[2]
        user_cakes_db.exec_query("DELETE FROM CakeOrders;")
        user_cakes_db.exec_query(self.eval_query)

    def validate_column_values(self, column_name):
        test_query = f"SELECT {column_name} from CakeOrders;"
        _, actual_rows = user_cakes_db.select_query(test_query)
        _, expected_rows = solution_cakes_db.select_query(test_query)

        assert sorted(actual_rows) == sorted(expected_rows), \
            f"Wrong {column_name} value found"

    def test_table_rowcount(self):
        test_query = "SELECT * from CakeOrders;"
        _, actual_rows = user_cakes_db.select_query(test_query)
        _, expected_rows = solution_cakes_db.select_query(test_query)

        assert len(actual_rows) == len(expected_rows),\
            f"Wrong number of rows expecting {len(actual_rows)} got {len(expected_rows)}"

    def test_OrderId(self):
        self.validate_column_values("OrderId")

    def test_CustomerID(self):
        self.validate_column_values("CustomerID")

    def test_Name(self):
        self.validate_column_values("Name")

    def test_Age(self):
        self.validate_column_values("Age")
