import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from storage import Storage
 
class TestStore(unittest.TestCase):
    def setUp(self):
        self.storage = Storage("test.pkl")
 
    def test_save_and_load(self):
        data = ["Test Employee"]
        self.storage.save(data)
        loaded_data = self.storage.load()
        self.assertEqual(loaded_data, data)
 
if __name__ == "__main__":
    unittest.main()