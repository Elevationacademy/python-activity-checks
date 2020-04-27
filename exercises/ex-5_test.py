from importlib.machinery import SourceFileLoader
import os
import pytest
import unittest
from unittest.mock import Mock

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
__location__ = os.path.dirname(os.path.dirname(__location__))

# Store class tests
class TestEx5(unittest.TestCase):
    def test_exercise5(self):
      try:
        evaluation_loc = os.path.join(__location__, 'src', 'Store.py')
        Store = SourceFileLoader("Store", evaluation_loc).load_module().Store
        evaluation_loc = os.path.join(__location__, 'src', 'Book.py')
        Book = SourceFileLoader("Book", evaluation_loc).load_module().Book
        evaluation_loc = os.path.join(__location__, 'src', 'Client.py')
        Client = SourceFileLoader("Client",evaluation_loc).load_module().Client

        # Properties Tests
        store = Store('Elevation')
        assert store.name == 'Elevation', f"The 'name' of the store was not initialized in the constructor. When passing 'Elevation' as an argument to the constructor, the name was initialized to '{store.name}' - make sure you're using 'self'"
        assert store.clients == [], f"The 'clients' of the `store was not initialized to an empty list in the constructor, instead it was initialized to {store.clients} - make sure you're using 'self'"
        assert store.items == [], f"The 'items' of the `store was not initialized to an empty list in the constructor, instead it was initialized to {store.items} - make sure you're using 'self'"

        # add_item() Tests
        book = Book('Elevation', 'Jona', 100)
        store.add_item(book)
        book.status = book.status.lower()
        assert len(store.items) == 1, "The `add_item` method of the Store class did not push the item it received to the `items` list of the store"
        assert isinstance(store.items[0], Book), "The `add_item` method of the Store class did not push the item it received to the `items` list of the store"

        # add_client() Tests
        client = Client('Jona', 'Banana')
        store.add_client(client)
        assert len(store.clients) == 1, "The `add_client` method of the Store class did not push the client it received to the `clients` list of the store"
        assert isinstance(store.clients[0], Client), "The `add_client` method of the Store class did not push the client it received to the `clients` list of the store"

        # repair_item() Tests
        store.repair_item(book)
        book.status = book.status.lower()
        assert book.status == 'in repair', "The 'repair_item' method of the Store class did not change the 'status' property of the item it received to 'In Repair', instead it was initialized to '{book.status}'"

        # rent_item() Tests
        book.status = 'Available'
        store.rent_item(book, client)
        book.status = book.status.lower()
        assert book.status == 'rented', "The 'rent_item' method of the Store class did not change the 'status' property of the item it received to 'Rented', instead it was initialized to '{book.status}'"
        assert book.value == 95, "The `rent_item` method of the Store class did not invoke the use() method of the item it received and/or did not decrease its value"
        assert len(client.rented_items) == 1, "The `rent_item` method of the Store class did not push the item it received to the `rented_items` list of the client it receives"
        assert isinstance(client.rented_items[0], Book), "The `rent_item` method of the Store class did not push the item it received to the `rented_items` list of the client it receives"

        book2 = Book('Elevation 2', 'Jona', 100)
        book2.status = 'Destroyed'
        store.rent_item(book2, client)
        assert len(client.rented_items) == 1, "The `rent_item` method of the Store class should NOT push the item to the `rented_items` list of the client it receives if the item's status is not 'Available'"
        assert book2.value == 100, "The `rent_item` method of the Store class should NOT invoke the use() method of the item it receives and NOT decrease the value of the item if the item's status is not 'Available'"
        assert book2.status == 'Destroyed', "The `rent_item` method of the Store class should NOT change the item's status to 'Rented' if the item's status is not 'Available'"

        # return_item() Tests
        store.return_item(book)
        book.status = book.status.lower()
        assert book.status == 'available', "The `return_item` method of the Store class should change the `status` of the item it receives to 'Available' if it's value is greater than 0"
        assert len(client.rented_items) == 0, "The `rent_item` method of the Store class  did not remove the item it received from the client's `rented_items` list"

        store.rent_item(book, client)
        book.value = 0
        store.return_item(book)
        book.status = book.status.lower()
        assert book.status == 'in repair', "The `return_item` method of the Store class did not change the `status` of the item it received to 'In Repair' when it's value is 0"

      except Exception as e:
        assert False, f'{e}'