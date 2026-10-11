import uuid
from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, id=None, fabric = "Unknown", condition=0):
        super().__init__(id)
        self.fabric = fabric
        self.condition = condition

    def get_category(self):
        return "Clothing"

    def __str__(self):
        return f"{super().__str__()} It is made from {self.fabric} fabric."

    