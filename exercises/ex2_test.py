import unittest
from .BikeStoreModel import *


class TestEx2(unittest.TestCase):
    def test_PotentialIncome(self):
        cell_expected_val = 0.
        for row in ws_data.iter_rows(min_row=2, max_row=row_count - 1):
            cell = row[BikeStoreSheetCols.LineTotal.value]
            cell_expected_val += cell.value
        cell_actual = ws_data.cell(column=BikeStoreSheetCols.LineTotal.value + 1, row=row_count)
        assert cell_actual.data_type == 'n', f"cell {cell.coordinate} type is not a number"
        self.assertAlmostEqual(cell_expected_val, cell_actual.value, places=3,
                               msg=f"cell {cell_actual.coordinate} value should be {cell_expected_val:.2f} but it is {cell_actual.value:.2f}")
        assert '"$"' in cell_actual.number_format, f"format of {cell_actual.coordinate} should be $"
        assert '0.00' in cell_actual.number_format, f"format of {cell_actual.coordinate} should be 2 digits accurate"
        assert cell_actual.font.bold, f"cell {cell_actual.coordinate} style should be Bold"
        formula_cell = ws[cell_actual.coordinate]
        assert formula_cell.data_type == 'f', f"cell {cell.coordinate} should be a formula"
        assert "SUM" in formula_cell.value, f"cell {cell.coordinate} formula should include SUM"

    def test_OrderDetailsCount(self):
        cell_expected_val = 0
        for row in ws_data.iter_rows(min_row=2, max_row=row_count - 1):
            cell = row[BikeStoreSheetCols.Quantity.value]
            cell_expected_val += cell.value
        cell_actual = ws_data.cell(column=BikeStoreSheetCols.Quantity.value + 1, row=row_count)
        assert cell_actual.data_type == 'n', f"cell {cell.coordinate} type is not a number"
        self.assertAlmostEqual(cell_expected_val, cell_actual.value, places=3,
                               msg=f"cell {cell_actual.coordinate} value should be {cell_expected_val:.2f} but it is {cell_actual.value:.2f}")
        assert cell_actual.font.bold, f"cell {cell_actual.coordinate} style should be Bold"
        formula_cell = ws[cell_actual.coordinate]
        assert formula_cell.data_type == 'f', f"cell {cell.coordinate} should be a formula"
        assert "SUM" in formula_cell.value, f"cell {cell.coordinate} formula should include SUM"


    def test_OrderedItems(self):
        cell_expected_val = 0
        for row in ws_data.iter_rows(min_row=2, max_row=row_count - 1):
            cell = row[BikeStoreSheetCols.ItemId.value]
            cell_expected_val += 1
        cell_actual = ws_data.cell(column=BikeStoreSheetCols.ItemId.value + 1, row=row_count)
        assert cell_actual.data_type == 'n', f"cell {cell.coordinate} type is not a number"
        assert cell_expected_val == cell_actual.value, f"cell {cell_actual.coordinate} value should be {cell_expected_val} but it is {cell_actual.value}"
        assert cell_actual.font.bold, f"cell {cell_actual.coordinate} style should be Bold"
        formula_cell = ws[cell_actual.coordinate]
        assert formula_cell.data_type == 'f', f"cell {cell.coordinate} should be a formula"
        assert "COUNT" in formula_cell.value, f"cell {cell.coordinate} formula should include COUNT"


    def test_AverageCostForOrderedItem(self):
        cell_expected_val = 0.0
        for row in ws_data.iter_rows(min_row=2, max_row=row_count - 1):
            cell = row[BikeStoreSheetCols.ListPrice.value]
            cell_expected_val += cell.value
        cell_expected_val /= (row_count - 2)
        cell_actual = ws_data.cell(column=BikeStoreSheetCols.ListPrice.value + 1, row=row_count)
        assert cell_actual.data_type == 'n', f"cell {cell.coordinate} type is not a number"
        self.assertAlmostEqual(cell_expected_val, cell_actual.value, places=3,
                               msg=f"cell {cell_actual.coordinate} value should be {cell_expected_val:.2f} but it is {cell_actual.value:.2f}")
        assert cell_actual.font.bold, f"cell {cell_actual.coordinate} style should be Bold"
        formula_cell = ws[cell_actual.coordinate]
        assert formula_cell.data_type == 'f', f"cell {cell.coordinate} should be a formula"
        assert "AVERAGE" in formula_cell.value, f"cell {cell.coordinate} formula should include AVERAGE"



    def test_AverageDiscountPerUnit(self):
        cell_expected_val = 0.0
        for row in ws_data.iter_rows(min_row=2, max_row=row_count - 1):
            cell = row[BikeStoreSheetCols.DiscountPerUnit.value]
            cell_expected_val += cell.value
        cell_expected_val /= (row_count - 2)
        cell_actual = ws_data.cell(column=BikeStoreSheetCols.DiscountPerUnit.value + 1, row=row_count)
        assert cell_actual.data_type == 'n', f"cell {cell.coordinate} type is not a number"
        assert cell_expected_val == cell_actual.value, f"cell {cell_actual.coordinate} value should be {cell_expected_val} but it is {cell_actual.value}"
        assert cell_actual.font.bold, f"cell {cell_actual.coordinate} style should be Bold"
        formula_cell = ws[cell_actual.coordinate]
        assert formula_cell.data_type == 'f', f"cell {cell.coordinate} should be a formula"
        assert "AVERAGE" in formula_cell.value, f"cell {cell.coordinate} formula should include AVERAGE"

    def test_TotalIncome(self):
        cell_expected_val = 0
        for row in ws_data.iter_rows(min_row=2, max_row=row_count - 1):
            cell = row[BikeStoreSheetCols.LineTotalAfterDiscount.value]
            cell_expected_val += cell.value
        cell_actual = ws_data.cell(column=BikeStoreSheetCols.LineTotalAfterDiscount.value + 1, row=row_count)
        assert cell_actual.data_type == 'n', f"cell {cell.coordinate} type is not a number"
        assert cell_expected_val == cell_actual.value, f"cell {cell_actual.coordinate} value should be {cell_expected_val} but it is {cell_actual.value}"
        assert cell_actual.font.bold, f"cell {cell_actual.coordinate} style should be Bold"
        formula_cell = ws[cell_actual.coordinate]
        assert formula_cell.data_type == 'f', f"cell {cell.coordinate} should be a formula"
        assert "SUM" in formula_cell.value, f"cell {cell.coordinate} formula should include SUM"
