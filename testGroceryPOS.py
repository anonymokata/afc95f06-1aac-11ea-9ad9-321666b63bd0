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

    def testRemoveSpecificItemFromTotal(self):

        self.grocery.removeSpecificItemFromTotal('apple')
        self.assertEqual(self.grocery.total, -5)
        self.grocery.removeSpecificItemFromTotal('grapes')
        self.assertEqual(self.grocery.total, -8)
        self.grocery.removeSpecificItemFromTotal('banana')
        self.assertEqual(self.grocery.total, -12)

 #I want to create a cart attribute on grocery that will append the scanned item in and pop that
# item when removed that way items cannot be scanned out more than once, and the balance will never be negative.
    def testAddItemToCart(self):

        self.grocery.addItemToCart('apple')
        self.assertEqual(self.grocery.cart[0].name, 'apple')

    def testRemoveItemFromCart(self):

        self.grocery.addItemToCart('apple')
        self.assertEqual(self.grocery.cart[0].name, 'apple')
        self.grocery.removeItemFromCart('apple')
        self.assertEqual(len(self.grocery.cart), 0)
        self.grocery.removeItemFromCart(('apple'))
        self.assertEqual(self.grocery.total, 0)
        self.grocery.addItemToCart('apple')
        self.grocery.addItemToCart('banana')
        self.grocery.addItemToCart('grapes')
        self.grocery.removeItemFromCart('apple')
        self.grocery.removeItemFromCart('apple')




if __name__ == '__main__':
    unittest.main()
