class Player():
    def __init__(self, level):
        self.level = level
        self.attack = level * 2
        self.defense = level * 1
        self.health = level * 10


    def take_damage(self, damage):
        if self.health <= 0:
            print("You have died")
        else:
            damage_taken = damage - self.defense


    def attack(self):
        damage =
