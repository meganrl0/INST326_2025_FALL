from argparse import ArgumentParser
import random

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
        self.inventory = Inventory()
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
        "warrior": {"hp": 120, "attack": 10, "defense": 8, "inventory": "iron sword"},
        "mage": {"hp": 90, "attack": 14, "defense": 4, "inventory": "strength potion"},
        "soldier": {"hp": 70, "attack": 18, "defense": 2, "inventory": "steel dagger"}
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

class Inventory:
    """Instantiates an object of the inventory class."""
    def __init__(self, active=[None], inv=[None, None, None, None, None,]):
        self.inv = inv
        self.active = active
        
    def add_item(self, item):
        """adds item to the inventory.
        Args: item (str) the item to be added.
        Side Effects, changes a None value in the inventory to item."""
        track_num = 1
        for i in self.active:
            iter = self.active[i]
            if iter == None:
                self.active[i] = item
                track_num -= 1
                break
        if track_num == 1:
            for j in self.inv:
                if self.inv[j] == None:
                    self.inv[j] = item
                    track_num -= 1
                    
    def subtract_item(self, item):
        """Subtracts item to the inventory.
        Args: item (str) the item to be removed.
        Returns item (str)
        Side Effects, changes a item value in the inventory to None."""
        track_num = 1
        for i in self.active:
            iter = self.active[i]
            if iter == item:
                self.active[i] = None
                track_num -= 1
                return iter
        for j in self.inv:
            if track_num == 0:
                break
            else:
                ret = self.inv[j]
                self.inv[j] = None
                track_num -= 1
                return ret
                
    def stack_item(self, item, n):
        """Takes duplicate items and stacks the together.
        Args: item (str) the stackable item, n (int) the amount of copies of the
        item are being stacked on to the original.
        Side Effects, increases the number of duplicate items in a stack
        represented by ("item name", xn)"""
        for i in self.active and self.inv:
            if self.active[i] == item:
                self.active[i] = item + " x" + n
            elif self.inv[i] == item:
                self.inv[i] = item + " x" + n
    def __str__(self):
        """Converts the active and inv into string representations of themselves."""
        return f"Active: {self.active} \nBag: {self.inv}"
                
class Item:
    """creates an object of the item class."""
    def __init__(self, name, description, actions, stackable=False):
        """Instantiates an item object.
        Attributes: name(str) the name of the object, description (str) a
        description of the item, its function and its lore, actions (list)
        of things that the item can be used for and the effects of such actions,
        stackable(bool) whether or not multiple copies of the item can occupy
        one inventory slot with the default value being False."""
        self.name = name
        self.description = description
        self.actions = actions
        self.stackable = stackable
        
    def use_item(self, action):
        """Accesses item's actions attributes to enact a use of that item.
        Args: action(list) a action that the item can be used for and its
        effects (example: consumables like healing potions can be consumed to
        restore health which deleats that instance of the item from the
        inventory).
        Returns: the effect(s) of that item's action."""
        if action in self.actions:
            return action[1]

exp_bar = [0, 50, 100, 175, 275, 400, 550, 725, 925, 1150]

character_growth = {
    "warrior": {"hp": 20, "attack": 6, "defense": 3},
    "mage": {"hp": 10, "attack": 5, "defense": 2},
    "soldier": {"hp": 15, "attack": 4, "defense": 1}
}

def level_up(player):
    """Checks if the player has enough EXP to level up
    
        Args:
            player (Player): the player object whose EXP and stats will be
            updated accordingly
            
        Returns:
            boolean: True if the player has leveled up at least once, False
            otherwise 
    """
    leveled_up = False
    growth = character_growth[player.character_class]
    
    while player.level < len(exp_bar) - 1 and player.exp >= exp_bar[player.level]:
        player.exp -= exp_bar[player.level]
        player.level += 1
        leveled_up = True
        
        player.hp += growth["hp"]
        player.attack += growth["attack"]
        player.defense += growth["defense"]
        
        print("\nLEVEL UP!")
        print(f"{player.name} reached Level {player.level}!")
        print("Stat increases:")
        print(f"  +{growth['hp']} HP to {player.hp}")
        print(f"  +{growth['attack']} Attack to {player.attack}")
        print(f"  +{growth['defense']} Defense to {player.defense}")
        
    return leveled_up

# Exploration System by Danish Malik
class ExplorationSystem:
    """
    Handles dungeon exploration and all random events that occur
    when a player enters a new room, including item discovery,
    monster encounters, and empty rooms.
    """

    def __init__(self, total_rooms):
        """
        Instantiates an ExplorationSystem object.

        Args:
            total_rooms (int): The total number of rooms in the dungeon.
        """
        self.total_rooms = total_rooms

        # Event probabilities
        self.event_table = {
            "Goblin": 0.25,
            "Bat": 0.15,
            "Slime": 0.2,
            "Minotaur": 0.05,
            "Healing Potion": 0.2,
            "Strength Potion": 0.1,
            "Iron Sword": 0.025,
            "Steel Dagger": 0.025,
            "Nothing": 0.05
        }

        # Normalize probabilities to sum to 1
        total = sum(self.event_table.values())
        self.event_table = {k: v / total for k, v in self.event_table.items()}

        # Monster stats
        self.monster_stats = {
            "Goblin": {"name": "Goblin", "hp": 30, "attack": 10, "exp": 20, "miss_chance": 0.1},
            "Bat": {"name": "Bat", "hp": 20, "attack": 15, "exp": 30, "miss_chance": 0.05},
            "Slime": {"name": "Slime", "hp": 50, "attack": 5, "exp": 20, "miss_chance": 0.1},
            "Minotaur": {"name": "Minotaur", "hp": 100, "attack": 15, "exp": 50, "miss_chance": 0.2}
        }

    def explore(self, player):
        """
        Moves the player forward by one room and determines what event 
        occurs based on weighted probabilities.

        Args:
            player (Player): The player object whose location will be 
            updated and who may encounter monsters or find items.

        Returns:
            tuple(str, str): A tuple containing:
                - event type ("monster", "item", "nothing")
                - a description or name associated with that event"""
        player.location += 1

        # Check if player reached the final room
        if player.location > self.total_rooms:
            player.location = self.total_rooms
            return "nothing", "You reached the final room!"

        # Choose a random event based on probabilities
        event = random.choices(list(self.event_table.keys()), list(self.event_table.values()))[0]

        # Handle monster encounter
        if event in self.monster_stats:
            return "monster", event

        # Handle item discovery
        elif "Healing" in event:
            player.inventory.add_item(Item("Healing Potion", "Consumable: increases HP"))
            return "item", f"You found a {event}!"
        elif "Strength" in event:
            player.inventory.add_item(Item("Strength Potion", "Consumable: Increases Attack Damage"))
            return "item", f"You found a {event}!"
        elif "Sword" in event:
            player.inventory.add_item(Item("Iron Sword", "Attack"))
            return "item", f"You found a {event}!"
        elif "Dagger" in event:
            player.inventory.add_item(Item("Steel Dagger", "Attack"))
            return "item", f"You found a {event}!"

        # Handle empty rooms
        else:
            return "nothing", "Nothing happens in this room."

