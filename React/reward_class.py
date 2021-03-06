class Reward:
    def __init__(self, health, special, attack, block, agility):
        """
        Initializes the Reward class
        """
        self.health = health
        self.attack = attack
        self.special = special
        self.block = block
        self.agility = agility
    
    def winner_upgrade(self):
        """
        """
        if self.health == 0: # The enemy's health is zero
            upgrade = input("Which stat would you like to upgrade!:") # Print stats
            if upgrade == "Health":
                print("You have upgraded your health by 1 point")
                return self.health + 100
            elif upgrade == "Special":
                print("You have upgraded your special by 1 point")
                return self.special + 100
            elif upgrade == "Attack":
                print("You have upgraded your attack by 1 point")
                return self.attack + 100
            elif upgrade == "Block":
                print("You have upgraded your block by 1 point")
                return self.block  + 100
            elif upgrade == "Agility":
                print("You have upgraded your agility by 1 point")
                return self.agility + 100
