from importlib.machinery import SourceFileLoader
import os
import pytest
import unittest

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
__location__ = os.path.dirname(os.path.dirname(__location__))

# Item class tests
class TestEx1(unittest.TestCase):
    def test_exercise1(self):
        try:
            evaluation_loc = os.path.join(__location__, 'src', 'Item.py')
            Item = SourceFileLoader("Item", evaluation_loc).load_module().Item
            item = Item()
            assert item.status.lower() == 'available', f"The status property was not initialized in the constructor to 'Available', instead it was initalized with - '{item.status}'"
            assert item.value == 100, f"The value property was not initialized in the constructor to 100, instead it was initialized with -  {item.value}"
            item.use()
            assert item.value == 95, f"When invoking use() method of the Item class, the 'value' property was not decreased by 5"
        except Exception as e:
            assert False, f'{e}'