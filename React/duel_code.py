import random
import time

def countdown(opponent):
    """
    Prints out the countdown before the battle.
    """
    print('\n')
    print("Your opponent is" , opponent)
    print("\n")
    print("Your battle will begin in...")
    time.sleep(1)
    print("3")
    print("\n")
    time.sleep(1)
    print("2")
    print("\n")
    time.sleep(1)
    print("1")
    print("\n")
    time.sleep(1)
    print("Begin!")
    print('\n')
    
def duel_code(player_1, player_2):
    """
    Runs the code that manages the battle. The player choses an attack they
    want to use. It runs with the take_damage method within the character class.
    It prints out the the opponent's health, and randomly choses and prints
    one of the opponent's attacks and prints player's new health. If a player
    reaches 0 health, the battle ends.
    """
    battle = True 
    while battle == True:
        print("It is your turn.")
        print("\n")
        player_1.show_attacks()
        print("\n")
        attack_choice = int(input("Choose an attack: "))
        if attack_choice == 1:
            player_2.take_damage(player_1.attack1)
        elif attack_choice == 2:
            player_2.take_damage(player_1.attack2)
        elif attack_choice == 3:
            player_2.take_damage(player_1.attack3)
        elif attack_choice == 4:
            player_2.take_damage(player_1.attack4)
        print("\n")
        if player_2.health > 0: 
            print("Opponent Health:" , player_2.health)
        elif player_2.health <= 0:
            print("Opponent Health: 0")
        player_2_attack = [player_2.attack1, player_2.attack2, player_2.attack3, player_2.attack4]
        player_2_attack_choice = random.choice(player_2_attack)
        print("Opponent Attack:" , player_2_attack_choice)
        player_1.take_damage(player_2_attack_choice)
        if player_1.health > 0:
            print("Player Health: ", player_1.health)
        elif player_1.health <= 0:
             print("Player Health: 0")
        print("\n")
        if player_1.health <= 0: #make sure they dont have negative health
            time.sleep(1)
            print(player_1.character_name , "is dead!")
            print("You have lost.")
            print("Train harder next time to defeat your opponent.")
            break
        if player_2.health <= 0:
            print(player_2.character_name, "is dead!")
            print("\n")
            time.sleep(1)
            print("You have won!")
            print("Congratulations young warrior!")
            battle = False
