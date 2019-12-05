import unittest
from GroceryPOS import GroceryPOS

class groceryPOSTest(unittest.TestCase):


    def setUp(self):

        self.grocery = GroceryPOS()
        self.grocery.fillInventory()

    # def testNoTotal(self):
    #
    #     self.assertEqual(self.grocery.total, 0)
    #
    #
    # def testAddToTotal(self):
    #
    #     # adds 5 to total
    #     self.grocery.addToTotal(5)
    #     self.assertEqual(self.grocery.total, 5)
    #     # adds 5 more to total
    #     self.grocery.addToTotal(5)
    #     self.assertEqual(self.grocery.total, 10)
    #     # adds 10 to total
    #     self.grocery.addToTotal(10)
    #     self.assertEqual(self.grocery.total, 20)
    #
    #
    #
    # def testRemoveFromTotal(self):
    #
    #     # removes 5 from total
    #     self.grocery.removeFromTotal(5)
    #     self.assertEqual(self.grocery.total, -5)
    #     # removes 5 from total
    #     self.grocery.removeFromTotal(5)
    #     self.assertEqual(self.grocery.total, -10)
    #     # removes 10 from total
    #     self.grocery.removeFromTotal(10)
    #     self.assertEqual(self.grocery.total, -20)
    #
    #
    # def testChooseSpecificItemFromCart(self):
    #
    #     print('testChooseSpecificItemFromCart')
    #
    #     # tests adding apple to cart and choosing item from list
    #     self.grocery.addItemToCart('apple')
    #     item = self.grocery.chooseSpecificItemFromCart('apple')
    #     self.assertEqual(item.name, 'apple')
    #     # tests adding grapes to cart and choosing item from list
    #     self.grocery.addItemToCart('grape')
    #     item = self.grocery.chooseSpecificItemFromCart('grape')
    #     self.assertEqual(item.name, 'grape')
    #     # tests adding banana to cart and choosing item from list
    #     self.grocery.addItemToCart('banana')
    #     item = self.grocery.chooseSpecificItemFromCart('banana')
    #     self.assertEqual(item.name, 'banana')


    # def testAddSpecificItemToTotal(self):
    #
    #     print('testAddSpecificItemToTotal')
    #     # 2 lbs of blueberry
    #     self.grocery.addItemToCart('blueberry')
    #     self.assertEqual(self.grocery.total, 4)
    #     # 3 lbs of raspberry
    #     self.grocery.addItemToCart('raspberry')
    #     self.assertEqual(self.grocery.total, 10)
    #     # 1 butter
    #     self.grocery.addItemToCart('butter')
    #     self.assertEqual(self.grocery.total, 13)

    # def testAddItemToCart(self):
    #
    #     print('testAddItemToCart')
    #     # adds 2 lb of apples
    #     self.grocery.addItemToCart('apple')
    #     self.assertEqual(len(self.grocery.cart), 1)
    #     self.assertEqual(self.grocery.cart[0].name, 'apple')
    #
    #     # this tests when another object with pounds is added only one object will remain in the list
    #     # adds 2 more pounds of apples
    #     self.grocery.addItemToCart('apple')
    #     self.assertEqual(len(self.grocery.cart), 1)
    #     self.assertEqual(self.grocery.total, 8)
    #
    #
    #
    # def testRemoveItemFromCart(self):
    #
    #     print('testRemoveItemFromCart')
    #     self.grocery.addItemToCart('apple')
    #     self.assertEqual(self.grocery.cart[0].name, 'apple')
    #     self.grocery.removeItemFromCart('apple')
    #     self.assertEqual(len(self.grocery.cart), 0)
    #
    #     # this tests that an item thats tried to be removed from an empty cart catches the exception
    #     self.grocery.removeItemFromCart('apple')
    #     # this tests that the total does not go negative when an item is removed that is not on the list
    #     self.assertEqual(self.grocery.total, 0)
    #
    #     # this tests removing two apple objects from a list that only contains one apple object but still other item objects
    #     self.grocery.addItemToCart('apple')
    #     self.grocery.addItemToCart('banana')
    #     self.grocery.addItemToCart('grape')
    #     self.grocery.removeItemFromCart('apple')
    #     self.grocery.removeItemFromCart('apple')

    # def testCheckUnits(self):
    #
    #     print('testCheckUnits')
    #
    #     # add 2 pounds of apples make sure units are kept correct
    #     self.grocery.addItemToCart('apple')
    #     self.assertEqual(self.grocery.cart[0].quantity, 2)
    #
    #     # adds 1 butter to make sure units are kept correct
    #     self.grocery.addItemToCart('butter')
    #     self.assertEqual(self.grocery.cart[1].quantity, 1)


    def testCheckBogo(self):

        print('testCheckBogo')

        # # this tests the bogo specialty that when one butter is added
        # self.grocery.addItemToCart('butter')
        # self.assertEqual(self.grocery.total, 3)
        #
        # # this tests the bogo specialty that when one butter is added
        # # this is a specialty case
        # self.grocery.addItemToCart('butter')
        # self.assertEqual(self.grocery.total, 3)
        # self.assertEqual(len(self.grocery.cart), 2)
        #
        # # this tests the bogo specialty that when one butter is added
        # self.grocery.addItemToCart('butter')
        # self.assertEqual(self.grocery.total, 6)
        #
        # # this tests the bogo specialty that when one butter is added
        # # this is a specialty case
        # self.grocery.addItemToCart('butter')
        # self.assertEqual(self.grocery.total, 6)
        #
        # # this tests when a butter is removed that it functions properly
        # self.grocery.removeItemFromCart('butter')
        # self.assertEqual(self.grocery.total, 6)
        #
        # # this tests when a butter is removed that it functions properly
        # self.grocery.removeItemFromCart('butter')
        # self.assertEqual(self.grocery.total, 3)
        #
        # # this tests when a butter is removed that it functions properly
        # self.grocery.removeItemFromCart('butter')
        # self.assertEqual(self.grocery.total, 3)
        #
        # # this tests the bogo specialty that when one butter is added
        # self.grocery.addItemToCart('butter')
        # self.assertEqual(self.grocery.total, 3)
        #
        # # this tests the bogo specialty that when one butter is added
        # self.grocery.addItemToCart('butter')
        # self.assertEqual(self.grocery.total, 6)
        #
        # # this tests the bogo limit of 6 by adding 4 butters
        # self.grocery.addItemToCart('butter')
        # self.assertEqual(self.grocery.total, 6)
        # self.grocery.addItemToCart('butter')
        # self.assertEqual(self.grocery.total, 9)
        # self.grocery.addItemToCart('butter')
        # self.assertEqual(self.grocery.total, 9)
        # self.grocery.addItemToCart('butter')
        # self.assertEqual(self.grocery.total, 12)
        # self.grocery.addItemToCart('butter')
        # self.assertEqual(self.grocery.total, 15)
        # self.grocery.addItemToCart('butter')
        # self.assertEqual(self.grocery.total, 18)
        #
        # #this tests removing sku outside of the limit and that the price is correct
        # self.grocery.removeItemFromCart('butter')
        # self.assertEqual(self.grocery.total, 15)
        # self.grocery.removeItemFromCart('butter')
        # self.assertEqual(self.grocery.total, 12)
        # self.grocery.removeItemFromCart('butter')
        # self.assertEqual(self.grocery.total, 9)
        # self.grocery.removeItemFromCart('butter')
        # self.assertEqual(self.grocery.total, 9)
        # self.grocery.removeItemFromCart('butter')
        # self.assertEqual(self.grocery.total, 6)
        # self.grocery.removeItemFromCart('butter')
        # self.assertEqual(self.grocery.total, 6)

        # # this tests when specialty is given to a per pound object it works as well
        # # this particular test is 1
        # self.grocery.addItemToCart('apple')
        # self.assertEqual(self.grocery.total, 4)
        #
        # # this particular test is 1
        # self.grocery.addItemToCart('apple')
        # self.assertEqual(self.grocery.total, 4)
        #
        # # this tests when more apples are added it still responds appropriately
        # # 1 more pound of apples will be added
        # self.grocery.addItemToCart('apple')
        # self.assertEqual(self.grocery.total, 8)
        #
        # # this tests when more apples are added it still responds appropriately
        # # 1 more pound of apples will be added
        # self.grocery.addItemToCart('apple')
        # self.assertEqual(self.grocery.total, 8)
        #
        # # tests that 2 lb of apples can be added
        # self.grocery.addItemToCart('apple')
        # self.assertEqual(self.grocery.total, 12)
        #
        # # adds 2 more lb of apples to check limit testing
        # self.grocery.addItemToCart('apple')
        # self.assertEqual(self.grocery.total, 20)
        #
        # # tests removes apple object and corrects price
        # self.grocery.removeItemFromCart('apple')
        # self.assertEqual(self.grocery.total, 0)
        #
        # # adds odd number of bogo lbs (5)
        # self.grocery.addItemToCart('apple')
        # self.assertEqual(self.grocery.total, 12)

    def testCheckNforX(self):

        print('testCheckNforX')

        # # tests n for x (this particular test was 3 for 10)
        # self.grocery.addItemToCart('bacon')
        # self.assertEqual(self.grocery.total, 4)
        # self.grocery.addItemToCart('bacon')
        # self.assertEqual(self.grocery.total, 8)
        # self.grocery.addItemToCart('bacon')
        # self.assertEqual(self.grocery.total, 10)
        #
        # # this tests when one is removed it responds correctly
        # self.grocery.removeItemFromCart('bacon')
        # self.assertEqual(self.grocery.total, 8)
        #
        # # this tests when one is removed it responds correctly
        # self.grocery.removeItemFromCart('bacon')
        # self.assertEqual(self.grocery.total, 4)
        #
        # # this tests when one is added back
        # self.grocery.addItemToCart('bacon')
        # self.assertEqual(self.grocery.total, 8)
        #
        # self.grocery.addItemToCart('bacon')
        # self.assertEqual(self.grocery.total, 10)
        #
        # # tests three more with checks on non qualifying amounts
        # self.grocery.addItemToCart('bacon')
        # self.assertEqual(self.grocery.total, 14)
        #
        # # this tests one addition to the total
        # self.grocery.addItemToCart('bacon')
        # self.assertEqual(self.grocery.total, 18)
        #
        # # this tests when one is removed it responds correctly
        # self.grocery.removeItemFromCart('bacon')
        # self.assertEqual(self.grocery.total, 14)
        #
        # # this tests when one is added back
        # self.grocery.addItemToCart('bacon')
        # self.assertEqual(self.grocery.total, 18)
        # self.grocery.addItemToCart('bacon')
        # self.assertEqual(self.grocery.total, 20)
        #
        # # this tests when one is removed it responds correctly
        # self.grocery.removeItemFromCart('bacon')
        # self.assertEqual(self.grocery.total, 18)
        #
        # # this tests when one is removed it responds correctly
        # self.grocery.removeItemFromCart('bacon')
        # self.assertEqual(self.grocery.total, 14)
        #
        # # this tests when one is removed it responds correctly
        # self.grocery.removeItemFromCart('bacon')
        # self.assertEqual(self.grocery.total, 10)
        #
        # # tests that adding it back works
        # self.grocery.addItemToCart('bacon')
        # self.assertEqual(self.grocery.total, 14)
        #
        # # tests that adding it back works
        # self.grocery.addItemToCart('bacon')
        # self.assertEqual(self.grocery.total, 18)
        #
        # # tests that adding it back works
        # self.grocery.addItemToCart('bacon')
        # self.assertEqual(self.grocery.total, 20)
        #
        # # this tests the limit of 6
        # self.grocery.addItemToCart('bacon')
        # self.assertEqual(self.grocery.total, 24)
        # self.grocery.addItemToCart('bacon')
        # self.assertEqual(self.grocery.total, 28)
        # self.grocery.addItemToCart('bacon')
        # self.assertEqual(self.grocery.total, 30)
        # self.grocery.addItemToCart('bacon')
        # self.assertEqual(self.grocery.total, 34)
        # self.grocery.addItemToCart('bacon')
        # self.assertEqual(self.grocery.total, 38)
        # self.grocery.addItemToCart('bacon')
        # self.assertEqual(self.grocery.total, 42)
        #
        # #this tests removing sku outside of the limit and that the price is correct
        # self.grocery.removeItemFromCart('bacon')
        # self.assertEqual(self.grocery.total, 38)
        # self.grocery.removeItemFromCart('bacon')
        # self.assertEqual(self.grocery.total, 34)
        # self.grocery.removeItemFromCart('bacon')
        # self.assertEqual(self.grocery.total, 30)
        # self.grocery.removeItemFromCart('bacon')
        # self.assertEqual(self.grocery.total, 28)
        # self.grocery.removeItemFromCart('bacon')
        # self.assertEqual(self.grocery.total, 24)

        # # this tests when specialty is given to a per pound object it works as well
        # # this test is 1
        # self.grocery.addItemToCart('grape')
        # self.assertEqual(self.grocery.total, 3)
        #
        # # this tests when more grapes are added it still responds appropriately
        # # 1 more pounds of grapes will be added
        # self.grocery.addItemToCart('grape')
        # self.assertEqual(self.grocery.total, 6)
        #
        # # 1 more pounds of grapes will be added
        # self.grocery.addItemToCart('grape')
        # self.assertEqual(self.grocery.total, 8)
        #
        # # 1 more pounds of grapes will be added
        # self.grocery.addItemToCart('grape')
        # self.assertEqual(self.grocery.total, 11)
        #
        # # 1 more pounds of grapes will be added
        # self.grocery.addItemToCart('grape')
        # self.assertEqual(self.grocery.total, 14)
        #
        # # 1 more pounds of grapes will be added
        # self.grocery.addItemToCart('grape')
        # self.assertEqual(self.grocery.total, 16)
        #
        # # # this tests when more grapes are added it still responds appropriately
        # # # 2 more pounds of grapes will be added
        # # self.grocery.addItemToCart('grape')
        # # self.assertEqual(self.grocery.total, 16)
        #
        # # 1 more pounds of grapes will be added
        # self.grocery.addItemToCart('grape')
        # self.assertEqual(self.grocery.total, 19)
        #
        # # 1 more pounds of grapes will be added
        # self.grocery.addItemToCart('grape')
        # self.assertEqual(self.grocery.total, 22)
        #
        # # 1 more pounds of grapes will be added
        # self.grocery.addItemToCart('grape')
        # self.assertEqual(self.grocery.total, 24)
        #
        # # 1 more pounds of grapes will be added
        # # this tests the limits
        # self.grocery.addItemToCart('grape')
        # self.assertEqual(self.grocery.total, 27)
        #
        # # 1 more pounds of grapes will be added
        # self.grocery.addItemToCart('grape')
        # self.assertEqual(self.grocery.total, 30)
        #
        # # 1 more pounds of grapes will be added
        # self.grocery.addItemToCart('grape')
        # self.assertEqual(self.grocery.total, 33)
        #
        # # tests removing the grape item/object
        # self.grocery.removeItemFromCart('grape')
        # self.assertEqual(self.grocery.total, 0)

    def testNMatX(self):

        print('testNMatX')

        # # add 1 milks
        # self.grocery.addItemToCart('milk')
        # self.assertEqual(self.grocery.total, 3)
        #
        # # tests remove 1 milk
        # self.grocery.removeItemFromCart('milk')
        # self.assertEqual(self.grocery.total, 0)
        #
        # # test adds two milks
        # self.grocery.addItemToCart('milk')
        # self.assertEqual(self.grocery.total, 3)
        # self.grocery.addItemToCart('milk')
        # self.assertEqual(self.grocery.total, 6)
        #
        # # tests remove milk
        # self.grocery.removeItemFromCart('milk')
        # self.assertEqual(self.grocery.total, 3)
        #
        # # tests 2 milks added
        # self.grocery.addItemToCart('milk')
        # self.assertEqual(self.grocery.total, 6)
        # self.grocery.addItemToCart('milk')
        # self.assertEqual(self.grocery.total, 7.50)
        #
        # # removes 1 milk
        # self.grocery.removeItemFromCart('milk')
        # self.assertEqual(self.grocery.total, 6)
        #
        # self.grocery.addItemToCart('milk')
        # self.assertEqual(self.grocery.total, 7.50)
        #
        # # tests remove milk
        # self.grocery.removeItemFromCart('milk')
        # self.assertEqual(self.grocery.total, 6)
        #
        # # tests one more milk
        # self.grocery.addItemToCart('milk')
        # self.assertEqual(self.grocery.total, 7.50)
        #
        # # tests one more milk
        # self.grocery.addItemToCart('milk')
        # self.assertEqual(self.grocery.total, 10.50)
        #
        # # tests one more milk
        # self.grocery.addItemToCart('milk')
        # self.assertEqual(self.grocery.total, 13.50)
        #
        # # removes 1 milk
        # self.grocery.removeItemFromCart('milk')
        # self.assertEqual(self.grocery.total, 10.50)
        #
        # # tests one more milk
        # self.grocery.addItemToCart('milk')
        # self.assertEqual(self.grocery.total, 13.50)
        #
        # # test one more milk this should be another nmatx
        # self.grocery.addItemToCart('milk')
        # self.assertEqual(self.grocery.total, 15)
        #
        # # removes 1 milk
        # self.grocery.removeItemFromCart('milk')
        # self.assertEqual(self.grocery.total, 13.50)
        #
        # # tests one more milk
        # self.grocery.addItemToCart('milk')
        # self.assertEqual(self.grocery.total, 15)
        #
        # # this tests the limit of 6
        # self.grocery.addItemToCart('milk')
        # self.assertEqual(self.grocery.total, 18)
        # self.grocery.addItemToCart('milk')
        # self.assertEqual(self.grocery.total, 21)
        # self.grocery.addItemToCart('milk')
        # self.assertEqual(self.grocery.total, 22.50)
        # self.grocery.addItemToCart('milk')
        # self.assertEqual(self.grocery.total, 25.50)
        # self.grocery.addItemToCart('milk')
        # self.assertEqual(self.grocery.total, 28.50)
        # self.grocery.addItemToCart('milk')
        # self.assertEqual(self.grocery.total, 31.50)
        #
        # #this tests removing sku outside of the limit and that the price is correct
        # self.grocery.removeItemFromCart('milk')
        # self.assertEqual(self.grocery.total, 28.50)
        # self.grocery.removeItemFromCart('milk')
        # self.assertEqual(self.grocery.total, 25.50)
        # self.grocery.removeItemFromCart('milk')
        # self.assertEqual(self.grocery.total, 22.50)
        # self.grocery.removeItemFromCart('milk')
        # self.assertEqual(self.grocery.total, 21)
        # self.grocery.removeItemFromCart('milk')
        # self.assertEqual(self.grocery.total, 18)

        # this tests 1 lb of banana
        self.grocery.addItemToCart('banana')
        self.assertEqual(self.grocery.total, 3)

        # this particular test is 1 Banana
        self.grocery.addItemToCart('banana')
        self.assertEqual(self.grocery.total, 6)

        # this particular test is 1 Banana
        self.grocery.addItemToCart('banana')
        self.assertEqual(self.grocery.total, 9)

        # this test when 1 lb is added this is specialty
        self.grocery.addItemToCart('banana')
        self.assertEqual(self.grocery.total, 10.50)

        # this tests when 1 lb are added
        self.grocery.addItemToCart('banana')
        self.assertEqual(self.grocery.total, 13.50)

        # this tests when 1 lb are added
        self.grocery.addItemToCart('banana')
        self.assertEqual(self.grocery.total, 16.50)

        # 1 more pounds of banana will be added
        self.grocery.addItemToCart('banana')
        self.assertEqual(self.grocery.total, 19.50)

        # 1 more pounds of banana will be added
        self.grocery.addItemToCart('banana')
        self.assertEqual(self.grocery.total, 21)

        # 1 more pounds of banana will be added
        self.grocery.addItemToCart('banana')
        self.assertEqual(self.grocery.total, 24)

        # 1 more pounds of banana will be added
        self.grocery.addItemToCart('banana')
        self.assertEqual(self.grocery.total, 27)

        # 1 more pounds of banana will be added
        self.grocery.addItemToCart('banana')
        self.assertEqual(self.grocery.total, 30)

        # 1 more pounds of banana will be added
        self.grocery.addItemToCart('banana')
        self.assertEqual(self.grocery.total, 31.50)

        # 1 more pounds of banana will be added
        self.grocery.addItemToCart('banana')
        self.assertEqual(self.grocery.total, 34.50)

        # 1 more pounds of banana will be added
        self.grocery.addItemToCart('banana')
        self.assertEqual(self.grocery.total, 37.50)

        # 1 more pounds of banana will be added
        self.grocery.addItemToCart('banana')
        self.assertEqual(self.grocery.total, 40.50)

        # 1 more pounds of banana will be added
        self.grocery.addItemToCart('banana')
        self.assertEqual(self.grocery.total, 43.50)



if __name__ == '__main__':
    unittest.main()

