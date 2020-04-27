from importlib.machinery import SourceFileLoader
import os
import pytest
import unittest
from unittest.mock import Mock

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
__location__ = os.path.dirname(os.path.dirname(__location__))

# Client class tests
class TestEx4(unittest.TestCase):
    def test_exercise4(self):
      try:
        evaluation_loc = os.path.join(__location__, 'src', 'Store.py')
        Store = SourceFileLoader("Store", evaluation_loc).load_module().Store
        evaluation_loc = os.path.join(__location__, 'src', 'Book.py')
        Book = SourceFileLoader("Book", evaluation_loc).load_module().Book
        evaluation_loc = os.path.join(__location__, 'src', 'Client.py')
        Client = SourceFileLoader("Client",evaluation_loc).load_module().Client

        client = Client('Jona', 'Banana')
        assert client.first_name == 'Jona', f"The 'first_name' of the client was not initialized in the constructor. When passing 'Jona' as an argument to the constructor, the first_name was initialized to '{client.first_name}' - make sure you're using 'self'"
        assert client.last_name == 'Banana', f"The 'last_name' of the client was not initialized in the constructor. When passing 'Banana' as an argument to the constructor, the last_name was initialized to '{client.last_name}' - make sure you're using 'self'"
        assert client.rented_items == [], f"The 'rented_items' of the client was not initialized to an empty list in the constructor, instead it was initialized to ${client.rented_items} - make sure you're using 'self'"

        book = Book('Elevation', 'Jona', 100)
        store = Store('LH')
        client.checkout_item(book, store)
        assert len(client.rented_items) == 1, "The `checkout_item` method in the Client class did not push the item to the `rented_items` items list"

        store = Mock()
        client.checkout_item(book, store)
        assert store.rent_item.call_count == 1, "The rent_item() method in the Store class wasn't invoked by the checkout_item() method of the Client class"

      except Exception as e:
        assert False, f'{e}'