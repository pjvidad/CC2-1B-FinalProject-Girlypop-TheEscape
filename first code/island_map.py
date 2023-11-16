import random
import os

# Define map symbols at the global level
#when player reaches these symbols, descriptions of the places will be printed and an event will take place
symbols = {
    'water': '.',
    'beach': ',',
    'grass': '"',
    'forest': '#',
    'mountain': '^',
    'player': '⊗'
}

def generate_island_map(width, height):
    # Initialize the map with water
    island_map = [['water' for _ in range(width)] for _ in range(height)]

    # Add beach around the island
    for i in range(height):
        island_map[i][0] = 'beach'
        island_map[i][width - 1] = 'beach'
    for j in range(width):
        island_map[0][j] = 'beach'
        island_map[height - 1][j] = 'beach'

    # Add some grassy areas
    for _ in range(10):
        x = random.randint(1, width - 2)
        y = random.randint(1, height - 2)
        island_map[y][x] = 'grass'

    # Add forests
    for _ in range(20):
        x = random.randint(1, width - 2)
        y = random.randint(1, height - 2)
        island_map[y][x] = 'forest'

    # Add mountains
    for _ in range(5):
        x = random.randint(1, width - 2)
        y = random.randint(1, height - 2)
        island_map[y][x] = 'mountain'

    # Add the player
    player_x = random.randint(1, width - 2)
    player_y = random.randint(1, height - 2)
    island_map[player_y][player_x] = 'player'

    return island_map, player_x, player_y

def print_island_map(island_map):
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console

    # Print the map with borders
    print('+' + '-' * (len(island_map[0]) * 2 - 1) + '+')
    for row in island_map:
        print('|' + ' '.join(symbols[cell] for cell in row) + '|')
    print('+' + '-' * (len(island_map[0]) * 2 - 1) + '+')

def move_player(island_map, player_x, player_y, direction):
    new_x, new_y = player_x, player_y

    if direction == 'w' and player_y > 1:
        new_y -= 1
    elif direction == 's' and player_y < len(island_map) - 2:
        new_y += 1
    elif direction == 'a' and player_x > 1:
        new_x -= 1
    elif direction == 'd' and player_x < len(island_map[0]) - 2:
        new_x += 1

    island_map[player_y][player_x] = 'grass'
    island_map[new_y][new_x] = 'player'

    return island_map, new_x, new_y


def loadMap():
    # Set the size of the map
    map_width = 30
    map_height = 20

    # Generate the initial map and player position
    island_map, player_x, player_y = generate_island_map(map_width, map_height)

    # Main game loop
    while True:
        # Print the map
        print_island_map(island_map)

        # Get user input for movement
        move_direction = input("Enter movement direction (W/A/S/D): ").lower()

        # Move the player
        island_map, player_x, player_y = move_player(island_map, player_x, player_y, move_direction)
