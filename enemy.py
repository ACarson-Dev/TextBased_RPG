class Enemy:
    def __init__(self, name, enemy_health, enemy_attack, enemy_defense, loot, enemy_level, exp_gained):
        self.enemy_name = name
        self.enemy_hp = enemy_health
        self.enemy_attack = enemy_attack
        self.enemy_defense = enemy_defense
        self.loot = loot
        self.enemy_level = enemy_level
        self.exp_gained = exp_gained

    def take_damage(self, damage):
        self.enemy_hp -= damage
        if self.enemy_hp <= 0:
            self.enemy_hp = 0

    def is_alive(self):
        return self.enemy_hp > 0

# Forest Area Enemies
class Goblin(Enemy):
    def __init__(self, name, enemy_health = 50, enemy_attack = 5, enemy_defense = 2, loot = "Minor Health Potion", enemy_level = 1, exp_gained = 10):
        super().__init__("Goblin", enemy_health, enemy_attack, enemy_defense, loot, enemy_level, exp_gained)
class Wolf(Enemy):
    def __init__(self, name, enemy_health = 60, enemy_attack = 6, enemy_defense = 3, loot = "Minor Mana Potion", enemy_level = 1, exp_gained = 12):
        super().__init__("Wolf", enemy_health, enemy_attack, enemy_defense, loot, enemy_level, exp_gained)
class Bear(Enemy):
    def __init__(self, name, enemy_health = 80, enemy_attack = 8, enemy_defense = 4, loot = "Wooden Shield", enemy_level = 1, exp_gained = 15):
        super().__init__("Bear", enemy_health, enemy_attack, enemy_defense, loot, enemy_level, exp_gained)

# Swamp Area Enemies
class SwampMonster(Enemy):
    def __init__(self, name, enemy_health = 70, enemy_attack = 7, enemy_defense = 5, loot = "Health Potion", enemy_level = 1, exp_gained = 20):
        super().__init__("Swamp Monster", enemy_health, enemy_attack, enemy_defense, loot, enemy_level, exp_gained)
class PoisonousFrog(Enemy):
    def __init__(self, name, enemy_health = 40, enemy_attack = 4, enemy_defense = 2, loot = "Mana Potion", enemy_level = 1, exp_gained = 8):
        super().__init__("Poisonous Frog", enemy_health, enemy_attack, enemy_defense, loot, enemy_level, exp_gained)
class GiantSnake(Enemy):
    def __init__(self, name, enemy_health = 90, enemy_attack = 9, enemy_defense = 6, loot = "Iron Shield", enemy_level = 1, exp_gained = 25):
        super().__init__("Giant Snake", enemy_health, enemy_attack, enemy_defense, loot, enemy_level, exp_gained)

# Mountains Area Enemies
class MountainTroll(Enemy):
    def __init__(self, name, enemy_health = 100, enemy_attack = 10, enemy_defense = 7, loot = "Major Health Potion", enemy_level = 1, exp_gained = 30):
        super().__init__("Mountain Troll", enemy_health, enemy_attack, enemy_defense, loot, enemy_level, exp_gained)
class Eagle(Enemy):
    def __init__(self, name, enemy_health = 50, enemy_attack = 5, enemy_defense = 3, loot = "Major Mana Potion", enemy_level = 1, exp_gained = 15):
        super().__init__("Eagle", enemy_health, enemy_attack, enemy_defense, loot, enemy_level, exp_gained)
class MountainLion(Enemy):
    def __init__(self, name, enemy_health = 80, enemy_attack = 8, enemy_defense = 5, loot = "Steel Shield", enemy_level = 1, exp_gained = 20):
        super().__init__("Mountain Lion", enemy_health, enemy_attack, enemy_defense, loot, enemy_level, exp_gained)

# Village Area Enemies
class Thief(Enemy):
    def __init__(self, name, enemy_health = 60, enemy_attack = 4, enemy_defense = 2, loot = "Health Potion", enemy_level = 1, exp_gained = 12):
        super().__init__("Thief", enemy_health, enemy_attack, enemy_defense, loot, enemy_level, exp_gained)
class Bandit(Enemy):
    def __init__(self, name, enemy_health = 70, enemy_attack = 4, enemy_defense = 2, loot = "Mana Potion", enemy_level = 1, exp_gained = 12):
        super().__init__("Bandit", enemy_health, enemy_attack, enemy_defense, loot, enemy_level, exp_gained)
