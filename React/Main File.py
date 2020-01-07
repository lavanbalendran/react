import random
import time
import os
os.chdir("/Users/lavanbalendran/desktop/react")
from character_file import *
from duel_code import *

program = True
while program == True:
    print("Welcome to React")
    time.sleep(1)
    print("Here are your characters")
    time.sleep(1)
    print("\n")
    ishiguro = Ishiguro("Ishiguro", 200, 300, 500, 300, 15, 10, 10, 5)
    ishiguro.show_stats()
    print("\n")
    ishiguro.show_attacks()
    print("\n")
    time.sleep(1)
    risotto_nero = Risotto_Nero("Risotto Nero", 400, 300, 200, 100, 20, 10, 5, 15)
    risotto_nero.show_stats()
    print("\n")
    risotto_nero.show_attacks()
    print('\n')
    time.sleep(1)
    forto = Forto("Forto", 500, 400, 200, 300, 15, 5, 15, 20)
    forto.show_stats()
    print("\n")
    forto.show_attacks()
    print('\n')
    time.sleep(1)
    piano = Piano("Piano", 300, 200, 100, 500, 20, 15, 5, 10)
    piano.show_stats()
    print("\n")
    piano.show_attacks()
    print('\n')

    characters = ['Ishiguro', 'Risotto Nero', 'Forto', 'Piano']
    player1 = input("Which character do you chose? ")
    print('\n')
    if player1 == "Ishiguro":
        player = Ishiguro("Ishiguro", 200, 300, 500, 300, 15, 10, 10, 5)
        #i feel like above line is repetitive, see if i can cut it elsewhere
    elif player1 == "Risotto Nero":
        player = Risotto_Nero("Risotto Nero", 400, 300, 200, 100, 20, 10, 5, 15)
    elif player1 == "Forto":
        player = Forto("Forto", 500, 400, 200, 300, 15, 5, 15, 20)
    elif player1 == "Piano":
        player = Piano("Piano", 300, 200, 100, 500, 20, 15, 5, 10)
    print("You have chosen" , player1)
    characters.remove(player1)
    computer = random.choice(characters)
    characters.remove(computer)
    if computer == "Ishiguro":
        comp = Ishiguro("Ishiguro", 200, 300, 500, 300, 15, 10, 10, 5)
        #i feel like above line is repetitive, see if i can cut it elsewhere
    elif computer == "Risotto Nero":
        comp = Risotto_Nero("Risotto Nero", 400, 300, 200, 100, 20, 10, 5, 15)
    elif computer == "Forto":
        comp = Forto("Forto", 500, 400, 200, 300, 15, 5, 15, 20)
    elif computer == "Piano":
        comp = Piano("Piano", 300, 200, 100, 500, 20, 15, 5, 10)
    ###this feels like a lot, see if i can cut (all of the elif and if statements)
    countdown(computer)
    #try making this a method in a class to reduce line numbers
    duel_code(player, comp)
    print("\n")
    print("You have won a reward")
    print("\n")
    player.stats()
    player.show_stats()
    print("\n")
    upgrade = input("Choose a stat you would like to upgrade: ")
    player.ugrade_skills(upgrade, 1)
    print("\n")
    print("These are your new stats:")
    player.show_stats()
    print("\n")
    player.show_attacks()
    print("\n")
    print("Your next battle will start soon")
    computer2 = random.choice(characters)
    characters.remove(computer2)
    if computer2 == "Ishiguro":
        comp2 = Ishiguro("Ishiguro", 200, 300, 500, 300, 15, 10, 10, 5)
        #i feel like above line is repetitive, see if i can cut it elsewhere
    elif computer2 == "Risotto Nero":
        comp2 = Risotto_Nero("Risotto Nero", 400, 300, 200, 100, 20, 10, 5, 15)
    elif computer2 == "Forto":
        comp2 = Forto("Forto", 500, 400, 200, 300, 15, 5, 15, 20)
    elif computer2 == "Piano":
        comp2 = Piano("Piano", 300, 200, 100, 500, 20, 15, 5, 10)
    countdown(computer2)
    duel_code(player, comp2)
    print("\n")
    print("You have won a reward")
    print("\n")
    player.stats() #resets stats, so previous reward is disregarded
    player.ugrade_skills(upgrade, 1)
    player.show_stats()
    print("\n")
    upgrade2 = input("Choose a stat you would like to upgrade: ")
    player.ugrade_skills(upgrade2, 2)
    print("\n")
    print("These are your new stats:")
    player.show_stats()
    print("\n")
    player.show_attacks()
    print("\n")
    time.sleep(2)
    print("You have reached the final stage.")
    time.sleep(2)
    print("Only few have made it this far.")
    time.sleep(2)
    print("But none have succeeded.")
    time.sleep(2)
    print("Your next battle is with the ...")
    time.sleep(2)
    print("MR PARK")
    time.sleep(2)
    final_boss = Mr_Park("Mr Park", 600, 500, 400, 400, 20, 15, 15, 20)
    countdown("Mr Park")
    duel_code(player, final_boss)
    print("\n")
    time.sleep(2)
    print("You have done the impossible and defeated the Mr Park!")
    time.sleep(2)
    print("And have won the game!")
    break
            

        
        
        
    
