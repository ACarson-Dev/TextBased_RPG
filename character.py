#Carson
# Purpose: Create a class to represent a character in a game

# Object of type Character
class Character:
    # Constructor method for character attributes
    def __init__ (self, name, health, strength, speed, armor, level):
        # Initialize the character's attributes
        self.Character_name = name
        self.Character_health = health
        self.Character_strength = strength
        self.Character_speed = speed
        self.Character_armor = armor
        self.Character_level = level

    def TakeDamage(self, damage):
        # Reduce the character's health by the damage amount
        self.Character_health -= damage - self.Character_armor
        if self.Character_health <= 0:
            self.Character_health = 0  # Ensure health doesn't go below 0
        # Check if the character is dead
        if self.Character_health <= 0:
            print(f"{self.Character_name} has died.")
        else:
            return self.Character_health # Return the remaining health

    def Attack(self, enemy):
        damage = self.Character_strength + (.25 * self.Character_speed) - enemy.defense

# Warrior class inherits from Character class
class Warrior(Character):
    def __init__(self, name, health = 100, strength = 10, speed = 3, armor = 5, level = 1):
        # Initialize the warrior's attributes
        Character.__init__(name, health, strength, speed, armor, level)
        self.defense = armor * level

# Mage class inherits from Character class
class Mage(Character):
    def __init__(self, name, health = 80, strength = 5, speed = 5, armor = 2, level = 1):
        # Initialize the mage's attributes
        Character.__init__(name, health, strength, speed, armor, level)
        self.defense = armor * speed
        self.mana = 20 * level

# Bowman class inherits from Character class
class Bowman(Character):
    def __init__(self, name, health = 60, strength = 7, speed = 7, armor = 3, level = 1):
        # Initialize the bowman's attributes
        Character.__init__(name, health * level, strength * level, speed * level, armor * level, level)
        self.defense = armor * speed
        self.arrows = 20 * level # Number of arrows

# SwordsMan class inherits from Character class
class Swordsman(Character):
    def __init__(self, name, health = 60, strength = 7, speed = 7, armor = 3, level = 1):
        Character.__init__(name, health * level, strength * level, speed * level, armor * level, level)
        self.defense = armor * speed
        self.sword = 1  # Number of swords

class Druid:
    pass