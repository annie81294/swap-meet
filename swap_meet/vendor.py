#from .item import Item

class Vendor:
    def __init__(self, inventory=None):
        if inventory is None:
            inventory = []
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, matching_item):
        found_index = None

        for i in range(len(self.inventory)):
            if self.inventory[i] == matching_item:
                found_index = i
                break

        if found_index is None:
            return None

        self.inventory[found_index], self.inventory[-1] = (
            self.inventory[-1],
            self.inventory[found_index]
        )
        self.inventory.pop()

        return matching_item

    def get_by_id(self, id):
        for item in self.inventory: 
            if item.id == id:
                return item 
        return None

    def swap_items(self, other_vendor, my_item, their_item):
        if not self.get_by_id(my_item.id) or not other_vendor.get_by_id(their_item.id):
            return False
        
        self.remove(my_item)
        other_vendor.add(my_item)
        self.add(their_item)
        other_vendor.remove(their_item)

        return True
    
    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False

        self.inventory[0], other_vendor.inventory[0] = (
            other_vendor.inventory[0],
            self.inventory[0],
            )
        return True

    def get_by_category(self, category):
        return [object for object in self.inventory if object.get_category() == category]

    def get_best_by_category(self, category):
        items = self.get_by_category(category)
        if not items:
            return None

        best_item = items[0]
        for item in items:
            if item.condition > best_item.condition:
                best_item = item

        return best_item

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        best_items_in_their_category = self.get_best_by_category(their_priority)
        best_items_in_my_category = other_vendor.get_best_by_category(my_priority)

        if best_items_in_their_category is None or best_items_in_my_category is None:
            return False

        return self.swap_items(other_vendor, best_items_in_their_category, best_items_in_my_category)
