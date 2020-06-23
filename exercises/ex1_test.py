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

    def check_col_formula(self, col_no, ref_substr, formula_substr):
        for row in ws.iter_rows(min_row=2, max_row=row_count):
            cell = row[col_no]
            assert cell.data_type == 'f', f"cell {cell.coordinate} should be a formula"
            for f in formula_substr:
                assert f in cell.value, f"cell {cell.coordinate} formula should include {f} function"
            for r in ref_substr:
                assert r in cell.value, f"cell {cell.coordinate} formula should reference to {r}"

    def test_TitlesColumn(self):
        self.check_col_formula(EmployeesDataCols.Title.value, ['titles'], ['VLOOKUP'])
        employees_db.fetch_title()
        for row in ws_data.iter_rows(min_row=2, max_row=row_count):
            actual = row[EmployeesDataCols.Title.value].value
            emp_no = row[EmployeesDataCols.No.value].value
            expected_value = employees_db.collection[emp_no].Title
            assert actual == expected_value, f" Wrong value in row {row[0].row - 1}" \
                                            f" found {actual} expecting {expected_value}"

    def test_DepartmentColumn(self):
        self.check_col_formula(EmployeesDataCols.Department.value, ['dept_emp'], ['VLOOKUP'])
        employees_db.fetch_departments()
        for row in ws_data.iter_rows(min_row=2, max_row=row_count):
            actual = row[EmployeesDataCols.Department.value].value
            emp_no = row[EmployeesDataCols.No.value].value
            expected_value = employees_db.collection[emp_no].Department
            assert actual == expected_value, f" Wrong value in row {row[0].row - 1}" \
                                             f" found {actual} expecting {expected_value}"

    def test_SalariesColumn(self):
        self.check_col_formula(EmployeesDataCols.Salary.value, ['salaries'], ['VLOOKUP'])
        employees_db.fetch_salaries()
        for row in ws_data.iter_rows(min_row=2, max_row=row_count):
            actual = row[EmployeesDataCols.Salary.value].value
            emp_no = row[EmployeesDataCols.No.value].value
            expected_value = employees_db.collection[emp_no].Salary
            assert actual == expected_value, f" Wrong value in row {row[0].row - 1}" \
                                             f" found {actual} expecting {expected_value}"
