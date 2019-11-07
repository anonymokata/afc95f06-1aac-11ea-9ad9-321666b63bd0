import unittest
from GroceryPOS import GroceryPOS

class groceryPOSTest(unittest.TestCase):


    def setUp(self):

        self.grocery = GroceryPOS()

    def testNoTotal(self):

        self.assertEqual(self.grocery.total, 0)

    def testAddToTotal(self):

        self.grocery.addToTotal()
        self.assertEqual(self.grocery.total, 5)


    def testRemoveFromTotal(self):

        self.grocery.removeFromTotal()
        self.assertEqual(self.grocery.total, -5)


if __name__ == '__main__':
    unittest.main()
