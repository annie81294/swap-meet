import uuid

class Item:
    def __init__(self, id = None):
        if id is None:
            id = uuid.uuid4().int

        self.id = id

    def get_category(self):
        return "Item"
