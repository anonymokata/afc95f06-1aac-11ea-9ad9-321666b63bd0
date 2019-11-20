import unittest
from GroceryPOS import GroceryPOS

class groceryPOSTest(unittest.TestCase):


    def setUp(self):

        self.grocery = GroceryPOS()
        self.grocery.fillInventory()

    def testNoTotal(self):

        self.assertEqual(self.grocery.total, 0)


    def testAddToTotal(self):

        # adds 5 to total
        self.grocery.addToTotal(5)
        self.assertEqual(self.grocery.total, 5)
        # adds 5 more to total
        self.grocery.addToTotal(5)
        self.assertEqual(self.grocery.total, 10)
        # adds 10 to total
        self.grocery.addToTotal(10)
        self.assertEqual(self.grocery.total, 20)



    def testRemoveFromTotal(self):

        # removes 5 from total
        self.grocery.removeFromTotal(5)
        self.assertEqual(self.grocery.total, -5)
        # removes 5 from total
        self.grocery.removeFromTotal(5)
        self.assertEqual(self.grocery.total, -10)
        # removes 10 from total
        self.grocery.removeFromTotal(10)
        self.assertEqual(self.grocery.total, -20)


    def testChooseSpecificItemFromCart(self):

        print('testChooseSpecificItemFromCart')

        # tests adding apple to cart and choosing item from list
        self.grocery.addItemToCart('Apple')
        item = self.grocery.chooseSpecificItemFromCart('Apple')
        self.assertEqual(item.name, 'Apple')
        # tests adding grapes to cart and choosing item from list
        self.grocery.addItemToCart('Grapes')
        item = self.grocery.chooseSpecificItemFromCart('Grapes')
        self.assertEqual(item.name, 'Grapes')
        # tests adding banana to cart and choosing item from list
        self.grocery.addItemToCart('Banana')
        item = self.grocery.chooseSpecificItemFromCart('Banana')
        self.assertEqual(item.name, 'Banana')


    def testAddSpecificItemToTotal(self):

        print('testAddSpecificItemToTotal')
        # 2 lbs of apples
        self.grocery.addItemToCart('Apple')
        self.assertEqual(self.grocery.total, 8)
        # 3 lbs of grapes
        self.grocery.addItemToCart('Grapes')
        self.assertEqual(self.grocery.total, 17)
        # 1 butter
        self.grocery.addItemToCart('Butter')
        self.assertEqual(self.grocery.total, 20.00)


    def testRemoveSpecificItemFromTotal(self):

        print('testRemoveSpecificItemFromTotal')
        # add and remove 2 lbs of apples
        self.grocery.addItemToCart('Apple')
        item = self.grocery.chooseSpecificItemFromCart('Apple')
        self.grocery.removeSpecificItemFromTotal(item)
        self.assertEqual(self.grocery.total, 0)

        # add and remove 3 lbs of grapes
        self.grocery.addItemToCart('Grapes')
        item = self.grocery.chooseSpecificItemFromCart('Grapes')
        self.grocery.removeSpecificItemFromTotal(item)
        self.assertEqual(self.grocery.total, 0)

        # add and remove 1 butter
        self.grocery.addItemToCart('Butter')
        item = self.grocery.chooseSpecificItemFromCart('Butter')
        self.grocery.removeSpecificItemFromTotal(item)
        self.assertEqual(self.grocery.total, 0)

    def testAddItemToCart(self):

        print('testAddItemToCart')
        # adds 2 lb of apples
        self.grocery.addItemToCart('Apple')
        self.assertEqual(len(self.grocery.cart), 1)
        self.assertEqual(self.grocery.cart[0].name, 'Apple')

        # this tests when another object with pounds is added only one object will remain in the list
        # adds 2 more pounds of apples
        self.grocery.addItemToCart('Apple')
        self.assertEqual(len(self.grocery.cart), 1)
        self.assertEqual(self.grocery.total, 16)



    def testRemoveItemFromCart(self):

        print('testRemoveItemFromCart')
        self.grocery.addItemToCart('Apple')
        self.assertEqual(self.grocery.cart[0].name, 'Apple')
        self.grocery.removeItemFromCart('Apple')
        self.assertEqual(len(self.grocery.cart), 0)

        # this tests that an item thats tried to be removed from an empty cart catches the exception
        self.grocery.removeItemFromCart('Apple')
        # this tests that the total does not go negative when an item is removed that is not on the list
        self.assertEqual(self.grocery.total, 0)

        # this tests removing two apple objects from a list that only contains one apple object but still other item objects
        self.grocery.addItemToCart('Apple')
        self.grocery.addItemToCart('Banana')
        self.grocery.addItemToCart('Grapes')
        self.grocery.removeItemFromCart('Apple')
        self.grocery.removeItemFromCart('Apple')


    # I think check units is being called twice but dont know how to run test without it since its in my add to cart
    def testCheckUnits(self):

        print('testCheckUnits')

        # add 2 pounds of apples make sure units are kept correct
        self.assertEqual(self.grocery.addItemToCart('Apple'), 2)

        # adds 1 butter to make sure units are kept correct
        self.assertEqual(self.grocery.addItemToCart('Butter'), 1)

    def testCheckSpecialty(self):

        print('testCheckSpecialty')
        # this tests the bogo specialty that when two butters are added
        self.grocery.addItemToCart('Butter')
        self.assertEqual(self.grocery.total, 3)
        self.grocery.addItemToCart('Butter')
        self.assertEqual(self.grocery.total, 3)
        self.assertEqual(len(self.grocery.cart), 2)

        # this tests the bogo when three butters are added
        self.grocery.addItemToCart('Butter')
        self.assertEqual(self.grocery.total, 6)

        # this tests the bogo when four butters are added
        self.grocery.addItemToCart('Butter')
        self.assertEqual(self.grocery.total, 6)





if __name__ == '__main__':
    unittest.main()

