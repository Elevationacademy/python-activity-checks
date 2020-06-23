import unittest
from .EmployeesWorksheetModel import *


class TestEx2(unittest.TestCase):

    def test_PivotTablesExistence(self):
        actual = len(ws_data._pivots)
        expected = 3
        assert actual == expected, f"The Employee Worksheet should include {expected} pivot tables, but it include {actual}"

    def assert_pivot_exists(self, pivot_name):
        for pt in ws_data._pivots:
            if pt.name == pivot_name:
                return pt
        assert False, f"could not find pivot table named {pivot_name}"
        ws_src = pt.cache.cacheSource.worksheetSource
        assert 'EmployeesData' in ws_src.sheet, f"Pivot table {pivot_name} is not referenceing EmployeesData Sheet"


    def test_DepartmentsCountPivotTable(self):
        pt = self.assert_pivot_exists('DepratmentsPersonalPivot')



    def test_AverageSalaryPivotTable(self):
        pt = self.assert_pivot_exists('AverageSalaryPivot')


    def test_SalaryBudget(self):
        pt = self.assert_pivot_exists('SalaryBudgetPivot')
