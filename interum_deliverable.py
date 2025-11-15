import random
#Megan Li Character Leveling System:
def level_up(current_lvl, current_exp, current_stats, exp_bar, stat_growth):
    """Checks if the player meets the required EXP/has enough EXP to level up
    
        Args:
            current_lvl (int): provides the player's current level
            current_exp (int): provides the player's current number of EXP
            current_stats (dict): provides the player's current stats
            exp_bar (list): provides the required EXP (per level) to level up
            
            Example: [0, 50, 100, 150, 250, ...]
            stat_growth (dict): how much stats grow per level depending on the 
            class
            
            Example: {"hp": 15,
                      "attack": 20,
                      "defense": 30}
        
        Returns:
            updated_level (tuple): the player's updated level such as their new
            level, remaining EXP, and updated stats
            
        Side effects: updates the player's level and stats
    """
    
    # Checks if the player hasn't reached max lvl and if they have enough EXP to 
    # reach the next lvl
    while current_lvl < len(exp_bar) - 1 and current_exp >= exp_bar[current_lvl]:
        current_lvl += 1

        for stat, growth_amt in stat_growth.items():
            current_stats[stat] += growth_amt
        
    remaining_exp = current_exp - exp_bar[current_lvl - 1]
    
    return current_lvl, remaining_exp, current_stats

# Test
current_lvl = 2
current_exp = 155

current_stats = {
    "hp": 100,
    "attack": 25,
    "defense": 35
}

stat_growth = {
    "hp": 15, 
    "attack": 5,
    "defense": 5
}

new_lvl, leftover_exp, updated_stats = level_up(
    current_lvl = current_lvl, 
    current_exp = current_exp, 
    current_stats = current_stats,
    exp_bar = [0, 50, 100, 150, 200], 
    stat_growth = stat_growth
    )

print("Initial Level:", current_lvl)
print("Remaining EXP:", leftover_exp)
print("Updated Stats:", updated_stats)

# Jeffrey Navarro Combat System:
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

#Danish Malik Exploration Sysyem:
def explore_room(player, total_rooms, event_list):
    """
    Move the player forward one room and trigger a random event.
    Args:
    player(dict): Player info with keys "location" (int) and "inventory" 
    (list of str).
    total_rooms(int): Total number of rooms in the dungeon.
    event_list(dict): Dictionary of events with probabilities. 
        Example:
        {"goblin":0.2, "dragon":0.05, "healing_potion":0.2, ...}

    Returns:
        player(dict): Updated player dictionary with new location and inventory.
        message(str): Description of what happened in the room.
        
    Side Effects:
        - Updates player["location"].
        - Appends items to player["inventory"] if found.
        - Randomly selects events using random.choices.    
    """

    # Step 1: move player forward
    player["location"] += 1

    # Step 2: check if player has reached the final room
    if player["location"] >= total_rooms:
        player["location"] = total_rooms
        return player, "You have reached the final room of the dungeon."

    # Step 3: randomly select an event using weighted probabilities
    # "events" contains the event names (e.g., "monster", "item", "nothing")
    events = list(event_list.keys())
    # "probabilities" contains the probability values for each event.
    # These determine how likely each event is to occur.
    probabilities = list(event_list.values())
    
    # Choose ONE event from the list using the given probabilities.
    # random.choices() returns a list, so we take the first (and only) element.
    event_type = random.choices(events, probabilities)[0]

    # Step 4: handle the event
    # Monsters 
    if event_type == "goblin":
        return player, "A goblin appears! Prepare for battle."
    if event_type == "dragon":
        return player, "A dragon appears! This is a deadly foe!"
    if event_type == "troll":
        return player, "A troll appears! Get ready to fight!"
    if event_type == "skeleton":
        return player, "A skeleton attacks! Prepare yourself!"

    # Items
    if event_type == "healing_potion":
        player["inventory"].append("Healing Potion")
        return player, "You found a Healing Potion!"
    if event_type == "strength_potion":
        player["inventory"].append("Strength Potion")
        return player, "You found a Strength Potion!"
    if event_type == "iron_sword":
        player["inventory"].append("Iron Sword")
        return player, "You found an Iron Sword!"
    if event_type == "steel_dagger":
        player["inventory"].append("Steel Dagger")
        return player, "You found a Steel Dagger!"

    #  Nothing happens
    return player, "Nothing happens in this room."



# Simple test simulation

player = {"location": 0, "inventory": []}
total_rooms = 5

event_list = {
    "goblin": 0.2,
    "dragon": 0.05,          
    "troll": 0.1,
    "skeleton": 0.1,
    "healing_potion": 0.2,
    "strength_potion": 0.15,
    "iron_sword": 0.1,
    "steel_dagger": 0.1,
    "nothing": 0.1            
}

print("Dungeon Exploration Test\n")

while player["location"] < total_rooms:
    player, message = explore_room(player, total_rooms, event_list)
    print(
    f"Room {player['location']}: {message} | Inventory: {player['inventory']}"
          )
    
#Joshua Cochran Inventory System:
def inventory():
       """Initializes the inventory and active items bar.
       displays inventory, 
       Returns: inventory (inv), active (active)
       """
       inv = [None, None, None, None, None,
           None, None, None, None, None,
           None, None, None, None, None,
           None, None, None, None, None,
           None, None, None, None, None]
       active = [None, None, None, None, None]
       return  active, inv
print(inventory())