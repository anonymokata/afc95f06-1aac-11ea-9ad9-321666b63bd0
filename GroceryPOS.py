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
            name = item.name
            markdownPrice = item.markdownPrice
            units = item.units
            specialtyToString = self.specialtyToString(item)
            print('{0}: ${1:.2f}/{2} {3}'.format(name, markdownPrice, units, specialtyToString))

    def specialtyToString(self, item):

        if item.specialtyType == 'none':
            return ''
        elif item.specialtyType == 'bogo':
            return 'Specialty: buy 1 get 1 free!'
        elif item.specialtyType == 'nforx':
            return 'Specialty: {0} for {1:.2f}!'.format(item.specialtyVariable1, item.specialtyVariable2)
        elif item.specialtyType == 'nmatx':
            print('Specialty: not set up yet')

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
        self.addToTotal(inventoryItem.markdownPrice * units)

    def removeSpecificItemFromTotal(self, cartItem):

        self.removeFromTotal(cartItem.markdownPrice * cartItem.quantity)

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
                self.total += cartItem.markdownPrice * units
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
                        self.total -= inventoryItem.markdownPrice
            elif inventoryItem.units == 'lb':
                if inventoryItem.quantity <= inventoryItem.limit:
                    qualifyingSpecialties = math.floor(inventoryItem.quantity / spv1)
                    self.total -= qualifyingSpecialties * inventoryItem.markdownPrice
                else:
                    qualifyingSpecialties = math.floor(inventoryItem.limit / spv1)
                    self.total -= qualifyingSpecialties * inventoryItem.markdownPrice

        if inventoryItem.specialtyType == 'nforx':

            if inventoryItem.units == 'sku':
                counter = 0
                for item in self.cart:
                    if item.name == inventoryItem.name:
                        counter += 1
                if counter <= inventoryItem.limit:
                    if counter % spv1 == 0:
                        self.total -= (spv1 * inventoryItem.markdownPrice)
                        self.total += spv2
            elif inventoryItem.units == 'lb':
                if inventoryItem.quantity <= inventoryItem.limit:
                    qualifyingSpecialties = math.floor(inventoryItem.quantity / spv1)
                    if qualifyingSpecialties >= 1:
                        self.total -= qualifyingSpecialties * (spv1 * inventoryItem.markdownPrice)
                        self.total += qualifyingSpecialties * (spv2)
                else:
                    qualifyingSpecialties = math.floor(inventoryItem.limit / spv1)
                    self.total -= qualifyingSpecialties * (spv1 * inventoryItem.markdownPrice)
                    self.total += qualifyingSpecialties * (spv2)

        if inventoryItem.specialtyType == 'nmatx':
            counter = 0
            if inventoryItem.units == 'sku':
                for item in self.cart:
                    if item.name == inventoryItem.name:
                        counter += 1
                if counter <= inventoryItem.limit:
                    if counter % (spv1 + spv2) == 0:
                        self.total -= ((spv2 * inventoryItem.markdownPrice)*(1-spv3))
            elif inventoryItem.units == 'lb':
                qualifyingSpecialties = math.floor(inventoryItem.quantity / (spv1 + spv2))
                self.total -= qualifyingSpecialties * ((spv2 * inventoryItem.markdownPrice)*(1-spv3))

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
                        self.total += cartItem.markdownPrice

            elif cartItem.units == 'lb':
                if cartItem.quantity <= cartItem.limit:
                    qualifyingSpecialties = math.floor(cartItem.quantity / spv1)
                    self.total += qualifyingSpecialties * cartItem.markdownPrice
                else:
                    qualifyingSpecialties = math.floor(cartItem.limit / spv1)
                    self.total += qualifyingSpecialties * cartItem.markdownPrice

        if cartItem.specialtyType == 'nforx':
            if cartItem.units == 'sku':
                counter = 0
                for item in self.cart:
                    if item.name == cartItem.name:
                        counter += 1
                if counter <= cartItem.limit:
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
                    self.total += qualifyingSpecialties * (spv1 * cartItem.markdownPrice)
                    self.total -= qualifyingSpecialties * (spv2)

        if cartItem.specialtyType == 'nmatx':
            if cartItem.specialtyType == 'sku':
                counter = 0
                for item in self.cart:
                    if item.name == cartItem.name:
                        counter += 1
                if counter % (spv1 + spv2) == 0:
                    qualifyingSpecialties = (counter / (spv1 + spv2))
                    difference = ((spv2 * cartItem.markdownPrice)*(1-spv3))
                    self.total += difference
            elif cartItem.specialtyType == 'lb':
                qualifyingSpecialties = math.floor(cartItem.quantity / (spv1 + spv2))
                self.total += qualifyingSpecialties * ((spv2 * cartItem.markdownPrice) * (1 - spv3))

    def generateItem(self, name, price, units, markdown, hasSpecialty, specialtyType, limit, specialtyVariable1, specialtyVariable2, specialtyVariable3):
        return InventoryItem(name, price, units, markdown, hasSpecialty, specialtyType, limit, specialtyVariable1, specialtyVariable2, specialtyVariable3)

    def fillInventory(self):

        loc = ('/Users/shawnzanders/PycharmProjects/theForgeCodeKata/GroceryExcel/GroceryInventory.xlsx')

        wb = xlrd.open_workbook(loc)
        sheet = wb.sheet_by_index(0)

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
        titleRow = self.inventory[0]
        self.inventory.remove(titleRow)
        self.generateMarkdownPrice()

    def generateMarkdownPrice(self):
        for item in self.inventory:
            item.markdownPrice = item.price - item.markdown

    def runPOS(self):
        command = True
        while command:
            print('Your total is: ${0:.2f}'.format(self.total))
            command = input('Enter I to see inventory and prices.\nEnter A to add an item to cart.\nEnter R to remove an item from cart.\nEnter Q to quit.')
            if command.lower() == 'i':
                self.printInventoryandPrices()
            elif command.lower() == 'a':
                validItem = False
                while validItem == False:
                    answer = input('What would you like to add to your cart?')
                    for item in self.inventory:
                        if item.name == answer:
                            self.addItemToCart(answer)
                            validItem = True

            elif command.lower() == 'r':
                answer = input('What would you like to remove from your cart')
                self.removeItemFromCart(answer)
            elif command.lower() == 'q':
                command = False
        print('Your final total is ${0:.2f}. We appreciate your business and we look forward to seeing you again. :)'.format(self.total))


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
        self.markdownPrice = 0.00
        self.specialtyVariable1 = specialtyVariable1
        self.specialtyVariable2 = specialtyVariable2
        self.specialtyVariable3 = specialtyVariable3

if __name__ == '__main__':
    grocery = GroceryPOS()
    grocery.fillInventory()
    grocery.runPOS()


