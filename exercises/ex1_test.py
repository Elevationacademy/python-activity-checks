import unittest
from .videoGameWorksheetModel import *


class TestEx1(unittest.TestCase):
    def test_YearColumn(self):
        for row in ws.iter_rows(min_row=2, max_row=row_count - 1):
            cell = row[VideoGameSalesSheetCols.Year.value]
            assert cell.data_type == 'n', f"cell {cell.coordinate} should be a numeric"

    def test_TableSort(self):
        pass

    def test_GloablSalesValues(self):
        pass

