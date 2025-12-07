import random
import json

# Megan Li
# using magic method (__str__)
# using f-strings containing expressions
class Player:
    """Represents a player character.

        Attributes:
            name (str): the player's name
            character_class (str): the player's chosen class (i.e. warrior, etc)
            hp (int): the player's health points
            attack (int): the player's attack strength
            defense (int): the player's defense value
            level (int): the player's current level
            exp (int): the player's current number of EXP
            inventory (list): a list of items that the player's currently holding
            location (int): the player's location in the dungeon
    """
    
    def __init__(self, name, character_class, stats):
        """Initalizes the player's name, character class, and stats

            Args:
                name (str): the player's name
                character_class (str): the player's chosen class
                stats (dict): contains the starting stats for the chosen class
        """
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
        """Produces an informal string representation of the player's starting
        stats before beginning the game
        """
        return(f"{self.name} the {self.character_class.capitalize()} | "
               f"Level: {self.level}, HP: {self.hp}, Attack: {self.attack}, Defense: {self.defense}")
        
def create_character():
    """Asks the user to create a player character
    
        Returns:
            Player: a Player object representing the newly created character
        
        Side effects:
            - Prints instructions to the console for the user
            - Displays the user's starting stats after creation
    """
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

# Create a while loop to keep the player exploring through the dungeon until
# they've defeated all the monsters or die
        
        
        
        
    
    
    
    
    

