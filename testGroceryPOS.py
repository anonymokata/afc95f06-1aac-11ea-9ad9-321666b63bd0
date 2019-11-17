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

    def testChooseSpecifcItem(self):

        self.grocery.addItemToCart('Apple')
        item = self.grocery.chooseSpecificItem('Apple')
        self.assertEqual(item.name, 'Apple')
        self.grocery.addItemToCart('Grapes')
        item = self.grocery.chooseSpecificItem('Grapes')
        self.assertEqual(item.name, 'Grapes')
        self.grocery.addItemToCart('Banana')
        item = self.grocery.chooseSpecificItem('Banana')
        self.assertEqual(item.name, 'Banana')

    def testAddSpecificItemToTotal(self):

        # 2 lbs of apples
        self.grocery.addItemToCart('Apple')
        self.grocery.addSpecificItemToTotal('Apple')
        self.assertEqual(self.grocery.total, 10)
        # 3 lbs of grapes
        self.grocery.addItemToCart('Grapes')
        self.grocery.addSpecificItemToTotal('Grapes')
        self.assertEqual(self.grocery.total, 19)
        # 1 butter
        self.grocery.addItemToCart('Butter')
        self.grocery.addSpecificItemToTotal('Butter')
        self.assertEqual(self.grocery.total, 22.19)

    def testRemoveSpecificItemFromTotal(self):

        self.grocery.removeSpecificItemFromTotal('Apple')
        self.assertEqual(self.grocery.total, -5)
        self.grocery.removeSpecificItemFromTotal('Grapes')
        self.assertEqual(self.grocery.total, -8)
        self.grocery.removeSpecificItemFromTotal('Banana')
        self.assertEqual(self.grocery.total, -12)

 #I want to create a cart attribute on grocery that will append the scanned item in and pop that
# item when removed that way items cannot be scanned out more than once, and the balance will never be negative.

    def testAddItemToCart(self):

        self.grocery.addItemToCart('Apple')
        self.assertEqual(len(self.grocery.cart), 1)
        self.assertEqual(self.grocery.cart[0].name, 'Apple')

    def testRemoveItemFromCart(self):

        self.grocery.addItemToCart('Apple')
        self.assertEqual(self.grocery.cart[0].name, 'Apple')
        self.grocery.removeItemFromCart('Apple')
        self.assertEqual(len(self.grocery.cart), 0)
        self.grocery.removeItemFromCart('Apple')
        self.assertEqual(self.grocery.total, 0)
        self.grocery.addItemToCart('Apple')
        self.grocery.addItemToCart('Banana')
        self.grocery.addItemToCart('Grapes')
        self.grocery.removeItemFromCart('Apple')
        self.grocery.removeItemFromCart('Apple')

    def testCheckUnits(self):

        self.grocery.addItemToCart('Apple')
        item = self.grocery.chooseSpecificItem('Apple')
        self.assertEqual(self.grocery.checkUnits(item), 2)
        self.grocery.addItemToCart('Butter')
        item = self.grocery.chooseSpecificItem('Butter')
        self.assertEqual(self.grocery.checkUnits(item), 1)


if __name__ == '__main__':
    unittest.main()

