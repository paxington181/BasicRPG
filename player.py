import random
weapon = None

class Player():
    def __init__(self, level):
        self.level = level
        self.attack = level * 2
        self.defense = level * 1
        self.health = level * 10


    def take_damage(self, damage):
        damage_taken = damage - self.defense
        if self.health <= 0:
            print("You have died")
        else:
            print(f"Remaining HP:{self.health}")

    def attack(self, weapon):
        if weapon is None:
            damage_dealt = self.attack + (random.randint(2, 6))
        else:
            damage_dealt = self.attack + (random.randint(weapon))
