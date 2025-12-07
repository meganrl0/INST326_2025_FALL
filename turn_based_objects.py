import random
import json

# Megan Li
def create_character():
    print("Welcome to Turn-Based Objects!")
    name = input("What's your character's name? ").strip().capitalize()
    
    character_classes = {
        "warrior": {"hp": 120, "attack": 10, "defense": 8},
        "mage": {"hp": 90, "attack": 14, "defense": 4},
        "soldier": {"hp": 70, "attack": 18, "defense": 2}
    }
    
    print("\nChoose your class:")
    for character, stats in character_classes.items():
        print(f"- {character.capitalize()} (HP: {stats['hp']}, Attack: {stats['attack']}, Defense: {stats['defense']})")
     
    chosen_class = None
    input_class = ""
    while not chosen_class:
        input_class = input("\nEnter your character class: ").lower()
        chosen_class = character_classes.get(input_class)
        if not chosen_class:
            print("Invalid class. Please try again.")
        else: 
            print(f"You chose {input_class.capitalize()}! Creating your player...\n")
            
    player = {
        "name": name,
        "class": input_class,
        "hp": chosen_class["hp"],
        "attack": chosen_class["attack"],
        "defense": chosen_class["defense"],
        "level": 1,
        "exp": 0,
        "inventory": [],
        "location": 0       
    }
    
    print(f"\nPlayer created! GLHF, {name} the {input_class.capitalize()}!\n")
    return player
        
        
player = create_character()
print(player)

# Create a while loop to keep the player exploring through the dungeon until
# they've defeated all the monsters or die
        
        
        
        
    
    
    
    
    

