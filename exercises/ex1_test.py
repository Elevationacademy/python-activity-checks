import math
import unittest
from .videoGameWorksheetModel import *


class TestEx1(unittest.TestCase):
    def test_YearColumn(self):
        for row in ws.iter_rows(min_row=2, max_row=row_count - 1):
            cell = row[VideoGameSalesSheetCols.Year.value]
            assert cell.data_type == 'n', f"cell {cell.coordinate} does not contain a numeric year value "
            assert cell.value <= 2016, f"cell {cell.coordinate} contains value from year {cell.value}, this row should be removed. "

    def test_TableSort(self):
        prev_vg = VideoGameDetails(ws[2])
        for row in ws.iter_rows(min_row=3, max_row=row_count - 1):
            cur_vg = VideoGameDetails(row)
            assert prev_vg <= cur_vg, f"table is not ordered correctly, see row {row[0].row}"
            prev_vg = cur_vg

    def test_GlobalSalesValues(self):
        for row in ws_data.iter_rows(min_row=2, max_row=row_count - 1):
            cell = row[VideoGameSalesSheetCols.GlobalSales.value]
            assert cell.data_type == 'n', f"cell {cell.coordinate} does not contain a value "
            expected_value = row[VideoGameSalesSheetCols.EuSales.value].value + \
                             row[VideoGameSalesSheetCols.JpSales.value].value + \
                             row[VideoGameSalesSheetCols.NaSales.value].value + \
                             row[VideoGameSalesSheetCols.OtherSales.value].value
            self.assertAlmostEqual(cell.value, expected_value, places=4,
                                    msg=f"cell {cell.coordinate} value should be {expected_value} but it is {cell.value}")

        # this loop is done separately since using cell_formula[cell.coordinate] inflicts great delays
        for row in ws.iter_rows(min_row=2, max_row=row_count - 1):
            cell_formula = row[VideoGameSalesSheetCols.GlobalSales.value]
            assert cell_formula.data_type == 'f', f"cell {cell_formula.coordinate} should be a formula"

