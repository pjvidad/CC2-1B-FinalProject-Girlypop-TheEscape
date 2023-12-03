import random
import time
import os
from scene_1 import typewriterEffect


def scene2():
    print("\n=======================================================================================")
    print()

    story = """Exhausted and bloodied, Eljin stood still with a beam and unwavering resolve, his passion continuing to burn brighter than it ever did.\n\
With his newly founded [ insert weapon or skills ], he ventured the deep unknown courageously. As the sun began to set and the sky gradually dims the sounds of horror from unknown creatures rang throughout the zone.\n\
Eljin looked up the dark blue sky glittered with twinkling stars, and the Aurora Borealis in sight, he paused for a moment to reminisce the memories with the people in his small village, and it is the first time in his 21 years of life that he had longed for his parents’ touch.\n\
In a shallow cave, guarded by gigantic trees, its shadows serving as protection, he set up his tent that will serve as his home for the next few months.\n\
In the middle of nowhere, the smell of freshly made fried chicken surrounded the area, and warmth began to embrace our hero. And as the moon beams, Eljin slowly drifts to sleep.\n\
But the night did not end just there. In the dark forest comes Jephomet.\n\
“How amusing. A young lad taking a soundly slumber in my own den. Tsk. Looks like someone is looking for trouble.” Jephomet smirked and casted a spell on the sleeping lad.\n\
Soon, he found himself in a new environment, confused and dazed, he looked around trying to study the new place he teleported to. Dazzling water springs, heavenly music, and flower paths surrounded our hero.\n\
“Where…-” The Earth rumbled, walls started to form from the ground, and suddenly, the heavenly site was replaced with horror.\n \n\
Help Eljin find his way out of this hellish rumble. """

    typewriterEffect(story)

    loadingText = "..."
    typewriterEffect(loadingText)
    print()

    instructions = """\nINSTRUCTIONS:

1. Explore the island by moving around the map. You can move up [W], down [S], left [A], or right [D].
2. After moving 5 times, combat begins! Prepare for battle.
3. Exchange three attacks with the enemy before you can retreat and leave combat.
4. If you collide with an enemy, the combat mode starts automatically.
5. Keep an eye out for surprises marked with "[?]" on the map. \n 
Colliding with a surprise may affect your HP either negatively or positively. You might also encounter a random enemy so watch out.
6. Watch out for walls marked with "[|]" and rooms with the symbol "[R]" — you can't collide with them.
7. To quit the game, simply input "quit" at any user prompt.

Get ready for an exciting adventure! May you conquer the challenges of the enigmatic castle.

[ @  ] - player
[ ️X  ] - enemy
"""
    print(instructions)
    input("\nPress enter to continue...")
    
    loadCastleMap()



# CASTLE MAP ---->



# THINGS TO BE REVISED FOR CASTLEMAP:
# >> Change the surprise events
# >> Change the attacks of the player if u want
# >> You can opt to change the values that each attacks deduct to the enemy
# >> Show rules first beforehand
# >> It should mention that if users want to quit, they should just input "quit" for every user prompt

global inGame
inGame = True

# Define map symbols at the global level
symbols = {
    'ground': '.',
    'boundary': ',',
    'trace': '"',
    'room': 'R',
    'surprise': '?',
    'player': '@',
    'enemy': '️X',
    'wall': '|',
}

# Player and enemy initial stats
player_stats = {'hp': 100}
enemy_stats = {'hp': 100}

