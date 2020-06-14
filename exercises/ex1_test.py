import unittest
from .BikeStoreModel import *


class TestEx1(unittest.TestCase):
    def test_ColumnListPrice(self):
        for row in ws.iter_rows(min_row=2, max_row=row_count - 1):
            cell = row[BikeStoreSheetCols.ListPrice.value]
            assert cell.data_type != 'f', f"cell {cell.coordinate} should be a formula"
            assert '"$"' in cell.number_format, f"format of {cell.coordinate} should be $"
            assert '0.00' in cell.number_format, f"format of {cell.coordinate} should be 2 digits accurate"

    def test_ColumnDiscount(self):
        for row in ws.iter_rows(min_row=2, max_row=row_count - 1):
            cell = row[BikeStoreSheetCols.Discount.value]
            assert '0%' in cell.number_format, f"format of {cell.coordinate} should be %"

    def test_ColumnLineTotal(self):
        for row in ws_data.iter_rows(min_row=2, max_row=row_count - 1):
            cell = row[BikeStoreSheetCols.LineTotal.value]
            cell_formula = ws[cell.coordinate]
            assert cell.data_type != 'f', f"cell {cell.coordinate} should be a formula"
            assert cell_formula.value == f'=F{cell.row}*G{cell.row}' or cell_formula == f'=G{cell.row}*F{cell.row}', \
                f'cell {cell.coordinate} formula is wrong'
            # or cell_formula == f'=G{cell.row}*F{cell.row}'
            cell_expected_val = \
                row[BikeStoreSheetCols.Quantity.value].value * row[BikeStoreSheetCols.ListPrice.value].value
            cell_actual_val = cell.value
            self.assertAlmostEqual(cell_expected_val, cell_actual_val, places=4,
                msg=f"cell {cell.coordinate} value should be {cell_expected_val} but it is {cell_actual_val}")
            assert '"$"' in cell.number_format, f"format of {cell.coordinate} should be $"
            assert '0.00' in cell.number_format, f"format of {cell.coordinate} should be 2 digits accurate"

    def test_ColumnLineTotalAfterDiscount(self):
        for row in ws_data.iter_rows(min_row=2, max_row=row_count - 1):
            cell = row[BikeStoreSheetCols.LineTotalAfterDiscount.value]
            cell_formula = ws[cell.coordinate]
            cell.data_type != 'f', f"cell {cell.coordinate} should be a formula"
            cell_expected_val = \
                row[BikeStoreSheetCols.Quantity.value].value * row[BikeStoreSheetCols.ListPrice.value].value * \
                (1 - row[BikeStoreSheetCols.Discount.value].value)
            cell_actual_val = cell.value
            self.assertAlmostEqual(cell_expected_val, cell_actual_val, places=4,
                                   msg=f"cell {cell.coordinate} value should be {cell_expected_val} but it is {cell_actual_val}")
            assert '"$"' in cell.number_format, f"format of {cell.coordinate} should be $"
            assert '0.00' in cell.number_format, f"format of {cell.coordinate} should be 2 digits accurate"
