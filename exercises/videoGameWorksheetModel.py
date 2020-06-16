import enum
import openpyxl as oxl

workbook_file = '/home/excel.xlsx'

wb_data = oxl.load_workbook(workbook_file, read_only=False, data_only=True)
wb_formulas = oxl.load_workbook(workbook_file, read_only=True, data_only=False)
ws = wb_formulas['vgsales']
ws_data = wb_data['vgsales']
row_count = ws.max_row


class VideoGameSalesSheetCols(enum.Enum):
    Rank = 0
    Name = 1
    Platform = 2
    Year = 3
    Genre = 5
    Publisher = 6
    NaSales = 7
    EuSales = 8
    JpSales = 9
    OtherSales = 10
    GlobalSales = 11


#class VideoGameDetails
#    def __init__(self, row):
#        self.Year = row[VideoGameSalesSheetCols.Year].value
#        self.Genre = row[VideoGameSalesSheetCols.Year].value
#        self.Platform = row[VideoGameSalesSheetCols.Year].value
#        self.Publisher = row[VideoGameSalesSheetCols.Year].value
#        self.Rank = row[VideoGameSalesSheetCols.Year].value


