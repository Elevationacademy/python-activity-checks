import unittest
from .CakesDb import *
from .SqlAnswerFileReader import *

class TestEx1(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestEx1, self).__init__(*args, **kwargs)
        self.eval_query = TestAnswers[1]
        user_cakes_db.exec_query(self.eval_query)

    def test_table_exist(self):
        check_query = "SELECT * FROM sqlite_master where name = 'CakeOrders'"
        actual_names, actual_rows = user_cakes_db.select_query(check_query)
        assert 1 == len(actual_rows), \
            f"Table CakeOrders does no exits."

    def test_table_columns(self):
        test_query = "SELECT * FROM CakeOrders"
        actual_names, _ = user_cakes_db.select_query(test_query)
        expected_names, _ = solution_cakes_db.select_query(test_query)

        assert len(actual_names) == len(actual_names),\
            f"Wrong number of column expecting {len(expected_names)} got {len(actual_names)}"

        assert sorted(expected_names) == sorted(actual_names), \
            f"Wrong column names, expecting {expected_names} but it is {actual_names} "
