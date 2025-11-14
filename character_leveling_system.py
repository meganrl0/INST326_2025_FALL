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