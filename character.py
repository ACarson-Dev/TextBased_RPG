# Carson
# Purpose: Create a class to represent a character in a game

# Object of type Character
class Character:
    # Constructor method for character attributes
    def __init__ (self, name, health, strength, speed, armor, level):
        # Initialize the character's attributes meaning the name, health, strength, speed, armor, and level
        # are set to the values and passed in when the object is created
        self.player_name = name
        self.player_health = health
        self.player_strength = strength
        self.player_speed = speed
        self.player_armor = armor
        self.player_level = level

    def player_info(self):
        print("My name is", self.player_name)
        print('Health =', self.player_health)
        print('Strength =', self.player_strength)
        print('Speed =', self.player_speed)
        print('Armor =', self.player_armor)
        print('Level =', self.player_level)
        if isinstance(self, Mage):
            print("Class Type: Mage")
            print("Mana =", self.mana)  # Display mana for Mage class
            print("Defense =", self.defense)  # Display defense for Mage class
        elif isinstance(self, Warrior):
            print("Class Type: Warrior")
            print("Defense =", self.defense)  # Display defense for Warrior class
        elif isinstance(self, Bowman):
            print("Class Type: Bowman")
            print("Arrows =", self.arrows)
            print("Defense =", self.defense)
        elif isinstance(self, Swordsman):
            print("Class Type: Swordsman")

            print("Defense =", self.defense)  # Display defense for Swordsman class


'''
    def take_damage(self, damage):
        # Reduce the character's health by the damage amount
        self.Character_health -= damage - self.Character_armor
        if self.Character_health <= 0:
            self.Character_health = 0  # Ensure health doesn't go below 0
        # Check if the character is dead
        if self.Character_health <= 0:
            print(f"{self.Character_name} has died.")
        else:
            return self.Character_health # Return the remaining health

    def attack(self, enemy):
        damage = self.Character_strength + (.25 * self.Character_speed) - enemy.defense
        enemy.take_damage(damage)
'''

# Warrior class inherits from Character class
class Warrior(Character):
    def __init__(self, name, health = 100, strength = 10, speed = 3, armor = 5, level = 1):
        # Initialize the warrior's attributes
        super().__init__(name, health, strength, speed, armor, level)
        self.defense = armor * level

# Mage class inherits from Character class
class Mage(Character):
    def __init__(self, name, health = 80, strength = 5, speed = 5, armor = 2, level = 1):
        # Initialize the mage's attributes
        super().__init__(name, health, strength, speed, armor, level)
        self.defense = armor * speed
        self.mana = 20 * level

# Bowman class inherits from Character class
class Bowman(Character):
    def __init__(self, name, health = 60, strength = 7, speed = 7, armor = 3, level = 1):
        # Initialize the bowman's attributes
        super().__init__(name, health * level, strength * level, speed * level, armor * level, level)
        self.defense = armor * speed
        self.arrows = 20 * level # Number of arrows

# SwordsMan class inherits from Character class
class Swordsman(Character):
    def __init__(self, name, health = 60, strength = 7, speed = 7, armor = 3, level = 1):
        super().__init__(name, health * level, strength * level, speed * level, armor * level, level)
        self.defense = armor * speed
        self.sword = 1  # Number of swords

instance1 = Swordsman('Hurcules', 100, 10, 4, 1, 1)
instance1.player_info()  # Call the player_info method to display character attributes

instance2 = Mage('Merlin', 80, 5, 5, 2, 1)
instance2.player_info()  # Call the player_info method to display character attributes
"""
    print(instance1.player_name)
    print(instance1.player_health)
    print(instance1.player_strength)
    print(instance1.player_speed)
    print(instance1.player_armor)
    print(instance1.player_level)
"""