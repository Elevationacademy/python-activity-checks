import enum

class BikeStoreSheetCols(enum.Enum):
    OrderId = 0
    ItemId = 1
    ProductName = 2
    ModelYear = 3
    ListPrice = 5
    Quantity = 6
    LineTotal = 7
    Discount = 8
    DiscountPerUnit = 9
    LineTotalAfterDiscount = 10
    OrderDate = 11
    SalesMan = 12
    OldModel = 15
