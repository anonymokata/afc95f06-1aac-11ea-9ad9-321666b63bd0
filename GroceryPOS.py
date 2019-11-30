import xlrd
import math

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
            print(f'{item.name}: {item.price}/{item.units} originally {item.price}')

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

        self.removeFromTotal((cartItem.price - cartItem.markdown) * cartItem.quantity)

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
                self.removeSpecialty(cartItem)
                units = int(input(f'How many pounds of {cartItem.name} would you like to add?'))
                cartItem.quantity += units
                self.total += (cartItem.price - cartItem.markdown) * units
                self.checkSpecialty(cartItem)
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
                self.removeSpecialty(cartItem)
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

        spv1 = inventoryItem.specialtyVariable1
        spv2 = inventoryItem.specialtyVariable2
        spv3 = inventoryItem.specialtyVariable3

        if inventoryItem.specialtyType == 'bogo':
            if inventoryItem.units == 'sku':
                counter = 0
                for item in self.cart:
                    if item.name == inventoryItem.name:
                        counter += 1
                if counter <= inventoryItem.limit:
                    if counter % spv1 == 0:
                        self.total -= (inventoryItem.price - inventoryItem.markdown)
            elif inventoryItem.units == 'lb':
                if inventoryItem.quantity <= inventoryItem.limit:
                    qualifyingSpecialties = math.floor(inventoryItem.quantity / spv1)
                    self.total -= qualifyingSpecialties * (inventoryItem.price - inventoryItem.markdown)
                else:
                    qualifyingSpecialties = math.floor(inventoryItem.limit / spv1)
                    self.total -= qualifyingSpecialties * (inventoryItem.price - inventoryItem.markdown)

        if inventoryItem.specialtyType == 'nforx':

            if inventoryItem.units == 'sku':
                counter = 0
                for item in self.cart:
                    if item.name == inventoryItem.name:
                        counter += 1
                if counter <= inventoryItem.limit:
                    if counter % spv1 == 0:
                        self.total -= (spv1 * (inventoryItem.price - inventoryItem.markdown))
                        self.total += spv2
            elif inventoryItem.units == 'lb':
                if inventoryItem.quantity <= inventoryItem.limit:
                    qualifyingSpecialties = math.floor(inventoryItem.quantity / spv1)
                    if qualifyingSpecialties >= 1:
                        self.total -= qualifyingSpecialties * (spv1 * (inventoryItem.price - inventoryItem.markdown))
                        self.total += qualifyingSpecialties * (spv2)
                else:
                    qualifyingSpecialties = math.floor(inventoryItem.limit / spv1)
                    self.total -= qualifyingSpecialties * (spv1 * (inventoryItem.price - inventoryItem.markdown))
                    self.total += qualifyingSpecialties * (spv2)

        if inventoryItem.specialtyType == 'nmatx':
            counter = 0
            if inventoryItem.units == 'sku':
                for item in self.cart:
                    if item.name == inventoryItem.name:
                        counter += 1
                if counter <= inventoryItem.limit:
                    if counter % (spv1 + spv2) == 0:
                        self.total -= ((spv2 * (inventoryItem.price - inventoryItem.markdown))*(1-spv3))
            elif inventoryItem.units == 'lb':
                qualifyingSpecialties = math.floor(inventoryItem.quantity / (spv1 + spv2))
                self.total -= qualifyingSpecialties * ((spv2 * (inventoryItem.price - inventoryItem.markdown))*(1-spv3))

    def removeSpecialty(self, cartItem):

        spv1 = cartItem.specialtyVariable1
        spv2 = cartItem.specialtyVariable2
        spv3 = cartItem.specialtyVariable3

        if cartItem.specialtyType == 'bogo':
            if cartItem.units == 'sku':
                counter = 0
                for item in self.cart:
                    if item.name == cartItem.name:
                        counter += 1
                if counter <= cartItem.limit:
                    if counter % spv1 == 0:
                        self.total += (cartItem.price - cartItem.markdown)
            elif cartItem.units == 'lb':
                if cartItem.quantity <= cartItem.limit:
                    qualifyingSpecialties = math.floor(cartItem.quantity / spv1)
                    self.total += qualifyingSpecialties * (cartItem.price - cartItem.markdown)
                else:
                    qualifyingSpecialties = math.floor(cartItem.limit / spv1)
                    self.total += qualifyingSpecialties * (cartItem.price - cartItem.markdown)

        if cartItem.specialtyType == 'nforx':
            if cartItem.units == 'sku':
                counter = 0
                for item in self.cart:
                    if item.name == cartItem.name:
                        counter += 1
                if counter % spv1 == 0:
                    difference = (((spv1 * (cartItem.price - cartItem.markdown)) - spv2))
                    self.total += difference
            elif cartItem.units == 'lb':
                if cartItem.quantity <= cartItem.limit:
                    qualifyingSpecialties = math.floor(cartItem.quantity / spv1)
                    if qualifyingSpecialties >= 1:
                        self.total += qualifyingSpecialties * (spv1 * (cartItem.price - cartItem.markdown))
                        self.total -= qualifyingSpecialties * (spv2)
                else:
                    qualifyingSpecialties = math.floor(cartItem.limit / spv1)
                    self.total += qualifyingSpecialties * (spv1 * (cartItem.price - cartItem.markdown))
                    self.total -= qualifyingSpecialties * (spv2)

        if cartItem.specialtyType == 'nmatx':
            if cartItem.specialtyType == 'sku':
                counter = 0
                for item in self.cart:
                    if item.name == cartItem.name:
                        counter += 1
                if counter % (spv1 + spv2) == 0:
                    qualifyingSpecialties = (counter / (spv1 + spv2))
                    difference = ((spv2 * (cartItem.price - cartItem.markdown))*(1-spv3))
                    self.total += difference
            elif cartItem.specialtyType == 'lb':
                qualifyingSpecialties = math.floor(cartItem.quantity / (spv1 + spv2))
                self.total += qualifyingSpecialties * ((spv2 * (cartItem.price - cartItem.markdown)) * (1 - spv3))

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

    def runPOS(self):
        command = True
        while command:
            print(f'Your total is: ${self.total}')
            command = input('Enter I to see inventory and prices. Enter A to add an item to cart. Enter R to remove an item from cart. Enter Q to quit.')
            if command.lower() == 'i':
                self.printInventoryandPrices()
            elif command.lower() == 'a':
                answer = input('What would you like to add to your cart?')
                self.addItemToCart(answer)
            elif command.lower() == 'r':
                answer = input('What would you like to remove from your cart')
                self.removeItemFromCart(answer)
            elif command.lower() == 'q':
                command = False
        print(f'Your final total is ${self.total}. We look forward to seeing you again. :)')


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



