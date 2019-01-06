from thing import Thing


class Supply(Thing):
    categories = ['cleaning', 'laundry', 'waste', 'hygiene']
    units = ['box', 'bottle', 'roll', 'carton', 'jug']

    def __init__(self, name, category, quantity, unit, opened=False, threshold=1, staple=False):
        super().__init__(name, category, quantity, unit, opened, threshold, staple)
        if self.category not in self.categories:
            self.categories.append(category)
        if self.unit not in self.units:
            self.units.append(unit)
