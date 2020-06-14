import os
import pytest
import unittest
import openpyxl as oxl

from .BikeStoreModel import BikeStoreSheetCols

wb_data = oxl.load_workbook('../Excel/Fundementals/Solution/BikeStoreSample.xlsx', read_only=False, data_only=True)
wb_formulas = oxl.load_workbook('../Excel/Fundementals/Solution/BikeStoreSample.xlsx', read_only=True, data_only=False)
ws = wb_formulas['OrderDetailsData']
ws_data = wb_data['OrderDetailsData']
row_count = ws.max_row

class TestEx4(unittest.TestCase):
    def test_TestYearsTotals(self):
        calc_ws = wb_formulas['YearlyIncome']
        calc_ws_data = wb_data['YearlyIncome']

        expected_vals = {}
        for row in ws_data.iter_rows(min_row=2, max_row=row_count - 1):
            order_date = row[BikeStoreSheetCols.OrderDate.value].value
            amount = row[BikeStoreSheetCols.LineTotalAfterDiscount.value].value
            if order_date.year not in expected_vals:
                expected_vals[order_date.year] = 0
            expected_vals[order_date.year] += amount

        for r in calc_ws_data.iter_cols(min_row=2, min_col=4, max_col=len(expected_vals) + 1, max_row=2):
            cell = r[0]
            assert '"$"' in cell.number_format, f"format of {cell.coordinate} should be $"
            assert '0.00' in cell.number_format, f"format of {cell.coordinate} should be 2 digits accurate"
            year = calc_ws_data.cell(column=cell.column, row=1).value # get the year value from first row
            assert cell.value == expected_vals[year], f"cell {cell.coordinate} value should be {expected_vals[year]} but it is {cell.value} "

            cell_formula = calc_ws[cell.coordinate]
            assert cell_formula.data_type == 'f', f"cell {cell.coordinate} should be a formula"
            assert "SUMIF" in cell_formula.value, f"cell {cell.coordinate} should formula should contain SUMIF"


    def test_TestMonthTotals(self):
        calc_ws = wb_formulas['MonthlyIncome']
        calc_ws_data = wb_data['MonthlyIncome']

        expected_vals = {}
        for row in ws_data.iter_rows(min_row=2, max_row=row_count - 1):
            order_date = row[BikeStoreSheetCols.OrderDate.value].value
            amount = row[BikeStoreSheetCols.LineTotalAfterDiscount.value].value
            if order_date.year not in expected_vals:
                expected_vals[order_date.year] = {}
            if order_date.month not in expected_vals[order_date.year]:
                expected_vals[order_date.year][order_date.month] = 0
            expected_vals[order_date.year][order_date.month] += amount

        for r in calc_ws_data.iter_cols(min_row=2, min_col=4, max_col=len(expected_vals) + 1, max_row=13):
            cell = r[0]
            assert '"$"' in cell.number_format, f"format of {cell.coordinate} should be $"
            assert '0.00' in cell.number_format, f"format of {cell.coordinate} should be 2 digits accurate"
            year = calc_ws_data.cell(column=cell.column, row=1).value # get the year value from first row
            month = calc_ws_data.cell(column=1, row=cell.row).value # get the month value from first column

            expected_value = 0 if month not in expected_vals[year] else expected_vals[year][month]
            assert cell.value == expected_value, f"cell {cell.coordinate} value should be {expected_value} but it is {cell.value}"

            cell_formula = calc_ws[cell.coordinate]
            assert cell_formula.data_type == 'f', f"cell {cell.coordinate} should be a formula"
            assert "SUMIF" in cell_formula.value, f"cell {cell.coordinate} should formula should contain SUMIF"

