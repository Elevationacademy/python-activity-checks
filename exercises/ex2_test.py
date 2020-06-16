import unittest
from .videoGameWorksheetModel import *


class TestEx2(unittest.TestCase):
    def test_StrategyTabTableValues(self):
        # check on the source data how many Strategy games we have.
        expected_count = 0
        for row in ws.iter_rows(min_row=2, max_row=row_count - 1):
            expected_count += 1 if row[VideoGameSalesSheetCols.Genre.value].value == "Strategy" else 0

        actual_count = 0
        sum_ws = wb_data['Strategy']
        for row in sum_ws.iter_rows(min_row=2, max_row=sum_ws.max_row - 1):
            cell = row[VideoGameSalesSheetCols.Genre.value]
            assert cell.value == 'Strategy', f"row  {cell.row} contains game from year {cell.value}"
            actual_count += 1

        assert expected_count == actual_count, f"rows count after filter should be {expected_count} but it is {actual_count} "


    def test_SortFormula(self):
        self.checkSortFormula('Eighties')
        self.checkSortFormula('Strategy')

    def checkSortFormula(self, ws_idx):
        sum_ws = wb_formulas[ws_idx]
        cell = sum_ws['A2']
        assert cell.data_type == 'f', f"cell {cell.coordinate} should be a formula"
        assert 'SORT' in cell.value, f"cell {cell.coordinate} formula should include SORT function"
        assert 'FILTER' in cell.value, f"cell {cell.coordinate} formula should include FILTER function"
        assert 'vgsales!' in cell.value, f"cell {cell.coordinate} formula should include refrence to vgsales Tab"


    def test_EightiesTabTableValues(self):
        # check on the source data how many Strategy games we have.
        expected_count = 0
        for row in ws.iter_rows(min_row=2, max_row=row_count):
            year = row[VideoGameSalesSheetCols.Year.value].value
            expected_count += 1 if 1980 <= year <= 1989 else 0

        prev_rank = 0
        actual_count = 0
        sum_ws = wb_data['Eighties']
        for row in sum_ws.iter_rows(min_row=2, max_row=sum_ws.max_row):
            rank = row[VideoGameSalesSheetCols.Rank.value - 1].value
            assert prev_rank <= rank, f"'Eighties' tab is not ordered correctly see row {row[0].row}"
            year = row[VideoGameSalesSheetCols.Genre.value - 1].value
            assert 1980 <= year <= 1989, f"row  {row.cell[0].row} contains game from year {year} which is not from the eighties "
            actual_count += 1

        assert expected_count == actual_count, f"'Eighties' tab rows count after filter should be {expected_count} but it is {actual_count} "
