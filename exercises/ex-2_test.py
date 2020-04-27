from importlib.machinery import SourceFileLoader
import os
import pytest
import unittest

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
__location__ = os.path.dirname(os.path.dirname(__location__))

# Book class tests
class TestEx2(unittest.TestCase):
    def test_exercise2(self):
      try:
        evaluation_loc = os.path.join(__location__, 'src', 'Item.py')
        Item = SourceFileLoader("Item", evaluation_loc).load_module().Item
        evaluation_loc = os.path.join(__location__, 'src', 'Book.py')
        Book = SourceFileLoader("Book",evaluation_loc).load_module().Book
        book = Book('Elevation', 'Jona', 100)
        assert isinstance(book, Item), 'The Book class does not inherit from the Item class'
        assert book.title == 'Elevation', f"The 'title' of the book was not initialized in the constructor. When passing 'Elevation' as an argument to the constructor, the title property was initialized to '{book.title}' - make sure you're using 'self'"
        assert book.author == 'Jona', f"The 'author' of the book was not initialized in the constructor. When passing 'Jona' as an argument to the constructor, the author property was initialized to '{book.author}' - make sure you're using 'self'"
        assert book.pages == 100, f"The 'pages' of the book was not initialized in the constructor. When passing 100 as an argument to the constructor, the pages property was initialized to '{book.pages}' - make sure you're using 'self'"
        book.use()
        assert book.value == 95, 'The use() method of Book class does not decrease the value property by 5 when pages is greater than 50. Make sure you override the use() method of Item'
        book.pages = 40
        book.use()
        assert book.value == 85, 'The use() method of Book class does not decrease the value property by 10 when pages is smaller/equal to 50. Make sure you override the use() method of Item'
      except Exception as e:
        assert False, f'{e}'
