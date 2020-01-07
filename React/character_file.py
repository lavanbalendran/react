import random

class character:
    def __init__(self,character_name1, health1, strength1, block1, special1, attack11, attack12, attack13, attack14):
        """
        Initializes Character class
        """
        self.character_name = character_name1
        self.health = health1
        self.strength = strength1
        self.block = block1
        self.special = special1
        self.attack1 = attack11
        self.attack2 = attack12
        self.attack3 = attack13
        self.attack4 = attack14

    def take_damage(self, opponent_attack):
        """
	When a character takes damage from their opponent,
	their health will decrease. It also gives a chance
	of having a player block an attack and activate a
	special power by doubling their attack.
	"""
        block_chance = random.randrange(0,100)
        special_chance = random.randrange(0,100)
        if block_chance <= (0.05)*self.block: 
            print("\n")
            print("Attack has been blocked")
        elif block_chance > (0.05)*self.block:
            if special_chance <= (0.05)*self.special:
                print("\n")
                print("Special Power is activated!")
                print("Attack has doubled!")
                print("\n")
                self.health = self.health - 2*(opponent_attack)
            else:
                self.health = self.health - opponent_attack

    def ugrade_skills(self, upgrade_choice, battle_number):
        """
        When a player defeats their opponent, they chose a skill to upgrade.
        They upgrade that skill by 100 times the battle number they just won. 
        """
        if upgrade_choice == "Health":
            self.health = self.health + (battle_number)*100
            print("You have upgraded your health by", battle_number*100)    
        elif upgrade_choice == "Strength":
            self.strength = self.strength + (battle_number)*100
            self.attack1 = self.attack1 + (battle_number)*5
            self.attack2 = self.attack2 + (battle_number)*5
            self.attack3 = self.attack3 + (battle_number)*5
            self.attack4 = self.attack4 + (battle_number)*5
            print("You have upgraded your attack by", battle_number*100)
        elif upgrade_choice == "Special":
            self.special = self.special + (battle_number)*100
            print("You have upgraded your special by",battle_number*100 )
        elif upgrade_choice == "Block":
            self.block = self.block + (battle_number)*100
            print("You have upgraded your block by",battle_number*100 )
            
class Ishiguro(character):
    def stats(self):
        """
        Initializes the Ishiguro Class
        """
        self.character_name = "Ishiguro"
        self.health = 200
        self.strength = 300
        self.block = 500
        self.special = 300
        self.attack1 = 15
        self.attack2 = 10  #come back for affect of agility and block
        self.attack3 = 10 
        self.attack4 = 5 #agility and block
        
    def show_attacks(self):
        """
	Shows Ishiguro's attacks and their properties
	"""
        print("Attacks:")
        print('1. Mini Black Holes:', self.attack1) #make one line
        print('2. Increase Gravity:', self.attack2)
        print('3. Change Gravity:', self.attack3)
        print('4. Levitation:', self.attack4)

    def show_stats(self):
        """
	Shows Ishiguro's stats
	"""
        print("Name:", self.character_name) #make one line
        print("Health:", self.health)
        print("Strength:", self.strength)
        print("Block:", self.block)
        print("Special:",self.special)


class Risotto_Nero(character):

    def stats(self):
        """
    	Initializes the Risotto Nero Class
    	"""
        self.character_name = 'Risotto Nero'
        self.health = 400
        self.strength = 300
        self.block = 200
        self.special = 100
        self.attack1 = 20
        self.attack2 = 10
        self.attack3 = 5 
        self.attack4 = 15

    def show_attacks(self):
        """
	Shows Risotto Nero's attacks and their properties
	"""
        print("Attacks:")
        print('1. Lightning Bolt:', self.attack1) #make one line
        print('2. Induced Magnetism:',self.attack2)
        print('3. Bright Flash:', self.attack3)
        print('4. Shock:',self.attack4)

    def show_stats(self):
        """
	Shows Risotto Nero's stats
	"""
        print("Name:", self.character_name)
        print("Health:" ,self.health)
        print("Strength:", self.strength)
        print("Block:",self.block)
        print("Special:",self.special)


class Forto(character):
    def stats(self):
        """
    	Initializes the Forto Class
    	"""
        self.character_name = 'Forto'
        self.health = 500
        self.strength = 400
        self.block = 200
        self.special = 300
        self.attack1 = 15
        self.attack2 = 5
        self.attack3 = 15 
        self.attack4 = 20

    def show_attacks(self):
        """
	Shows Forto's attacks and their properties
	"""
        print("Attacks:")
        print('1. Compression:', self.attack1) #make one line
        print('2. Glue:', self.attack2)
        print('3. Explosion:', self.attack3)
        print('4. Atomic Disintegration:', self.attack4)

    def show_stats(self):
        """
	Shows Forto's stats
	"""
        print("Name:", self.character_name)
        print("Health:", self.health)
        print("Strength:",self.strength)
        print("Block:",self.block)
        print("Special:",self.special)


class Piano(character):
    def stats(self):
        """
    	Initializes the Piano Class
    	"""
        self.character_name = 'Piano'
        self.health = 300
        self.strength = 200
        self.block = 100
        self.special = 500
        self.attack1 = 20
        self.attack2 = 15
        self.attack3 = 5 #come back for afteraffects
        self.attack4 = 10

    def show_attacks(self):
        """
	Shows Piano's attacks and their properties
	"""
        print("Attacks:")
        print('1. Nuclear Decay:', self.attack1) #make one line
        print('2. Nuetron Attack:', self.attack2)
        print('3. Radiation:', self.attack3)
        print('4. Neutrino Rain:', self.attack4)

    def show_stats(self):
        """
	Shows Piano's stats
	"""
        print("Name:", self.character_name)
        print("Health:", self.health)
        print("Strength:", self.strength)
        print("Block:", self.block)
        print("Special:" ,self.special)

class Mr_Park(character):
    def stats(self):
        """
        Initializes Mr_Park class
        """
        self.character_name = 'Mr Park'
        self.health = 600 #come back for stats
        self.strength = 500
        self.agility = 100
        self.block = 400
        self.special = 400
        self.attack1 = 20
        self.attack2 = 15
        self.attack3 = 15 
        self.attack4 = 20

    #include methods for different stages

    def show_attacks(self):
        """
	Shows Mr Park's attacks and their properties
	"""
        print("Attacks:")
        print('1. Plasma Cannon', self.attack1) #come for stats 
        print('2. Energy Projection:', self.attack2)
        print('3. Homing Missile:', self.attack3)
        print('4. Telekinesis:', self.attack4)

    def show_stats(self):
        """
	Shows Mr Park's stats
	"""
        print("Name:", self.character_name)
        print("Health:", self.health)
        print("Strength:", self.strength)
        print("Agility:" , self.agility)
        print("Block:", self.block)
        print("Special:" ,self.special)

###make all the characters be under one class, itll be easier to call on them 
