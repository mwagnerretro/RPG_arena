# The following program creates a battle arena for players.
import random

class Character:
    # Constructor
    def __init__(self, name, strength, health, defense):
        self.name = name
        self.strength = strength
        self.health = health
        self.defense = defense

    # take_damage() Method
    def take_damage(self, damage):
        damage_taken = damage - self.defense
        self.health -= damage_taken
        return damage_taken

    # attack() Method
    def attack(self, target):
        damage = self.strength * 2
        damage_dealt = target.take_damage(damage)
        return damage_dealt

    # is_alive() Method
    def is_alive(self):
        return self.health > 0

# Extend a Class
class Rogue(Character):
    # attack() Method
    def attack(self, target):
        dexterity = 20
        critical_hit = random.randint(0, 100) < dexterity
        damage = self.strength * 2
        if critical_hit:
            damage *= 2
            print("*** Critical Hit ***")
        damage_dealt = target.take_damage(damage)
        return damage_dealt

# Class Objects
player = Character("Cheetah", 10, 100, 2)
print(player.name)
print(player.strength)
print(player.health)
print(player.defense)

enemy = Rogue("Eevee", 8, 100, 4)
print(enemy.name)
print(enemy.strength)
print(enemy.health)
print(enemy.defense)
