import uuid
from swap_meet.item import Item

class Clothing:
    def __init__(self, id = None, fabric = "Unknown", condition=0):

        if id is None:
            id = uuid.uuid4().int
        self.id = id
        self.fabric = fabric
        self.condition = condition

    def get_category(self):
        return "Clothing"

    def __str__(self):
        return f"An object of type Clothing with id {self.id}. It is made from {self.fabric} fabric."

    def condition_description(self):
        return Item.condition_description(self)

    