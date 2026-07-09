# class game_character:
#     def __init__(self, name, health, attack, heal_methods):

#         self.name = name
#         self.health = health
#         self.attack = attack
#         self.heal_methods = heal_methods

#     def intro(self):
#         return f"Name: {self.name}, Health: {self.health}, Attack: {self.attack}, Heal: {self.heal_methods}"
    
# char1 = game_character("zibai", 1000, 300, "potion")
# char2 = game_character("columbina", 1500, 270, "potion")

# print(char1.name)
# print(char1.attack)

# print(char1.intro())
# print(char2.intro())

class game_character:
    def __init__(self, name, health, attack_power):

        self.name = name
        self.health = health
        self.attack_power = attack_power
       
    def intro(self):
        return f"Name: {self.name}, Health: {self.health}, Attack: {self.attack_power}"
    
    def attack(self, enemy):
            enemy.health -= self.attack_power
            print(f"{self.name} serang {enemy.name}! {enemy.name} -{self.attack_power} HP.")

    def heal(self):
            self.health += 50
            
            print(f"{self.name} guna heal! HP sekarang: {self.health}")
            return "heal +50"

char1 = game_character("zibai", 1000, 300)
char2 = game_character("columbina", 1500, 270)

# 1. Tengok intro dulu
print(char1.intro())
print(char2.intro())
print("-" * 30)

# 2. Zibai serang Columbina!
char1.attack(char2) 

# 3. Columbina heal sebab kena serang!
char2.heal()
