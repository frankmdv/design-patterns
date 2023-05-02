import copy


class Pant:
    def __init__(self, color, material):
        self.color = color
        self.material = material

    def clone(self):
        return copy.deepcopy(self)


class ElegantPant(Pant):
    def __init__(self, color, fabric, designer, brand):
        super().__init__(color, fabric)
        self.designer = designer
        self.brand = brand


class BeachPant(Pant):
    def __init__(self, color, fabric, pockets=False, cords=False):
        super().__init__(color, fabric)
        self.pockets = pockets
        self.cords = cords
