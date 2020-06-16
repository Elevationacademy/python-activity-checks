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
#            print(row[0].row, cur_vg.__dict__)
            assert prev_vg <= cur_vg, f"table is not ordered correctly, see row {row[0].row}"
            prev_vg = cur_vg

    def test_GlobalSalesValues(self):
        pass

