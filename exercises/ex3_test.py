import openpyxl as oxl
from .EmployeesWorksheetModel import *
import unittest

class TestEx3(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestEx3, self).__init__(*args, **kwargs)
        self.emp_ws_data = wb_data['Employees']
        self.emp_ws_formula = wb_formulas['Employees']

    def checkHeader(self, name, col):
        cell = self.emp_ws_data[1][col]
        assert cell.value.strip() == name.strip(), f"expected column header on cell {cell.coordinate} should be {name} " \
                                   f"but it is {cell.value}"


    def test_FirstNameFirstLetter(self):
        self.checkHeader('FirstNameFirstLetter', 6)

    def test_LastNameLastLetter(self):
        self.checkHeader('LastNameLastLetter', 7)

    def test_TrimedEdgesName(self):
        self.checkHeader('TrimedEdgesName', 8)

    def test_FirstLetterIndex(self):
        self.checkHeader('FirstLetterIndex',9)

