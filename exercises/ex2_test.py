import unittest
from .videoGameWorksheetModel import *


class TestEx2(unittest.TestCase):
    def test_StrategyTabTableValues(self):
        pass

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
        pass
