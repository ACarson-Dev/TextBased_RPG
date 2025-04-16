# Carson_FinalProject
# Programmer: Alexander Carson
# Email: acarson2@cnm.edu
# Purpose: Create a class for weapon types used by characters and enemies in the game

class Weapon:
    def __init__(self, name, damage, weapon_type):
        self.name = name
        self.damage = damage
        self.weapon_type = weapon_type

    def describe(self):
        return f"{self.name} ({self.weapon_type}): {self.damage} damage"

