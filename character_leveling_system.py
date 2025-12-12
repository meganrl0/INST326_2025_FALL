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