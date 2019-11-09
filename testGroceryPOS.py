import unittest
from GroceryPOS import GroceryPOS

class groceryPOSTest(unittest.TestCase):


    def setUp(self):

        self.grocery = GroceryPOS()

    def testNoTotal(self):

        self.assertEqual(self.grocery.total, 0)

    def testAddToTotal(self):

        self.grocery.addToTotal(5)
        self.assertEqual(self.grocery.total, 5)
        self.grocery.addToTotal(5)
        self.assertEqual(self.grocery.total, 10)
        self.grocery.addToTotal(10)
        self.assertEqual(self.grocery.total, 20)


    def testRemoveFromTotal(self):

        self.grocery.removeFromTotal(5)
        self.assertEqual(self.grocery.total, -5)
        self.grocery.removeFromTotal(5)
        self.assertEqual(self.grocery.total, -10)
        self.grocery.removeFromTotal(10)
        self.assertEqual(self.grocery.total, -20)



if __name__ == '__main__':
    unittest.main()
