class Vendor:
    def __init__(self, inventory = []):
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, matching_item):
        for i in range(len(self.inventory)):
            print(self.inventory[i])
            print(matching_item)
            if self.inventory[i] == matching_item:
                self.inventory.pop(i)
                return matching_item
        return None
            