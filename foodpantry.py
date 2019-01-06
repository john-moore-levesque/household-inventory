from pantry import Pantry


class FoodPantry(Pantry):
    def __init__(self):
        super().__init__()

    def addToPantry(self, foodstuff):
        super().addToPantry(foodstuff)
        if foodstuff.staple:
            if foodstuff.name not in self.staples:
                self.staples.append(foodstuff.name)
