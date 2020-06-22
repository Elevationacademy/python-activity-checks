import unittest
from .EmployeesWorksheetModel import *


class TestEx1(unittest.TestCase):
    def test_EmployeeData(self):
        cell = ws['A2']
        assert cell.data_type == 'f', f"cell {cell.coordinate} should be a formula"
        assert 'SORT' in cell.value, f"cell {cell.coordinate} formula should include SORT function"
        assert 'Employees!' in cell.value, f"cell {cell.coordinate} formula should include reference to Employees Tab"

    def test_TableSort(self):
        prev_no = 0
        for row in ws_data.iter_rows(min_row=2, max_row=row_count):
            cur_no = row[EmployeesDataCols.No.value].value
            assert cur_no > prev_no, f" The EmpolyeesData Tab is not ordered as expected, row {row[0].row - 1}" \
                                     f" should come after row {row[1].row}"

    def test_TitlesColumn(self):
        pass

    def test_DepartmentColumn(self):
        pass

    def test_SalariesColumn(self):
        pass