def generate_castle_map(width, height):

    # Initialize the map with ground
    castle_map = [['ground' for _ in range(width)] for _ in range(height)]

    # Add boundaries around the map
    for i in range(height):
        castle_map[i][0] = 'boundary'
        castle_map[i][width - 1] = 'boundary'
    for j in range(width):
        castle_map[0][j] = 'boundary'
        castle_map[height - 1][j] = 'boundary'

    # Add some trace to character movement
    for _ in range(10):
        x = random.randint(1, width - 2)
        y = random.randint(1, height - 2)
        castle_map[y][x] = 'trace'

    # Add rooms
    for _ in range(30):
        x = random.randint(1, width - 2)
        y = random.randint(1, height - 2)
        castle_map[y][x] = 'room'

    # Add "surprise"
    for _ in range(15):
        x = random.randint(1, width - 2)
        y = random.randint(1, height - 2)
        castle_map[y][x] = 'surprise'

    # Add walls
    for _ in range(15):
        wall_length = random.randint(3, 6)
        orientation = random.choice(['horizontal', 'vertical'])
        wall_start_x = random.randint(1, width - wall_length - 1)
        wall_start_y = random.randint(1, height - wall_length - 1)

        if orientation == 'horizontal':
            for i in range(wall_length):
                castle_map[wall_start_y][wall_start_x + i] = 'wall'
        else:
            for i in range(wall_length):
                castle_map[wall_start_y + i][wall_start_x] = 'wall'

    # Add the player
    player_x = random.randint(1, width - 2)
    player_y = random.randint(1, height - 2)
    castle_map[player_y][player_x] = 'player'

    # Add the enemy
    enemy_x = random.randint(1, width - 2)
    enemy_y = random.randint(1, height - 2)
    castle_map[enemy_y][enemy_x] = 'enemy'

    return castle_map, player_x, player_y, enemy_x, enemy_y

def print_castle_map(castle_map):
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console

castle_map = [
    # Your castle map rows go here
]

legend_items = {
    "Player": "[@]",
    "Enemy": "[☠️]",
    "Surprise": "[?]",
    "Tree": "[#]",
    "Boundary": "[,]",
    "Room": "R",
    "Wall": "|",
}

def display_legend():
    print("\nMap Legends:")
    for item, symbol in legend_items.items():
        print(f"{item}: {symbol}")

display_legend()

    # Print the map with borders
    print('+' + '-' * (len(castle_map[0]) * 2 - 1) + '+')
    for row in castle_map:
        print('|' + ' '.join(symbols[cell] for cell in row) + '|')
    print('+' + '-' * (len(castle_map[0]) * 2 - 1) + '+')

def enemy_attack(player_stats, enemy_stats):
    global inGame

    # Simulate enemy attacking player
    damage = random.randint(15, 25) #the damage the enemy inflict on you will be between 15 to 30
    player_stats['hp'] -= damage

    print()

    loading = "..."
    typewriterEffect(loading)

    time.sleep(1)

    print()
    print(f"\n>> ENEMY ATTACKS! You take [{damage}] damage.")
    
    time.sleep(1)

    print()
    print(" ================ ")
    print("||  HP STATUS:  ||")
    print(" ================ ")
    print(f"Your remaining HP: [{player_stats['hp']}]")
    print(f"Enemy HP: [{enemy_stats['hp']}]")

    if player_stats['hp'] <= 0:
        print()
        print(" ======================================== ")
        print("||  You have been defeated. GAME OVER.  ||")
        print(" ======================================== ")
        inGame = False

def player_attack(enemy_stats):
    global inGame

    print()
    print("+--------------------------------+")
    print("|       Choose your attack       |")
    print("+--------------------------------+")
    print("  1.        Chi Strike            ")
    print("  2.   Artificial Hand Blast      ")
    print("  3.    Baseball Bat Attack       ")
    print("  4      Berserker Combat         ")
    print("+--------------------------------+")

    choice = input("  Enter number: ")

    if choice == '1':
        #chi strike
        damage = random.randint(10, 20)
        enemy_stats['hp'] -= damage
        print(f"\n>> You attacked with Chi Strike! Enemy takes [{damage}] damage.")
    elif choice == '2':
        #artificial hand blast
        damage = random.randint(5, 10)
        enemy_stats['hp'] -= damage
        print(f"\n>> You attacked with Articifical Hand Blast! Enemy takes [{damage}] damage.")
    elif choice == '3':
        #baseball bat attack
        damage = random.randint(5, 10)
        enemy_stats['hp'] -= damage
        print(f"\n>> You attacked with Baseball Bat Attack! Enemy takes [{damage}] damage.")
    elif choice == '4':
        #berserker combat
        damage = random.randint(15, 25)
        enemy_stats['hp'] -= damage
        print(f"\n>> You attacked with Berserker Combat! Enemy takes [{damage}] damage.")
    elif choice == 'quit':
        print()
        print("Redirecting to the the main menu", end="")
        loading = "..."
        typewriterEffect(loading)
        print()
        input("Press enter to continue. ")

        import main
        main
        
        inGame = False
    else:
        print("\n!!! Invalid choice. You missed the attack. !!!")
    
    time.sleep(1)

    # display HP stats after the player attacks
    print()
    print(" ================ ")
    print("||  HP STATUS:  ||")
    print(" ================ ")
    print(f"Your remaining HP: [{player_stats['hp']}]")
    print(f"Enemy HP: [{enemy_stats['hp']}]") 


