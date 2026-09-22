from .item import Item

class Vendor:
    def __init__(self, inventory=None):
        if inventory is None:
            inventory = []
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

    def get_by_category(self, category):
        category_objects = []

        for object in self.inventory:
            if category == object.get_category():
                category_objects.append(object)

        return category_objects

    def get_best_by_category(self, category):
        current_best_condition = 0
        best_object_so_far = Item
        category_objects = self.get_by_category(category)
        if len(category_objects) == 0:
            return None

        for object in category_objects:
            if object.condition > current_best_condition:
                best_object_so_far = object
                current_best_condition = object.condition

        return best_object_so_far

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        best_items_in_their_category = self.get_best_by_category(their_priority)
        if not best_items_in_their_category:
            return None
        best_items_in_my_category = other_vendor.get_best_by_category(my_priority)
        if not best_items_in_my_category:
            return None

        self.swap_items(other_vendor, best_items_in_their_category, best_items_in_my_category)

        return True
