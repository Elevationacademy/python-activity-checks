from importlib.machinery import SourceFileLoader
import os
import pytest
import unittest

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
__location__ = os.path.dirname(os.path.dirname(__location__))

# Instrument class tests
class TestEx3(unittest.TestCase):
    def test_exercise3(self):
      try:
        evaluation_loc = os.path.join(__location__, 'src', 'Item.py')
        Item = SourceFileLoader("Item", evaluation_loc).load_module().Item
        evaluation_loc = os.path.join(__location__, 'src', 'Instrument.py')
        Instrument = SourceFileLoader("Instrument",evaluation_loc).load_module().Instrument
        inst = Instrument('Percussion', 'Guitar')
        assert isinstance(inst, Item), 'The Instrument class does not inherit from the Item class'
        assert inst.category == 'Percussion', f"The 'category' of the instrument was not initialized in the constructor. When passing 'Percussion' as an argument to the constructor, the category property was initialized to '{inst.category}' - make sure you're using 'self'"
        assert inst.type == 'Guitar', f"The 'type' of the instrument was not initialized in the constructor. When passing 'Guitar' as an argument to the constructor, the type property was initialized to '{inst.type}' - make sure you're using 'self'"
        inst.use()
        assert inst.value == 95, 'The use() method of Instrument class does not decrease the value property by 5 when its category equal to "Percussion". Make sure you override the use() method of Item'
        inst.category = 'Woodwind'
        inst.use()
        assert inst.value == 95, 'The use method of the Instrument class changed the value property even when the category was not equal to "Percussion"; the use method should NOT change the value property (at all) if its category is NOT equal to "Percussion". Make sure you override the use() method of Item'
      except Exception as e:
        assert False, f'{e}'