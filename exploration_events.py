import random

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
