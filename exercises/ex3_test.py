import openpyxl as oxl
from .BikeStoreModel import *
import unittest


class TestEx3(unittest.TestCase):
    def test_ColumnOldModel(self):
        for row in ws_data.iter_rows(min_row=2, max_row=row_count - 1):
            cell = row[BikeStoreSheetCols.OldModel.value]
            formula_cell = ws[cell.coordinate]
            assert formula_cell.data_type == 'f', f"cell {cell.coordinate} should be a formula"
            assert "IF" in formula_cell.value, f"cell {cell.coordinate} formula should include conditional"
            assert str(cell.row) in formula_cell.value, f"cell {cell.coordinate} should reference row {cell.row}"
            d = row[BikeStoreSheetCols.OrderDate.value].value
            y = row[BikeStoreSheetCols.ModelYear.value].value
            expected_val = 'YES' if d.year > y else 'NO'
            assert expected_val == cell.value, f"cell {cell.coordinate} value should be should {expected_val} but it it {cell.value} "

    def test_ColumnOldModelTotal(self):
        total_expected_val = 0
        for row in ws_data.iter_rows(min_row=2, max_row=row_count - 1):
            cell = row[BikeStoreSheetCols.OldModel.value]
            formula_cell = ws[cell.coordinate]
            d = row[BikeStoreSheetCols.OrderDate.value].value
            y = row[BikeStoreSheetCols.ModelYear.value].value
            total_expected_val += 1 if d.year > y else 0

        cell_actual = ws_data.cell(column=BikeStoreSheetCols.OldModel.value + 1, row=row_count)
        assert cell_actual.data_type == 'n', f"cell {cell.coordinate} type is not a number"
        assert total_expected_val == cell_actual.value, f"cell {cell_actual.coordinate} value should be {total_expected_val} but it is {cell_actual.value}"
        assert cell_actual.font.bold, f"cell {cell_actual.coordinate} style should be Bold"
        formula_cell = ws[cell_actual.coordinate]
        assert formula_cell.data_type == 'f', f"cell {cell.coordinate} should be a formula"
        assert "YES" in formula_cell.value, f"cell {cell.coordinate} formula should check the value of 'YES' values"
        assert "P" in formula_cell.value, f"cell {cell.coordinate} formula should reference column P range"
        assert "2" in formula_cell.value, f"cell {cell.coordinate} formula should reference row 2"
        assert str(row_count - 1) in formula_cell.value, f"cell {cell.coordinate} formula should reference row {str(row_count - 1)}"

    def test_TotalOrderId(self):
        total_expected_val = 0
        for row in ws_data.iter_rows(min_row=2, max_row=row_count - 1):
            cell = row[BikeStoreSheetCols.ItemId.value]
            formula_cell = ws[cell.coordinate]
            total_expected_val += 1 if cell.value == 1 else 0

        cell_actual = ws_data.cell(column=BikeStoreSheetCols.OrderId.value + 1, row=row_count)
        assert cell_actual.data_type == 'n', f"cell {cell.coordinate} type is not a number"
        assert total_expected_val == cell_actual.value, f"cell {cell_actual.coordinate} value should be {total_expected_val} but it is {cell_actual.value}"
        assert cell_actual.font.bold, f"cell {cell_actual.coordinate} style should be Bold"
        formula_cell = ws[cell_actual.coordinate]
        assert formula_cell.data_type == 'f', f"cell {cell.coordinate} should be a formula"
        assert "COUNTIF" in formula_cell.value or "SUMIF" in formula_cell.value , f"cell {cell.coordinate} formula should contain SUMIF or COUNTIF"
        assert str(row_count - 1) in formula_cell.value, f"cell {cell.coordinate} formula should reference row {str(row_count - 1)}"