def combat(player_stats, enemy_stats):
    global inGame
    print()
    print(">>>>> Battle starts! <<<<<")

    player_attack_count = 0  # Counter for player attacks

    while True:
        player_attack(enemy_stats)
        player_attack_count += 1
        # after attacking the enemy, increase player_attack_count
        # when it reaches 3 or the player has attacked the enemy thrice, they should be able to retreat

        if player_attack_count >= 3:
            print()
            print(" ================================")
            print("||  You successfully retreated!  ||")
            print(" ================================")
            input("Press enter to continue...")
            print("\n")
            break

        if enemy_stats['hp'] <= 0:
            print()
            print(" ============================================ ")
            print("||  You defeated the enemy. CONGRATULATIONS! ||")
            print(" ============================================ ")
            print("\n")
            
            inGame = False
            break

        # Simulate enemy's turn
        enemy_attack(player_stats, enemy_stats)

        if player_stats['hp'] <= 0:
            print()
            print(" ======================================== ")
            print("||  You have been defeated. GAME OVER.  ||")
            print(" ======================================== ")
            print("\n")
            
            inGame = False
            break


def move_player(castle_map, player_x, player_y, enemy_x, enemy_y, direction, move_counter):
    global inGame

    #for every move of the player, check if the enemy's hp falls below 0
    if enemy_stats['hp'] <= 0:
            print()
            print(" ============================================== ")
            print("||  You defeated the enemy. CONGRATULATIONS!  ||")
            print(" ==============================================  ")
            print("\n")
            
            inGame = False

    #for every move of the player, check if the player's hp falls below 0
    if player_stats['hp'] <= 0:
            print()
            print(" ======================================== ")
            print("||  You have been defeated. GAME OVER.  ||")
            print(" ======================================== ")
            print("\n")
            
            inGame = False

    new_x, new_y = player_x, player_y
    surprise_event = False

    # Replace previous positions with 'trace'
    castle_map[player_y][player_x] = 'trace'
    castle_map[enemy_y][enemy_x] = 'trace'

    #as long as the direction upon which the player is going to is not to rooms, walls, or the enemy, they can move
    if direction == 'w' and player_y > 1 and castle_map[player_y - 1][player_x] != 'room' and player_y > 1 and castle_map[player_y - 1][player_x] != 'wall' and castle_map[player_y - 1][player_x] != 'enemy':
        if castle_map[player_y - 1][player_x] == 'surprise':
            surprise_event = True
            #if the player moves and it's close to '?' symbol, it will trigger a surprise event by setting its value to True
        if castle_map[player_y - 1][player_x] == 'enemy':
            combat(player_stats, enemy_stats)
            #if the player moves and it's close to the enemy, it will start the battle
        new_y -= 1
    elif direction == 's' and player_y < len(castle_map) - 2 and castle_map[player_y + 1][player_x] != 'room' and castle_map[player_y + 1][player_x] != 'wall' and castle_map[player_y + 1][player_x] != 'enemy':
        if castle_map[player_y + 1][player_x] == 'surprise':
            surprise_event = True
        if castle_map[player_y + 1][player_x] == 'enemy':
            combat(player_stats, enemy_stats)
        new_y += 1
    elif direction == 'a' and player_x > 1 and castle_map[player_y][player_x - 1] != 'room' and castle_map[player_y][player_x - 1] != 'wall' and castle_map[player_y][player_x - 1] != 'enemy':
        if castle_map[player_y][player_x - 1] == 'surprise':
            surprise_event = True
        if castle_map[player_y][player_x - 1] == 'enemy':
            combat(player_stats, enemy_stats)
        new_x -= 1
    elif direction == 'd' and player_x < len(castle_map[0]) - 2 and castle_map[player_y][player_x + 1] != 'room' and castle_map[player_y][player_x + 1] != 'wall' and castle_map[player_y][player_x + 1] != 'enemy':
        if castle_map[player_y][player_x + 1] == 'surprise':
            surprise_event = True
        if castle_map[player_y][player_x + 1] == 'enemy':
            combat(player_stats, enemy_stats)
        new_x += 1
    elif direction == 'quit':
        print("Redirecting to the the main menu", end="")
        loading = "..."
        typewriterEffect(loading)
        input("Press enter to continue...")

        inGame = False


    castle_map[player_y][player_x] = 'ground'
    castle_map[new_y][new_x] = 'player'


    # Move the enemy towards the player
    if enemy_x < new_x and castle_map[enemy_y][enemy_x + 1] != 'player':
        if castle_map[enemy_y - 1][enemy_x] == 'player':
            combat(player_stats, enemy_stats)
        enemy_x += 1
    elif enemy_x > new_x and castle_map[enemy_y][enemy_x - 1] != 'player':
        if castle_map[enemy_y + 1][enemy_x] == 'enemy':
            combat(player_stats, enemy_stats)
        enemy_x -= 1
    elif enemy_y < new_y and castle_map[enemy_y + 1][enemy_x] != 'player':
        if castle_map[enemy_y][enemy_x - 1] == 'enemy':
            combat(player_stats, enemy_stats)
        enemy_y += 1
    elif enemy_y > new_y and castle_map[enemy_y - 1][enemy_x] != 'player':
        if castle_map[enemy_y][enemy_x + 1] == 'enemy':
            combat(player_stats, enemy_stats)
        enemy_y -= 1

    castle_map[enemy_y][enemy_x] = 'enemy'

    # change these surprise events for castleMap
    if surprise_event:
        surprise = {
        'Health Potion': 20,
        'Lucky Charm': 5,
        'Venomous Snakes': -5,
        'Cursed Relic': -10,
        'Minion of the Enemy Boss' : -20,
        'Nothing': 0
        }

        surprise_list = ("Health Potion", "Lucky Charm", "Venomous Snakes", "Cursed Relic", "Minion of the Enemy Boss", "Nothing")

        input("You reached a surprise area. Press enter to see what you got...")
        random_surprise = random.choice(surprise_list)
        
        
        if random_surprise in surprise:
            if surprise[random_surprise] >= 0:
                input(f"You got {random_surprise}! That's worth {surprise[random_surprise]} points of HP!")
                player_stats['hp'] += surprise[random_surprise]
            elif surprise[random_surprise] < 0:
                input(f"Oh no! You encountered a {random_surprise}! That's worth {surprise[random_surprise]} points of HP!")
                player_stats['hp'] += surprise[random_surprise]



    # Check for combat every 5 moves
    move_counter += 1
    if move_counter % 5 == 0:
        print("\n=======================================================================================")
        print()
        print(">>>   COMBAT BEGINS!  <<<")
        print()
        print("    ================     ")
        print("   ||  HP STATUS:  ||    ")
        print("    ================     ")
        print(f"  Your remaining HP: [{player_stats['hp']}]")
        print(f"  Enemy HP: [{enemy_stats['hp']}]")
        
        combat(player_stats, enemy_stats)

    return castle_map, new_x, new_y, enemy_x, enemy_y, move_counter


def loadCastleMap():
    if inGame:
        # Set the size of the map
        map_width = 25
        map_height = 15

        # Generate the initial map and player position
        castle_map, player_x, player_y, enemy_x, enemy_y = generate_castle_map(map_width, map_height)

        move_counter = 0


    while inGame:
        # Print the map
        print_castle_map(castle_map)

        # Get user input for movement
        move_direction = input("Where do you want to go? (W/A/S/D): ").lower()

        # Move the player and handle events
        castle_map, player_x, player_y, enemy_x, enemy_y, move_counter = move_player(
            castle_map, player_x, player_y, enemy_x, enemy_y, move_direction, move_counter
        )

        if not inGame:
            input("Press enter to return to Main Menu...")
            import main
            main

            break
            # should go to main menu