def combat_system(player, monster):
    """ creates a turn-based combat system between the player and a monster
    
    Args:
        player:  players stats
        monster(dict): a dict that contains the monsters stats
        
    Returns:
        None: updates players dict and gives live combat messages
    """
    print(f"\nA wild {monster['name']} has appeared!")
    while player.hp > 0 and monster["hp"] > 0:
        option = input("\nChoose one of the following: [A]ttack, " \
            "[I]nventory\n").lower()
    
        if option == 'a':
            critical_hit = random.choice([1, 1, 1, 2])
            dmg = player.attack * (2 if critical_hit == 2 else 1) # conditional expression
            monster["hp"] -= dmg
            if critical_hit == 2:
                print(f"\nYou landed a critical hit! You dealt {dmg} "
                      "damage!")
            else:
                print(f"\nYou dealt {dmg} damage!")
        elif option == "i":
            Inventory.use_item(player)
            print("placeholder")
            continue
        else:
            print("Invalid option.")
            continue
        if monster["hp"] <= 0:
            print(f"\nYou have slain the {monster['name']}!")
            player.exp += monster['exp']
            print(f"{monster['exp']} exp was accquired from the {monster['name']}")
            
            level_up(player)
            
            break
        
        print(f"\nThe {monster['name']} will now strike!")
        if random.random() < monster['miss_chance']:
            print(f"The {monster['name']} missed!")
        else:
            dmg = monster['attack']
            player.hp -= dmg
            print(f"The {monster['name']} has dealt {dmg} damage")
            f"{'!' if dmg > 0 else '... he missed...'}" # conditional expression
        if player.hp <= 0:
            print("\nYou have been killed...")         
            break

def dungeon_loop(player):
    """
    controls the dungeon progression by putting the player against different
    monsters and events
    
    Args:
        player (Player): player object in dungeon
    Returns:
        None: runs combat encounters and prints messages. Loop end if the player
        is dead
    """
    monsters =[
        {"name": "Goblin", "hp": 30, "attack": 10, "exp": 20, "miss_chance": .1},
        {"name": "Bat", "hp": 20, "attack": 15, "exp": 30, "miss_chance": .05},
        {"name": "Slime", "hp": 50, "attack": 5, "exp": 20, "miss_chance": .1},
        {"name": "Minotaur", "hp": 100, "attack": 15, "exp": 50, "miss_chance": .2}
    ]
    monsters.sort(key=lambda m: m["hp"])
    
    while player.hp > 0 and monsters:
        current_monster = monsters.pop(0)
        combat_system(player, current_monster)
        if player.hp <= 0:
            print("\nYou died. Game over.")
            return
        
    if not monsters:
        print("\nYou have defeated all the monsters! yay!")
        
def main():
    # 1. Create player
    player = create_character()
    
     # 2. Initialize exploration system with 5 rooms
    total_rooms = 5
    explorer = ExplorationSystem(total_rooms)

    print("\n--- Dungeon Exploration Test Begins ---")
    
    # 3. Explore rooms until the player reaches the final room or dies
    while player.hp > 0 and player.location < total_rooms:
        event_type, info = explorer.explore(player)
        
        if event_type == "monster":
            print(f"Room {player.location}: A  {info} appears!")
            # Retrieve monster stats from ExplorationSystem
            # copy to avoid mutating original
            monster_stats = explorer.monster_stats[info].copy()
            combat_system(player, monster_stats)
            
        elif event_type == "item":
            print(f"Room {player.location}: {info}")
        else:
            print(f"Room {player.location}: {info}")
        
        # Display player status after each room    
        print(f"Player HP: {player.hp}")
        print(f"Inventory: {player.inventory}")
        
    # End of dungeon
    if player.hp > 0:
        print("\nYou have reached the final room of the dungeon!")
        print(f"Final Inventory: {player.inventory}")
    else:
        print("\nGame over. You died in the dungeon.")

def parse_args(command):
    """Allows command line arguments.
    Args: command(str)
    Returns: parsed arguments in command."""
    parser = ArgumentParser()
    parser.add_argument("name", help="Please enter your character's name.")
    parser.add_argument("character class", help="Please Enter your character's class")
    parser.add_argument("number of rooms", help="Please enter the amount of rooms you want to go through.")
return parser.parse_args(command)

if __name__ == "__main__":
    main()
