from .item import Item

class Vendor:
    def __init__(self, inventory = []):
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, matching_item):
        for i in range(len(self.inventory)):
            if self.inventory[i] == matching_item:
                self.inventory.pop(i)
                return matching_item
        return None

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
        if len(self.inventory) == 0 or len(other_vendor.inventory) == 0:
            return False
        first_item_in_my_inventory = self.inventory[0]
        first_item_in_others_inventory = other_vendor.inventory[0]

        self.swap_items(other_vendor, first_item_in_my_inventory, first_item_in_others_inventory)
        return True
