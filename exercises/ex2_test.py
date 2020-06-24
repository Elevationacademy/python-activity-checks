import unittest
from .EmployeesWorksheetModel import *


class TestEx2(unittest.TestCase):

    def test_PivotTablesExistence(self):
        actual = len(ws_data._pivots)
        expected = 3
        assert actual == expected, f"The Employee Worksheet should include {expected} pivot tables, but it include {actual}"

    def assert_pivot_valid(self, pivot_name, expected_subtotal, rowField, colField, dataField = -1):
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

        assert len(p.pivotFields) >= 9, "Please make sure that all columns are references by the Pivot Table"

        assert p.rowFields[0].x == rowField, f"Pivot table {pivot_name} is not using the correct column for the row labels"
        if colField != -1:
            assert p.colFields[0].x == colField, f"Pivot table {pivot_name} is not using the correct column for the col labels"
        if dataField != -1:
            assert p.dataFields[0].fld == dataField, f"Pivot table {pivot_name} is not using the correct colunm for the Data"


        return p

    def test_DepartmentsCountPivotTable(self):
        pt = self.assert_pivot_valid('DepratmentsPersonalPivot', 'count', 7, 6)


    def test_AverageSalaryPivotTable(self):
        pt = self.assert_pivot_valid('AverageSalaryPivot', 'average',6 , 4, 8)

    def test_SalaryBudget(self):
        pt = self.assert_pivot_valid('SalaryBudgetPivot', 'sum', 7, -1, 8)
