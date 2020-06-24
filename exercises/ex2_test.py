import unittest
from .EmployeesWorksheetModel import *


class TestEx2(unittest.TestCase):

    def test_PivotTablesExistence(self):
        actual = len(ws_data._pivots)
        expected = 3
        assert actual == expected, f"The Employee Worksheet should include {expected} pivot tables, but it include {actual}"

    def assert_pivot_exists(self, pivot_name, expected_subtotal):
        p = None
        for pt in ws_data._pivots:
            if pt.name == pivot_name:
                p = pt
        assert p is not None, f"could not find pivot table named {pivot_name}"
        ws_src = p.cache.cacheSource.worksheetSource
        assert 'EmployeesData' in ws_src.sheet, f"Pivot table {pivot_name} is not referencing EmployeesData Sheet"
        actual_subtotal = p.dataFields[0].subtotal
        assert actual_subtotal == expected_subtotal, f"Pivot table {pivot_name} sub total " \
                                                     f"should be {expected_subtotal} but it {actual_subtotal}"
        return p

    def test_DepartmentsCountPivotTable(self):
        pt = self.assert_pivot_exists('DepratmentsPersonalPivot', 'count')


    def test_AverageSalaryPivotTable(self):
        pt = self.assert_pivot_exists('AverageSalaryPivot', 'average')

    def test_SalaryBudget(self):
        pt = self.assert_pivot_exists('SalaryBudgetPivot', 'sum')
