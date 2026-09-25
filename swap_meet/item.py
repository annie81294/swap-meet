import uuid

class Item:
    def __init__(self, id = None):
        if id is None:
            id = uuid.uuid4().int

        self.id = id

    def get_category(self):
        return "Item"

    def __str__(self):
        #return(f"An object of type Item with id {self.id}.")
        return f"An object of type {self.__class__.__name__} with id {self.id}."
    
    def condition_description(self):
        if self.condition < 2:
            return "It's a no from me"
        elif self.condition < 4:
            return "Maybe"
        else:
            return"Score!"