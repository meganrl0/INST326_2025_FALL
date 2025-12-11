import Inventory-Class.py
import character_leveling_system.py
import combat_system.py
import exploration_events.py



def dungeon_loop(player):
    monsters =[
        {"name": "Goblin", "hp": 30, "attack": 10, "exp": 20, "miss_chance": .1},
        {"name": "Bat", "hp": 20, "attack": 15, "exp": 30, "miss_chance": .05},
        {"name": "Slime", "hp": 50, "attack": 5, "exp": 20, "miss_chance": .1},
        {"name": "Minotaur", "hp": 100, "attack": 15, "exp": 50, "miss_chance": .2}
    ]
    
    while player.hp > 0 and monsters:
        current_monster = monsters.pop(0)
        combat_system(player, current_monster)
        if player.hp <= 0:
            print("\nYou died. Game over.")
            return
        
    if not monsters:
        print("\nYou have defeated all the monsters! yay!")
def main():
    player = create_character()
    dungeon_loop(player)

# testing of program together
if __name__ == "__main__":
    # 1. Create player
    player = create_character()

    # 2. Initialize exploration system with 5 rooms
    total_rooms = 5
    explorer = ExplorationSystem(total_rooms)

    print("\n--- Dungeon Exploration Test Begins ---")

    # 3. Explore rooms until the player reaches the final room or dies
    while player.hp > 0 and player.location < total_rooms:
        # Uncomment the next line to require ENTER press each room
        # input("\nPress ENTER to explore the next room...")

        event_type, info = explorer.explore(player)

        if event_type == "monster":
            print(f"Room {player.location}: A {info} appears!")

            # Retrieve monster stats from ExplorationSystem
            monster_stats = explorer.monster_stats[info].copy()  # copy to avoid mutating original
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
