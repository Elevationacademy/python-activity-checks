import unittest
from .EmployeesWorksheetModel import *


class TestEx1(unittest.TestCase):
    def test_EmployeeData(self):
        cell = ws_data['A2']
        assert cell.data_type == 'f', f"cell {cell.coordinate} should be a formula"
        assert 'SORT' in cell.value, f"cell {cell.coordinate} formula should include SORT function"
        assert 'Employees!' in cell.value, f"cell {cell.coordinate} formula should include reference to Employees Tab"

    def test_TitlesColumn(self):
        pass

    def test_DepartmentColumn(self):
        pass

    def test_SalariesColumn(self):
        pass
