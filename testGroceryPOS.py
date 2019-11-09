import unittest
from GroceryPOS import GroceryPOS

class groceryPOSTest(unittest.TestCase):


    def setUp(self):

        self.grocery = GroceryPOS()
        self.grocery.fillInventory()

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

    def testChooseSpecificItem(self):


        self.assertEqual(self.grocery.chooseSpecificItem('apple'), 'apple')
        self.assertEqual(self.grocery.chooseSpecificItem('grapes'), 'grapes')
        self.assertEqual(self.grocery.chooseSpecificItem('banana'), 'banana')

    def testAddSpecificItemToTotal(self):

        self.grocery.addSpecificItemToTotal('apple')
        self.assertEqual(self.grocery.total, 5)
        self.grocery.addSpecificItemToTotal('grapes')
        self.assertEqual(self.grocery.total, 8)
        self.grocery.addSpecificItemToTotal('banana')
        self.assertEqual(self.grocery.total, 12)




if __name__ == '__main__':
    unittest.main()
