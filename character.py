# Carson
# Programmer: Alexander Carson
# Email: acarson2@cnm.edu
# Purpose: Create a class to represent a character in a game incorporating how they attack and take damage as well as
# any special information for each character type


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


    def take_damage(self, damage):
        # Reduce the character's health by the damage amount
        self.player_health -= max(0, damage - self.player_armor)
        if self.player_health <= 0:
            self.player_health = 0  # Ensure health doesn't go below 0
            print(f"{self.player_name} has died.") # Check if the character is dead
        else:
            return print(f"{self.player_name} has {self.player_health} health remaining")

    def attack(self, enemy):
        damage = (self.player_strength + (.25 * self.player_speed)) - enemy.enemy_defense
        if damage > enemy.player_health:
            print(f"{self.player_name} has killed a {enemy.enemy_name}")
        else:
            print(f"{self.player_name} has attacked {enemy.enemy_name} for {damage} damage")





def __str__(self):
    # Return the character's information as a formatted string
    return (
        f"My name is {self.player_name}\n"
        f"Health = {self.player_health}\n"
        f"Strength = {self.player_strength}\n"
        f"Speed = {self.player_speed}\n"
        f"Armor = {self.player_armor}\n"
        f"Level = {self.player_level}"
    )


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
    def __init__(self, name, health = 100, strength = 10, speed = 3, armor = 5, level = 1): # Initialize the warrior's base attributes
        super().__init__(name, health, strength, speed, armor, level)
        self.defense = armor * level
    def special_info(self):
        # Override the player_info method to include mana for Mage class
        print("Class Type: Bowman")
        print("Defense =", self.defense, '\n')

# Mage class inherits from Character class
class Mage(Character):
    def __init__(self, name, health = 80, strength = 5, speed = 5, armor = 2, level = 1): # Initialize the mage's base attributes
        super().__init__(name, health, strength, speed, armor, level)
        self.defense = armor * speed
        self.mana = 20 * level
    def special_info(self):
        #Override the player_info method to include mana for Mage class
        print("Class Type: Mage")
        print("Mana =", self.mana)
        print("Defense =", self.defense, '\n')

# Bowman class inherits from Character class
class Bowman(Character):
    def __init__(self, name, health = 60, strength = 7, speed = 7, armor = 3, level = 1): # Initialize the bowman's base attributes
        super().__init__(name, health, strength, speed, armor, level)
        self.defense = armor * speed
        self.arrows = 20 * level # Number of arrows
    def special_info(self):
        #Override the player_info method to include mana for Mage class
        print("Class Type: Bowman")
        print("Arrows Qt. =", self.arrows)
        print("Defense =", self.defense, '\n')

# SwordsMan class inherits from Character class
class Swordsman(Character):
    def __init__(self, name, health = 60, strength = 7, speed = 7, armor = 3, level = 1): # Initialize the swordsman's base attributes
        super().__init__(name, health, strength, speed, armor, level)
        self.defense = armor * speed
        self.sword = 1  # Number of swords
    def special_info(self):
        #Override the player_info method to include mana for Mage class
        print("Class Type: Bowman")
        print("Arrows Qt. =", self.sword)
        print("Defense =", self.defense, '\n')

def main():
    instance1 = Swordsman('Hercules', 100, 10, 4, 1, 1)
    print(instance1)  # Call the player_info method to display character attributes

    instance2 = Mage('Merlin', 80, 5, 5, 2, 1)
    print(instance2)  # Call the player_info method to display character attributes

    instance3 = Warrior('Achilles', 120, 15, 3, 6, 1)
    print(instance3)  # Call the player_info method to display character attributes

    instance4 = Bowman('Robin Hood', 90, 8, 7, 4, 1)
    print(instance4)  # Call the player_info method to display character attributes

    instance5 = Swordsman('Lancelot', 110, 12, 6, 5, 1)
    print(instance5)  # Call the player_info method to display character attributes

if __name__ == "__main__":
    main()  # Call the main function to start the program

    """     
            self.experience = experience
            self.inventory = inventory
            self.equipped_items = equipped_items
    """