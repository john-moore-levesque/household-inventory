class Thing:
    def __init__(self, name, category, quantity, unit, opened, threshold, staple):
        self.name = name
        self.category = category
        self.quantity = quantity
        self.unit = unit
        self.opened = opened
        self.threshold = threshold
        self.staple = staple

    def open(self):
        self.opened = True

    @property
    def categories(self):
        raise NotImplementedError

    @property
    def units(self):
        raise NotImplementedError
