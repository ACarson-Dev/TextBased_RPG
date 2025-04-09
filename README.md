# TextBased_RPG
 
text_based_rpg/
├── character.py
    # The character.py file contains the Character class needs the following attributes:
    # - name: The name of the character.
    # - health: The health of the character.
    # - attack: The attack power of the character.
    # - strength: The strength of the character.
    # - speed: The speed of the character which is used to determine the order of turns in combat.
    # - armor: The armor of the character which is used to determine the damage taken from enemies.
    # - level: The level of the character based on exp. gained from defeating enemies.
    # - experience: The experience points gained from defeating enemies working towards the next level.
    # - inventory: The inventory of the character which is a list of all items categorised by type.
    # - equipped_items: The equipped items of the character which is only one item per type.
├── area.py
    # The area.py file contains the Area class needs the following attributes:
    # - name: The name of the area.
    # - description: The description of the area.
    # - enemies: The enemies that can be found in the area.
    # - items: The items that can be found in the area.
├── enemy.py
    # The enemy.py file contains the Enemy class needs the following attributes:
    # - name: The name of the enemy.
    # - health: The health of the enemy.
    # - attack: The attack power of the enemy.
    # - defense: The defense power of the enemy.
    # - loot: The loot dropped by the enemy.
    # - level: The level of the enemy.
    # - experience: The experience points gained from defeating the enemy.
├── player.py
    # The player.py file contains the Player class needs the following attributes:
    # - name: The name of the player.
    # - health: The health of the player based on the class chosen.
    # - attack: The attack power of the player based on the class chosen.
    # - defense: The defense power of the player based on the class chosen.
    # - level: The level of the player based on what the player has done in the game.
    # - experience: The current experience points gained from defeating enemies working towards the next level.
    # - inventory: The inventory of the player which is a list of all items categorised by type.
    # - equipped_items: The equipped items of the player which is only one item per type.
├── items/
│   ├── __init__.py # This file is required to make Python treat the directory as a package
│   ├── potions.py
    # The potions.py file contains the Potion class needs the following attributes:
    # - name: The name of the potion.
    # - effect: The effect of the potion.
    # - duration: The duration of the potion effect.
    # - type: The type of the potion (healing, buff, debuff).
    # - level: The level of the potion.
│   ├── armor.py
│   └── weapon.py 
│       ├── __init__.py # This file is required to make Python treat the directory as a package
│       ├── swords.py
        # contains the Sword class needs the following attributes:
        # - type: The type of the sword (long, short, broad, two-handed). 
        # - damage: The damage done by the sword based on the type of sword.
        # - level: The level of the sword which is used to determine the damage done by the sword.
│       ├── shields.py
        # contains the Shield class needs the following attributes:
        # - type: The type of the shield (kite, tower, buckler).
        # - defense: The defense done by the shield based on the type of shield.
        # - level: The level of the shield which is used to determine the defense done by the shield.
│       ├── bows.py
        # contains the Bow class needs the following attributes:
        # - type: The type of the bow (long, short, crossbow).
        # - damage: The damage done by the bow based on the type of bow.
        # - level: The level of the bow which is used to determine the damage done by the bow.
│       └── axes.py
        # contains the Axe class needs the following attributes:
        # - type: The type of the axe (battle, hand, throwing).
        # - damage: The damage done by the axe based on the type of axe.
        # - level: The level of the axe which is used to determine the damage done by the axe.
└── game.py
    # The game.py file contains the Game class needs the following attributes:
    # - player: The player object.
    # - area: The area object.
    # - enemies: The enemies in the area.
    # - items: The items in the area.
    # - inventory: The inventory of the player which is a list of all items categorised by type.
    # - equipped_items: The equipped items of the player which is only one item per type.