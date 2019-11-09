
class GroceryPOS:
    def __init__(self):
        self.total = 0

    def addToTotal(self, item):

        self.total += item

    def removeFromTotal(self, item):

        self.total -= item

    def chooseSpecificItem(self):

        return 'apple'