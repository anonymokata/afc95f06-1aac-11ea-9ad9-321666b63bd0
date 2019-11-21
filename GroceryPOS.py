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
        for item in self.inventory:
            if item.name == name:
                return item

    def addSpecificItemToTotal(self, inventoryItem):

        units = self.checkUnits(inventoryItem)
        self.addToTotal((inventoryItem.price - inventoryItem.markdown) * units)

    def removeSpecificItemFromTotal(self, cartItem):

        self.removeFromTotal((cartItem.price - cartItem.markdown) * cartItem.pounds)


    def addItemToCart(self, name):

        if name not in self.listOfItemNamesInCart:
            inventoryItem = self.chooseSpecificItemFromInventory(name)
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
            inventoryItem.quantity = quantity
            return inventoryItem.quantity
        elif inventoryItem.units == 'sku':
            inventoryItem.quantity = 1
            return inventoryItem.quantity

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
            if counter <= inventoryItem.limit:
                if counter % inventoryItem.specialtyVariable1 == 0:
                     self.total -= (inventoryItem.price - inventoryItem.markdown)


        if inventoryItem.specialtyType == 'nforx':
            counter = 0
            for item in self.cart:
                if item.name == inventoryItem.name:
                    counter += 1
            if counter % inventoryItem.specialtyVariable1 == 0:
                self.total -= (inventoryItem.specialtyVariable1 * (inventoryItem.price - inventoryItem.markdown))
                self.total += inventoryItem.specialtyVariable2

        if inventoryItem.specialtyType == 'nmatx':
            spv1 = inventoryItem.specialtyVariable1
            spv2 = inventoryItem.specialtyVariable2
            spv3 = inventoryItem.specialtyVariable3
            counter = 0
            for item in self.cart:
                if item.name == inventoryItem.name:
                    counter += 1
            if counter % (spv1 + spv2) == 0:
                self.total -= ((spv2 * (inventoryItem.price - inventoryItem.markdown))*(1-spv3))



    def generateItem(self, name, price, units, markdown, hasSpecialty, specialtyType, limit, specialtyVariable1, specialtyVariable2, specialtyVariable3):
        return InventoryItem(name, price, units, markdown, hasSpecialty, specialtyType, limit, specialtyVariable1, specialtyVariable2, specialtyVariable3)

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
            specialtyType = sheet.cell_value(i, 6)
            limit = sheet.cell_value(i, 7)
            specialtyVariable1 = sheet.cell_value(i, 8)
            specialtyVariable2 = sheet.cell_value(i, 9)
            specialtyVariable3 = sheet.cell_value(i, 10)
            item = self.generateItem(name, price, units, markdown, hasSpecialty, specialtyType, limit, specialtyVariable1, specialtyVariable2, specialtyVariable3)
            self.inventory.append(item)




class InventoryItem:

    def __init__(self, name, price, units, markdown, hasSpecialty, specialtyType, limit, specialtyVariable1, specialtyVariable2, specialtyVariable3):
        self.name = name
        self.price = price
        self.units = units
        self.markdown = markdown
        self.hasSpecialty = hasSpecialty
        self.specialtyType = specialtyType
        self.limit = limit
        self.quantity = 0
        self.specialtyVariable1 = specialtyVariable1
        self.specialtyVariable2 = specialtyVariable2
        self.specialtyVariable3 = specialtyVariable3





