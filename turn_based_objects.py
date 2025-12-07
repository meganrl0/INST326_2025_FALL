import random
import json

# Megan Li
# using magic method (__str__)
class Player:
    def __init__(self, name, character_class, stats):
        self.name = name
        self.character_class = character_class
        self.hp = stats["hp"]
        self.attack = stats["attack"]
        self.defense = stats["defense"]
        self.level = 1
        self.exp = 0
        self.inventory = []
        self.location = 0
        
    def __str__(self):
        return(f"{self.name} the {self.character_class.capitalize()} | "
               f"Level: {self.level}, HP: {self.hp}, Attack: {self.attack}, Defense: {self.defense}")
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
    
    player = Player(name, input_class, chosen_class)
    
    print(f"\nPlayer created! GLHF, {name} the {player.character_class.capitalize()}!\n")
    print(player)
    return player

if __name__ == "__main__":
    player = create_character()

# Create a while loop to keep the player exploring through the dungeon until
# they've defeated all the monsters or die
        
        
        
        
    
    
    
    
    

