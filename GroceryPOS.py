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

    def checkSpecialty(self, inventoryItem):

        if inventoryItem.hasSpecialty == True:
            return True
        else:
            return False


    def generateItem(self, name, price, units, markdown, hasSpecialty):
        return InventoryItem(name, price, units, markdown, hasSpecialty)

    def fillInventory(self):

        loc = ('/Users/shawnzanders/PycharmProjects/theForgeCodeKata/GroceryExcel/GroceryInventory.xlsx')

        wb = xlrd.open_workbook(loc)
        sheet = wb.sheet_by_index(0)

        sheet.cell_value(0, 1)

        for i in range(sheet.nrows):
            name = sheet.cell_value(i, 1)
            price = sheet.cell_value(i, 2)
            units = sheet.cell_value(i, 3)
            markdown = sheet.cell_value(i, 4)
            hasSpecialty = sheet.cell_value(i, 5)
            item = self.generateItem(name, price, units, markdown, hasSpecialty)
            self.inventory.append(item)



class InventoryItem:

    def __init__(self, name, price, units, markdown, hasSpecialty):
        self.name = name
        self.price = price
        self.units = units
        self.markdown = markdown
        self.hasSpecialty = hasSpecialty

