import openpyxl as oxl
from .videoGameWorksheetModel import *
import unittest


class TestEx3(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestEx3, self).__init__(*args, **kwargs)
        self.worksheet_data = wb_data['Genres']
        self.worksheet_formula = wb_formulas['Genres']
        self.max_row = self.worksheet_data.max_row

    def test_GenresColumn(self):
        expected_genres_values = set()
        # check on the source data how many Strategy games we have.
        for row in ws.iter_rows(min_row=2, max_row=row_count):
            expected_genres_values.add(row[VideoGameSalesSheetCols.Genre.value].value)

        actual_genres_values = []
        actual_genres_values_set = set()

        for row in self.worksheet_data.iter_rows(min_row=2, max_row=self.max_row):
            assert row[0].data_type == 's', f"{row[0].coordinate} type should be string."
            actual_genres_values.append(row[0].value)
            actual_genres_values_set.add(row[0].value)

        assert len(actual_genres_values) >= len(actual_genres_values_set), f"some genres on " \
                                                                          f"'Genres tabs appears more than once."

        assert len(expected_genres_values) == len(actual_genres_values), f"wrong number of genres added to Genres tab "


    def test_GameCount(self):

        expected_genres_counts = {}
        for row in ws.iter_rows(min_row=2, max_row=row_count):
            cur_genre = row[VideoGameSalesSheetCols.Genre.value].value
            if cur_genre not in expected_genres_counts.keys():
                expected_genres_counts[cur_genre] = 1
            else:
                expected_genres_counts[cur_genre] += 1

        for row in self.worksheet_data.iter_rows(min_row=2, max_row=self.max_row):
            cell = row[1]
            assert cell.data_type == 'n', f"cell {cell.coordinate} type should be numeric"
            formula_cell = self.worksheet_formula[cell.coordinate]
            assert formula_cell.data_type == 'f', f"cell {cell.coordinate} should be a formula"
            assert "COUNTIF" in formula_cell.value, f"cell {cell.coordinate} should include COUNTIF in its formula"
            genre = row[0].value
            assert expected_genres_counts[genre] == cell.value, f"Genere {genre} count is {cell.value} but it " \
                                                                f"should be {expected_genres_counts[genre]}"


    def test_TotalIncome(self):
        pass


    def test_PieChart(self):
        pass