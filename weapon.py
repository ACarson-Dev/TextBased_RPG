# Carson
# Purpose: Create a class for weapon types

class Weapon:
    def __init__(self, name, damage, weapon_type):
        self.name = name
        self.damage = damage
        self.weapon_type = weapon_type

class Spears(Weapon):
    def __init__(self, name="Spear", damage=15):
        super().__init__(name, damage, "Spear")

