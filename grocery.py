from thing import Thing


class Grocery(Thing):
    categories = ['produce', 'dairy', 'frozen', 'meat', 'dry goods', 'supplies']
    units = ['box', 'jar', 'can', 'bag', 'lbs', 'gal', 'qt', 'pint', 'carton']

    def __init__(self, name, category, quantity, unit, opened=False, threshold=1, staple=False):
        super().__init__(name, category, quantity, unit, opened, threshold, staple)
        if not self.opened:
            self.maxQuantity = quantity
        else:
            self.maxQuantity = None
        if self.category not in self.categories:
            self.categories.append(category)
        if self.unit not in self.units:
            self.units.append(unit)
