import unittest
from GroceryPOS import GroceryPOS

class groceryPOSTest(unittest.TestCase):


    def setUp(self):

        self.grocery = GroceryPOS()
        self.grocery.fillInventory()

    # def testNoTotal(self):
    #
    #     self.assertEqual(self.grocery.total, 0)


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
    #     self.grocery.addItemToCart('Apple')
    #     item = self.grocery.chooseSpecificItemFromCart('Apple')
    #     self.assertEqual(item.name, 'Apple')
    #     # tests adding grapes to cart and choosing item from list
    #     self.grocery.addItemToCart('Grapes')
    #     item = self.grocery.chooseSpecificItemFromCart('Grapes')
    #     self.assertEqual(item.name, 'Grapes')
    #     # tests adding banana to cart and choosing item from list
    #     self.grocery.addItemToCart('Banana')
    #     item = self.grocery.chooseSpecificItemFromCart('Banana')
    #     self.assertEqual(item.name, 'Banana')
    #
    #
    # def testAddSpecificItemToTotal(self):
    #
    #     print('testAddSpecificItemToTotal')
    #     # 2 lbs of apples
    #     self.grocery.addItemToCart('Apple')
    #     self.assertEqual(self.grocery.total, 8)
    #     # 3 lbs of grapes
    #     self.grocery.addItemToCart('Grapes')
    #     self.assertEqual(self.grocery.total, 17)
    #     # 1 butter
    #     self.grocery.addItemToCart('Butter')
    #     self.assertEqual(self.grocery.total, 20.00)
    #
    #
    # def testRemoveSpecificItemFromTotal(self):
    #
    #     print('testRemoveSpecificItemFromTotal')
    #     # add and remove 2 lbs of apples
    #     self.grocery.addItemToCart('Apple')
    #     item = self.grocery.chooseSpecificItemFromCart('Apple')
    #     self.grocery.removeSpecificItemFromTotal(item)
    #     self.assertEqual(self.grocery.total, 0)
    #
    #     # add and remove 3 lbs of grapes
    #     self.grocery.addItemToCart('Grapes')
    #     item = self.grocery.chooseSpecificItemFromCart('Grapes')
    #     self.grocery.removeSpecificItemFromTotal(item)
    #     self.assertEqual(self.grocery.total, 0)
    #
    #     # add and remove 1 butter
    #     self.grocery.addItemToCart('Butter')
    #     item = self.grocery.chooseSpecificItemFromCart('Butter')
    #     self.grocery.removeSpecificItemFromTotal(item)
    #     self.assertEqual(self.grocery.total, 0)
    #
    # def testAddItemToCart(self):
    #
    #     print('testAddItemToCart')
    #     # adds 2 lb of apples
    #     self.grocery.addItemToCart('Apple')
    #     self.assertEqual(len(self.grocery.cart), 1)
    #     self.assertEqual(self.grocery.cart[0].name, 'Apple')
    #
    #     # this tests when another object with pounds is added only one object will remain in the list
    #     # adds 2 more pounds of apples
    #     self.grocery.addItemToCart('Apple')
    #     self.assertEqual(len(self.grocery.cart), 1)
    #     self.assertEqual(self.grocery.total, 16)
    #
    #
    #
    # def testRemoveItemFromCart(self):
    #
    #     print('testRemoveItemFromCart')
    #     self.grocery.addItemToCart('Apple')
    #     self.assertEqual(self.grocery.cart[0].name, 'Apple')
    #     self.grocery.removeItemFromCart('Apple')
    #     self.assertEqual(len(self.grocery.cart), 0)
    #
    #     # this tests that an item thats tried to be removed from an empty cart catches the exception
    #     self.grocery.removeItemFromCart('Apple')
    #     # this tests that the total does not go negative when an item is removed that is not on the list
    #     self.assertEqual(self.grocery.total, 0)
    #
    #     # this tests removing two apple objects from a list that only contains one apple object but still other item objects
    #     self.grocery.addItemToCart('Apple')
    #     self.grocery.addItemToCart('Banana')
    #     self.grocery.addItemToCart('Grapes')
    #     self.grocery.removeItemFromCart('Apple')
    #     self.grocery.removeItemFromCart('Apple')
    #
    #
    # # I think check units is being called twice but dont know how to run test without it since its in my add to cart
    # def testCheckUnits(self):
    #
    #     print('testCheckUnits')
    #
    #     # add 2 pounds of apples make sure units are kept correct
    #     self.grocery.addItemToCart('Apple')
    #     self.assertEqual(self.grocery.cart[0].pounds, 2)
    #
    #     # adds 1 butter to make sure units are kept correct
    #     self.grocery.addItemToCart('Butter')
    #     self.assertEqual(self.grocery.cart[1].pounds, 1)


    def testCheckBogo(self):

        print('testCheckBogo')

        # # this tests the bogo specialty that when one butter is added(count:1)
        # self.grocery.addItemToCart('butter')
        # self.assertEqual(self.grocery.total, 3)
        #
        # # this tests the bogo specialty that when one butter is added(count:2)
        # # this is a specialty case
        # self.grocery.addItemToCart('butter')
        # self.assertEqual(self.grocery.total, 3)
        # self.assertEqual(len(self.grocery.cart), 2)
        #
        # # this tests the bogo specialty that when one butter is added(count:3)
        # self.grocery.addItemToCart('butter')
        # self.assertEqual(self.grocery.total, 6)
        #
        # # this tests the bogo specialty that when one butter is added(count:4)
        # # this is a specialty case
        # self.grocery.addItemToCart('butter')
        # self.assertEqual(self.grocery.total, 6)
        #
        # # this tests when a butter is removed that it functions properly(count:3)
        # self.grocery.removeItemFromCart('butter')
        # self.assertEqual(self.grocery.total, 6)
        #
        # # this tests when a butter is removed that it functions properly(count:2)
        # self.grocery.removeItemFromCart('butter')
        # self.assertEqual(self.grocery.total, 3)
        #
        # # this tests when a butter is removed that it functions properly(count:1)
        # self.grocery.removeItemFromCart('butter')
        # self.assertEqual(self.grocery.total, 3)
        #
        # # this tests the bogo specialty that when one butter is added(count:2)
        # self.grocery.addItemToCart('butter')
        # self.assertEqual(self.grocery.total, 3)
        #
        # # this tests the bogo specialty that when one butter is added(count:3)
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


        # this tests when specialty is given to a per pound object it works as well
        # this particular test is 1
        self.grocery.addItemToCart('apple')
        self.assertEqual(self.grocery.total, 4)

        # this particular test is 1
        self.grocery.addItemToCart('apple')
        self.assertEqual(self.grocery.total, 4)

        # this tests when more apples are added it still responds appropriately
        # 1 more pound of apples will be added
        self.grocery.addItemToCart('apple')
        self.assertEqual(self.grocery.total, 8)

        # this tests when more apples are added it still responds appropriately
        # 1 more pound of apples will be added
        self.grocery.addItemToCart('apple')
        self.assertEqual(self.grocery.total, 8)

        # tests that 2 lb of apples can be added
        self.grocery.addItemToCart('apple')
        self.assertEqual(self.grocery.total, 12)

        # adds 2 more lb of apples to check limit testing
        self.grocery.addItemToCart('apple')
        self.assertEqual(self.grocery.total, 20)

        # removes 1 lb of apples
        self.grocery.removeItemFromCart('apple')
        self.assertEqual(self.grocery.total, 0)

        # adds odd number of bogo lbs (5)
        self.grocery.addItemToCart('apple')
        self.assertEqual(self.grocery.total, 12)




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

        # # this tests when specialty is given to a per pound object it works as well
        # # this particular test is 1
        # self.grocery.addItemToCart('grape')
        # self.assertEqual(self.grocery.total, 3)
        #
        # # this tests when more grapes are added it still responds appropriately
        # # 1 more pounds of grapes will be added
        # self.grocery.addItemToCart('grape')
        # print(self.grocery.total)
        # self.assertEqual(self.grocery.total, 6)
        #
        # # 1 more pounds of grapes will be added
        # self.grocery.addItemToCart('grape')
        # self.assertEqual(self.grocery.total, )
        #
        # # this tests when more grapes are added it still responds appropriately
        # # 3 more pounds of grapes will be added
        # self.grocery.addItemToCart('grape')
        # self.assertEqual(self.grocery.total, )



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
        # # test one more milk this should be another nmatx
        # self.grocery.addItemToCart('milk')
        # self.assertEqual(self.grocery.total, 15)
        #
        # # this tests the limit of 6
        # self.grocery.addItemToCart('milk')
        # self.assertEqual(self.grocery.total, 24)
        # self.grocery.addItemToCart('milk')
        # self.assertEqual(self.grocery.total, 28)
        # self.grocery.addItemToCart('milk')
        # self.assertEqual(self.grocery.total, 30)
        # self.grocery.addItemToCart('milk')
        # self.assertEqual(self.grocery.total, 34)
        # self.grocery.addItemToCart('milk')
        # self.assertEqual(self.grocery.total, 38)
        # self.grocery.addItemToCart('milk')
        # self.assertEqual(self.grocery.total, 42)
    #
    #     # this tests 1 lb of banana
    #     self.grocery.addItemToCart('Banana')
    #     self.assertEqual(self.grocery.total, 2)
    #
    #     # this particular test is 1 Banana
    #     self.grocery.addItemToCart('Banana')
    #     self.assertEqual(self.grocery.total, 4)
    #
    #     # this particular test is 1 Banana
    #     self.grocery.addItemToCart('Banana')
    #     self.assertEqual(self.grocery.total, 6)
    #
    #     # this test when 1 lb is added this is specialty
    #     self.grocery.addItemToCart('Banana')
    #     self.assertEqual(self.grocery.total, 7)
    #
    #     # this tests when 1 lb are added
    #     self.grocery.addItemToCart('Banana')
    #     self.assertEqual(self.grocery.total, 9)
    #
    #     # this tests when 1 lb are added
    #     self.grocery.addItemToCart('Banana')
    #     self.assertEqual(self.grocery.total, 11)
    #
    #     # this tests when more banana are added
    #     # 1 more pounds of banana will be added
    #     self.grocery.addItemToCart('Banana')
    #     self.assertEqual(self.grocery.total, 13)
    #
    #     # 1 more pounds of banana will be added
    #     self.grocery.addItemToCart('Banana')
    #     self.assertEqual(self.grocery.total, 14)


if __name__ == '__main__':
    unittest.main()

