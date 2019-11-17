import xlrd

class GroceryPOS:
    def __init__(self):
        self.total = 0
        self.inventory = []
        self.cart = []

    def addToTotal(self, item):

        self.total += item

    def removeFromTotal(self, item):

        self.total -= item

    def chooseSpecificItem(self, choice):
        for item in self.cart:
            if item.name == choice:
                return item


    def addSpecificItemToTotal(self, name):
        for inventoryItem in self.cart:
            if inventoryItem.name == name:
                units = self.checkUnits(inventoryItem)
                self.addToTotal((inventoryItem.price - inventoryItem.markdown) * units)

    def removeSpecificItemFromTotal(self, name):
        for inventoryItem in self.cart:
            if inventoryItem.name == name:
                units = self.checkUnits(inventoryItem)
                self.removeFromTotal((inventoryItem.price - inventoryItem.markdown) * units)

    def addItemToCart(self, name):
        for inventoryItem in self.inventory:
            if inventoryItem.name == name:
                self.cart.append(inventoryItem)


    def removeItemFromCart(self, name):
        if len(self.cart) == 0:
            print('There are no items in your cart')

        else:
            scannedItem = ''
            try:
                for inventoryItem in self.inventory:
                    if inventoryItem.name == name:
                        scannedItem = inventoryItem.name
                        self.cart.remove(inventoryItem)

            except ValueError:
                print(f'There is no {scannedItem} in your cart')

    def checkUnits(self, inventoryItem):

        if inventoryItem.units == 'lb':
            quantity = int(input('How many pounds?'))
            return quantity
        elif inventoryItem.units == 'sku':
            return 1


    def generateItem(self, name, price, units, markdown):
        return InventoryItem(name, price, units, markdown)

    def fillInventory(self):

        loc = ('/Users/shawnzanders/PycharmProjects/theForgeCodeKata/GroceryExcel/GroceryInventory.xlsx')

        wb = xlrd.open_workbook(loc)
        sheet = wb.sheet_by_index(0)

        sheet.cell_value(0, 0)

        for i in range(sheet.nrows):
            name = sheet.cell_value(i, 1)
            price = sheet.cell_value(i, 2)
            units = sheet.cell_value(i, 3)
            markdown = sheet.cell_value(i, 4)
            item = self.generateItem(name, price, units, markdown)
            self.inventory.append(item)



class InventoryItem:

    def __init__(self, name, price, units, markdown):
        self.name = name
        self.price = price
        self.units = units
        self.markdown = markdown

