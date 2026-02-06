import random
import time


class Character:
    def __init__(self, name, strength, health, defense):
        self.name = name
        self.strength = strength
        self.health = health
        self.defense = defense

    def take_damage(self, damage):
        damage_taken = max(0, damage - self.defense)
        self.health -= damage_taken
        return damage_taken

    def attack(self, target):
        damage = self.strength * 2
        return target.take_damage(damage)

    def is_alive(self):
        return self.health > 0


class Rogue(Character):
    def attack(self, target):
        dexterity = 20
        critical_hit = random.randint(1, 100) <= dexterity

        damage = self.strength * 2
        if critical_hit:
            damage *= 2
            print("*** Critical Hit ***")

        return target.take_damage(damage)


def arena_battle(player, enemy):
    print(f"\n=== {player.name} vs. {enemy.name} ===")

    while player.is_alive() and enemy.is_alive():
        print(f"\n{player.name}: {player.health} HP")
        print(f"{enemy.name}: {enemy.health} HP")

        dmg = player.attack(enemy)
        print(f"{player.name} hits {enemy.name} for {dmg}")

        if not enemy.is_alive():
            break

        dmg = enemy.attack(player)
        print(f"{enemy.name} hits {player.name} for {dmg}")

        time.sleep(1)

    if player.is_alive():
        print(f"\n{player.name} wins!")
        return True
    else:
        print(f"\n{enemy.name} wins!")
        return False


if __name__ == "__main__":
    player = Character("Cheetah", 10, 100, 2)
    enemy = Rogue("Eevee", 8, 100, 4)
    arena_battle(player, enemy)
