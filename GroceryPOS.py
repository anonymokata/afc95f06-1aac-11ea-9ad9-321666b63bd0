
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
        self.total += 5

