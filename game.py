#Carson_FianlProject
#Programmer: Alexander Carson
#Email: acarson2@cnm.edu
#Purpose: Create a game in which the player can interact with the environment and fight enemies

from character import Character, Mage, Warrior, Bowman, Swordsman
from enemy import Enemy, Goblin, Wolf, Bear, SwampMonster, PoisonousFrog, GiantSnake
from area import Forest, Swamp, Mountains, Village
from items.potions import Item, HealthPotion, ManaPotion


def main(): 

    instance1 = Character('Hercules', 100, 10, 4, 1, 1)
    instance1.player_info()  # Call the player_info method to display character attributes

    instance2 = Mage('Merlin', 80, 5, 5, 2, 1)
    instance2.player_info()  # Call the player_info method to display character attributes

    instance3 = Warrior('Achilles', 120, 15, 3, 6, 1)
    instance3.player_info()  # Call the player_info method to display character attributes

    instance4 = Bowman('Robin Hood', 90, 8, 7, 4, 1)
    instance4.player_info()  # Call the player_info method to display character attributes

    instance5 = Swordsman('Lancelot', 110, 12, 6, 5, 1)
    instance5.player_info()  # Call the player_info method to display character attributes

'''
    print('Character types: \nWarrior \nMage \nBowman \nSwordsman')
    player_type = input('Choose your character type: ')
    player_health = input('Health: ')
    player_strength = input('Strength: ')
    player_speed = input('Speed: ')
    player_armor = input('Armor: ')
    player_level = input('Level: ')
   '''

main()  # Call the main function to start the program