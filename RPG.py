# Every time the player walks, a random algorithm will be run that determines if a wild enemy has appeared (A 1/3 or 1/4 chance of being attacked
# Use a while loop to control this flow.
# If a wild enemy appears
# The user can decide to attack or run
# If attacking, a random amount of damage will be dealt between a minimum number and maximum number
# If running, there will be a 50% chance of escaping
# After the player attacks or runs the enemy attacks back for a random damage amount
# The player and enemy will attack each other in a loop until one of them passes out or dies.
# If the player kills the enemy you can give the Player some HP and a special item that is stored in the inventory. After this, the player will continue walking.
# If the enemy kills the player the console prints a cool death message and the game ends
# Inventory
# When the player kills enemies, they are awarded with items

import random 

print("Welcome fellow pirate!")
Name = input("What should I call you?")
hello = input(f"Hello {Name} ready to go steal some tresure?")

hp = 100
treasure = []
player_health = 100
enemy_health = 100

def attack_enemy(player_health, enemy_health):
    while True:
        if player_health > 0: 
            your_attack = random.randint(10,100)
            print(f"you attacked the enemy for {your_attack} damage!")
            enemy_health -= your_attack 
            
        
        if enemy_health > 0:
            enemy_attack = random.randint(10,100)
            print(f"the enemy attacked you for {enemy_attack} damage!")
            player_health -= enemy_attack

        if player_health <= 0:
            print(f"RIP {Name} dead men tell no tales!")
            exit()
        
        if enemy_health <= 0:
            print("you have recieved 25 health and gold in your inventory")
            player_health += 25
            treasure.append('gold')
            break

while True:
    start_action = input("type s to sail onward. type t to check your treasure chest. ")
    if start_action == 's':
        action1 = "Opps, it seems you have run into another pirate ship!"
        action2 = "Oh no, It seems you have fallin into the sirens trap"
        action3 = "whoops, you have attracted the attention of a sea monster!"

        actions = [action1, action2, action3]
        action_choice = print(random.choice(actions))


        battle = input("Will you stay and f-fight or r-run away?")
        if battle == "f":
            attack_enemy(player_health, enemy_health)
        elif battle == "r":
            print("you have eascaped your enemy good job")
    elif start_action == 't':
        print(f"You have {hp} HP and {len(treasure)} treasure so far.")


                











        