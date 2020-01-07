class Start:
    def __init__(self, health, special, attack, block, agility, player_name, character_list):
        self.health = health
        self.player_name = player_name
        self.health = health
        self.attack = attack
        self.special = special
        self.block = block
        self.agility = agility
        self.character_list = character_list
    
        
class Attack(Start):
    def __init__(self, attack_choice, damage):
        self.attack_choice = attack_choice
        self.damage = damage
    
    def choose(self):
        print("Mini-black Holes")
        print("Increase Gravity")
        print("Change Gravity Direction")
        print("Levitation")
        self.attack_choice = input("Choose which attack you will use?")
                    
    def ishiguro_attacks(self):
        if self.attack == "Mini-black Holes":
            self.damage = 150
        if self.attack == "Increase Gravity":
            self.damage = 15
            self.agility = self.agility - 20
            self.block = self.block + 20
        if self.attack == "Change Gravity Direction":
            self.damage = 20
        if self.attack == "Levitation":
            self.damage = 5
            self.agility = self.agility - 10
            self.block = self.block - 10
            

class Health():
    def __init__(self, health, damage):
        self.health = health
        self.damage = damage
    
    def start_health(self):
        full = self.health
        return full
    
    def damage(self):
        return self.health - self.damage  #Come back here later, code doesn't work, attacks itself
        
    def death(self):
        if self.health == 0:
            print("You have lost!")

