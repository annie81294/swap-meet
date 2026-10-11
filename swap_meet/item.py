import uuid

CONDITION_DESCRIPTIONS = [
    "It's a no from me",  
    "It's a no from me",  
    "Maybe",              
    "Maybe",              
    "Score!",             
    "Score!",             
]

class Item:
    def __init__(self, id=None, condition=0):
        if id is None:
            id = uuid.uuid4().int

        self.id = id
        self.condition = condition

    def get_category(self):
        return "Item"

    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."
    
    def condition_description(self):
        return CONDITION_DESCRIPTIONS[int(self.condition)]