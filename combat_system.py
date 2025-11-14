import random
def combat_system(player, monster):
    """ creates a turn-based combat system between the player and a monster
    
    Args:
        player(dict): a dict that contains the players stats
        monster(dict): a dict that contains the monsters stats
        
    Returns:
        None: updates players dict and gives live combat messages
    """
    print(f"\nA wild {monster['name']} has appeared!")
    while player["hp"] > 0 and monster["hp"] > 0:
        option = input("\nChoose one of the following: [A]ttack,"
            "[I]nventory\n").lower()
    
        if option == 'a':
            critical_hit = random.choice([1, 1, 1, 2])
            dmg = max(0, (player["attack"] * critical_hit) - 0)
            monster["hp"] -= dmg
            if critical_hit == 2:
                print(f"\nYou landed a critical hit! You dealt {dmg} "
                      "damage!")
            else:
                print(f"\nYou dealt {dmg} damage!")
        elif option == "i":
            # inventory.use_item(player)
            print("placeholder")
            return
        else:
            print("Invalid.")
            continue
        if monster["hp"] <= 0:
            print(f"\nYou have slain the {monster['name']}!")
            player['exp'] += monster['exp']
            print(f"{monster['exp']} was accquired from the {monster['name']}")
            break
        
        print(f"\nThe {monster['name']} will now strike!")
        if random.random() < monster['miss_chance']:
            print(f"The {monster['name']} missed!")
        else:
            dmg = monster['attack']
            player['hp'] -= dmg
            print(f"The {monster['name']} has dealt {dmg} damage")
        if player['hp'] <= 0:
            print("\nYou have been killed...")         
            break
          
player = {
    "name": "john",
    "hp": 10,
    "attack": 2,
    "level": 1,
    "exp": 0
    
}
monster = {
    "name": "Goblin",
    "hp": 10,
    "attack": 3,
    "exp": 20,
    "miss_chance": .1
}
combat_system(player, monster)