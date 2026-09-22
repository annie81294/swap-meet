import uuid
from swap_meet.item import Item

class Electronics:
    def __init__(self, id = None, type="Unknown", condition=0):
        if id == None:
            id = uuid.uuid4().int

        self.id = id
        self.type = type
        self.condition = condition

    def get_category(self):
        return "Electronics"

    def __str__(self):
        return f"An object of type Electronics with id {self.id}. This is a {self.type} device."

    def condition_description(self):
        return Item.condition_description(self)