
class GroceryPOS:
    def __init__(self):
        self.total = 0
        self.inventory = []

    def addToTotal(self, item):

        self.total += item

    def removeFromTotal(self, item):

        self.total -= item

    def chooseSpecificItem(self, choice):
        return choice

    def addSpecificItemToTotal(self, name):
        for inventoryItem in self.inventory:
            if inventoryItem.name == name:
                self.addToTotal(inventoryItem.price)

    def removeSpecificItemFromTotal(self, name):
        self.total -= 5

    def fillInventory(self):

        apple = InventoryItem('apple', 5)
        grapes = InventoryItem('grapes', 3)
        banana = InventoryItem('banana', 4)

        self.inventory.append(apple)
        self.inventory.append(grapes)
        self.inventory.append(banana)



class InventoryItem:

    def __init__(self, name, price):
        self.name = name
        self.price = price