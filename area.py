# Carson
# Purpose: Create a class for different types of areas in the game


class Area:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.enemies = []
        self.items = []

class Forest(Area):
    def __init__(self):
        super().__init__("Forest", "A dense forest filled with trees and wildlife.")
        self.forest_enemies = ["Goblin", "Wolf", "Bear"]
        self.items = ["Minor-Health Potion", "Minor-Mana Potion", "Wooden Shield"]

class Swamp(Area):
    def __init__(self):
        super().__init__("Swamp", "A murky swamp with dangerous creatures.")
        self.swamp_enemies = ["Swamp Monster", "Poisonous Frog", "Giant Snake"]
        self.items = ["Health Potion", "Mana Potion", "Iron Shield"]

class Mountains(Area):
    def __init__(self):
        super().__init__("Mountains", "A rocky mountain range with treacherous paths.")
        self.mountain_enemies = ["Mountain Troll", "Eagle", "Mountain Lion"]
        self.items = ["Major-Health Potion", "Major-Mana Potion", "Steel Shield"]

class Village(Area):
    def __init__(self):
        super().__init__("Village", "A peaceful village with friendly inhabitants.")
        self.village_enemies = ["Thief", "Bandit"]
        self.items = ["Health Potion", "Mana Potion", "Wooden Shield"]
