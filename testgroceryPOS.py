import unittest
from GroceryPOS import GroceryPOS

class groceryPOSTest(unittest.TestCase):

    def setUp(self):
        self.grocery = GroceryPOS()

    def testNoTotal(self):

        self.assertEqual(self.grocery.total,0)
