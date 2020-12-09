import unittest
from .CakesDb import *
from .SqlAnswerFileReader import *

class TestEx7(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestEx7, self).__init__(*args, **kwargs)
        self.eval_query = TestAnswers[7]
        self.expected_query = """SELECT DISTINCT Name, Age, 
                CASE
                    WHEN Age > 20 THEN '5% Discount'
                    WHEN Age > 50 THEN '17% Discount'
                    WHEN Age > 80 THEN '25% Discount'
                    ELSE 'No Discount'
                END as AgeDiscount
                FROM CakeOrders;"""

    def test_select_query(self):
        assert all(x not in self.eval_query.upper() for x in ['DROP', 'DELETE', 'INSERT'])

    def test_rows_count(self):
        actual_names, actual_rows = user_cakes_db.select_query(self.eval_query)
        expected_names, expected_rows = solution_cakes_db.select_query(self.expected_query)

        assert len(actual_rows) == len(expected_rows),\
            f"Wrong number of rows expecting {len(actual_rows)} got {len(expected_rows)}"

    def test_cols_count(self):
        actual_names, actual_rows = user_cakes_db.select_query(self.eval_query)
        expected_names, expected_rows = solution_cakes_db.select_query(self.expected_query)

        assert len(actual_names) == len(expected_names),\
            f"Wrong number of cols expecting {len(actual_names)} got {len(expected_names)}"

    def test_rows_values(self):
        _, actual_rows = user_cakes_db.select_query(self.eval_query)
        _, expected_rows = solution_cakes_db.select_query(self.expected_query)

        assert sorted(actual_rows) == sorted(expected_rows), \
            f"expecting values: {sorted(expected_rows)}, found :  {sorted(actual_rows)}"
