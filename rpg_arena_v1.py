# The following program creates a battle arena for players.
class Character:
    # Constructor
    def __init__(self, name, strength, health, defense):
        self.name = name
        self.strength = strength
        self.health = health
        self.defense = defense

# Class Objects
player = Character("Cheetah", 10, 100, 2)
print(player.name)
print(player.strength)
print(player.health)
print(player.defense)
