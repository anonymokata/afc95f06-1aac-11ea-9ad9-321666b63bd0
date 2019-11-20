import xlrd

class GroceryPOS:
    def __init__(self):
        self.total = 0
        self.inventory = []
        self.cart = []
        self.listOfItemNamesInCart = []

    def addToTotal(self, item):

        self.total += item

    def removeFromTotal(self, item):

        self.total -= item

    def printInventoryandPrices(self):
        for item in self.inventory:
            print(f'{item.name}: + {item.price - item.markdown}/ + {item.units}')


    def chooseSpecificItemFromCart(self, name):
        for item in self.cart:
            if item.name == name:
                return item

    def chooseSpecificItemFromInventory(self, name):
        for item in self.cart:
            if item.name == name:
                return item

    def addSpecificItemToTotal(self, inventoryItem):

        units = self.checkUnits(inventoryItem)
        self.addToTotal((inventoryItem.price - inventoryItem.markdown) * units)

    def removeSpecificItemFromTotal(self, inventoryItem):

        self.removeFromTotal((inventoryItem.price - inventoryItem.markdown) * inventoryItem.pounds)


    def addItemToCart(self, name):

        if name not in self.listOfItemNamesInCart:
            for inventoryItem in self.inventory:
                if inventoryItem.name == name:
                    self.listOfItemNamesInCart.append(inventoryItem.name)
                    self.cart.append(inventoryItem)
                    self.addSpecificItemToTotal(inventoryItem)
                    self.checkSpecialty(inventoryItem)
        else:
            cartItem = self.chooseSpecificItemFromCart(name)
            if cartItem.units == 'lb':
                units = int(input(f'How many pounds of {cartItem.name} would you like to add?'))
                cartItem.pounds += units
                self.total += (cartItem.price - cartItem.markdown) * units
            elif cartItem.units == 'sku':
                self.listOfItemNamesInCart.append(cartItem.name)
                self.cart.append(cartItem)
                self.addSpecificItemToTotal(cartItem)
                self.checkSpecialty(cartItem)

    def removeItemFromCart(self, name):
        if len(self.cart) == 0:
            print('There are no items in your cart')
        elif name not in self.listOfItemNamesInCart:
            print('item is not in cart')
        else:
            scannedItem = ''
            try:
                cartItem = self.chooseSpecificItemFromCart(name)
                scannedItem = cartItem.name
                self.removeSpecificItemFromTotal(cartItem)
                self.listOfItemNamesInCart.remove(cartItem.name)
                self.cart.remove(cartItem)

            except ValueError:
                print(f'There is no {scannedItem} in your cart')

    def checkUnits(self, inventoryItem):

        if inventoryItem.units == 'lb':
            quantity = int(input(f'How many pounds of {inventoryItem.name}?'))
            inventoryItem.pounds = quantity
            return inventoryItem.pounds
        elif inventoryItem.units == 'sku':
            inventoryItem.pounds = 1
            return inventoryItem.pounds

    def checkSpecialty(self, inventoryItem):

        if inventoryItem.hasSpecialty == True:
            self.useSpecialty(inventoryItem)
            return True
        else:
            return False

    def useSpecialty(self, inventoryItem):

        if inventoryItem.specialtyType == 'bogo':
            counter = 0
            for item in self.cart:
                if item.name == inventoryItem.name:
                    counter += 1
            if counter % 2 == 0:
                self.total -= (inventoryItem.price - inventoryItem.markdown)

    def generateItem(self, name, price, units, markdown, hasSpecialty, specialtyType):
        return InventoryItem(name, price, units, markdown, hasSpecialty, specialtyType)

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
            specialtyType = sheet. cell_value(i, 6)
            item = self.generateItem(name, price, units, markdown, hasSpecialty, specialtyType)
            self.inventory.append(item)




class InventoryItem:

    def __init__(self, name, price, units, markdown, hasSpecialty, specialtyType):
        self.name = name
        self.price = price
        self.units = units
        self.markdown = markdown
        self.hasSpecialty = hasSpecialty
        self.specialtyType = specialtyType
        self.pounds = 0



