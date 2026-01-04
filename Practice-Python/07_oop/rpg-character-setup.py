# Title

import shutil
width = shutil.get_terminal_size().columns
print("/" * width)
print("\n")
print(" ⚔️  RPG character setup ⚔️".center(width))
print(("_" * 23).center(width))
print("\n")
print("\\" * width)


class Character:
    def __init__(self, name, health, attack_power, defense_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.defense_power = defense_power

    def attack(self):
        print(f"{self.name} attacks with power {self.attack_power}")

    def get_stats(self):
        print(f"Name: {self.name}")
        print(f"Health: {self.health}")
        print(f"Attack power: {self.attack_power}")
        print(f"Defense power: {self.defense_power}")

class Warrior(Character):
    def __init__(self, name, health, attack_power, defense_power, weapon):
        super().__init__(name, health, attack_power, defense_power)
        self.weapon = weapon

    def attack(self):
        super().attack()
        print(f"Weapon: {self.weapon}")
        print(f"Get ready to witness {self.name}'s power ! ")
        

    def special_move(self):
        
        print(f"{self.name}'s Special move: INFINITE SLASH 🔥 ")


class Mage(Character):
    def __init__(self, name, health, attack_power, defense_power, mana):
        super().__init__(name, health, attack_power, defense_power)
        self.mana = mana

    def attack(self):
        print(f"My spell...You can't escape {self.name}'s magic ! ")

    def cast_spell(self):
        print(f"Mana power: {self.mana}")
        print(f"{self.name} casts a spell using {self.mana} mana 🔮")



print("\n")
name = input("Enter you character name 🔫: ")
health = 100

choice = input("Enter your character: WARRIOR/MAGE: ").upper()

if choice == "WARRIOR":
    attack_power = 75
    defense_power = 35
    weapon = "Sword"
    player = Warrior(name, health, attack_power, defense_power, weapon)


elif choice == "MAGE":
    attack_power = 30
    defense_power = 80
    mana = "Wind"
    player = Mage(name, health, attack_power, defense_power, mana)

else:
    print("Invalid character choice")
    exit()

print("\n")
print("~" * width)
print(" ⚔️  YOUR SETUP ⚔️".center(width))
print("~" * width)
print("\n")

player.get_stats()
player.attack()

if isinstance(player, Warrior):
    player.special_move()

elif isinstance(player, Mage):
    player.cast_spell()