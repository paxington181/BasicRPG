import random

class Monster():
    def __init__(self, m_attack, m_defense, m_health):
        self.attack = m_attack
        self.defense = m_defense
        self.health = m_health

    def basic_attack(self):
        damage_done = self.attack + random.randint(1, 3)

    def take_damage(self):
