class Pantry:
    def __init__(self):
        self.inventory = {}
        self.depleted = []
        self.low = []
        self.shoppingList = {}
        self.staples = []

    def addToPantry(self, item):
        if item.name not in self.inventory.keys():
            self.inventory[item.name] = [0, []]
        self.inventory[item.name][0] += item.quantity
        self.inventory[item.name][1].append(item)

    def consume(self, item, amount):
        restock = False
        if item.name not in self.inventory.keys():
            return False
        self.inventory[item.name][0] -= amount
        if self.inventory[item.name][0] < 0:
            self.depleted.append(item.name)
            self.inventory.pop(item.name)
            restock = True
        elif self.inventory[item.name][0] < item.threshold:
            self.low.append(item.name)
            restock = True
        if restock:
            self.buildShoppingList(item)

    def consolidate(self, item):
        if item.name not in self.inventory.keys():
            return False
        quantity = 0
        for thing in self.inventory[item.name][1]:
            quantity += thing.quantity
        self.inventory[item.name][0] = quantity

    def buildShoppingList(self, item):
        if item.name not in self.shoppingList.keys():
            self.shoppingList[item.name] = (item.maxQuantity or 1, item.unit)
        else:
            return None

    def shopped(self):
        self.shoppingList.clear()
