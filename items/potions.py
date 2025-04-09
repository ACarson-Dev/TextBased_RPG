class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class HealthPotion(Item):
    def __init__(self, name, description, health_restored):
        super().__init__(name, description)
        self.health_restored = health_restored

    def use(self):
        print(f"Using {self.name}. Restores {self.health_restored} health.")
        # Implement health restoration logic here


class ManaPotion(Item):
    def __init__(self, name, description, mana_restored):
        super().__init__(name, description)
        self.mana_restored = mana_restored

    def use(self):
        print(f"Using {self.name}. Restores {self.mana_restored} mana.")
        # Implement mana restoration logic here