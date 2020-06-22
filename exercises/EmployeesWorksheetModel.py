import enum
import openpyxl as oxl

workbook_file = '/home/excel.xlsx'

wb_data = oxl.load_workbook(workbook_file, read_only=False, data_only=True)
wb_formulas = oxl.load_workbook(workbook_file, read_only=True, data_only=False)
ws = wb_formulas['EmployeesData']
ws_data = wb_data['EmployeesData']
row_count = ws.max_row

class EmployeesDataCols(enum.Enum):
    No = 0
    BirthDate = 1
    FirstName = 2
    LastName = 3
    Gender = 4
    HireDate = 5
    Title = 6
    Department = 7
    Salary = 8
    Seniority = 9


class EmployeeDetails:
    def __init__(self, row):
        self.No = row[EmployeesDataCols.No.value].value
        self.BirthDate = row[EmployeesDataCols.BirthDate.value].value
        self.FirstName = str(row[EmployeesDataCols.FirstName.value].value)
        self.LastName = row[EmployeesDataCols.LastName.value].value
        self.Gender = row[EmployeesDataCols.Gender.value].value
        self.HireDate = row[EmployeesDataCols.HireDate.value].value
        self.Title = row[EmployeesDataCols.Title.value].value
        self.Department = row[EmployeesDataCols.Department.value].value
        self.Salary = row[EmployeesDataCols.Salary.value].value
#        self.Seniority = row[EmployeesDataCols.Title.value].value

    def __eq__(self, other):
        return self.No == other.No

    def __ne__(self, other):
        return not self == other

    def __le__(self, other):
        return self.No <= other.No

    def __gt__(self, other):
        return not self <= other

    def __ge__(self, other):
        return self.No >= other.No

    def __lt__(self, other):
        return not self >= other


