import time
import random
import os
import sys

def typewriterEffect(message):
    if message == "...": #for loadingTexts
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.5)
    else:
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()

            if char != "\n":
                time.sleep(0.05)
            else: #if it's turning into a new line, there should be a longer pause
                time.sleep(1)

def scene1():
    print("\n=======================================================================================")
    print()

    story = """Year 854. \n \n\
Peace has reigned in the heavens and the Earth after 2000 long years of war between angels and devils.\n\
It was peaceful they said, where laughter of children rang, and songs of glory were sung in choirs.\n\
The grass dances with the wind, the birds sing songs of freedom, everything is peaceful.\n\
The cry of a new born baby sounded across the small village. \n\
“IT'S A BOY!” announced by the physician, and everyone clapped and exclaimed their excitement. \n\
A new baby boy was born, not a royal, nor divine, but every birth is celebrated as a baby symbolizes a new hope. \n\
Everyone cheered and celebrated, tears of joy were raining, and everyone was just enormously grateful. \n\
The family was showered with love and support. Everything is peaceful.  \n\
But one shouldn't be blinded by the beauty of it all. \n \n\
In the deep dark forest, remnants of the dead were lingering. Those mortals who were caught between the war of \n\
angels and devils suffered the most gut-wrenching and insufferable consequences. 80%. \n\
It was believed that 80% of the world's population vanished in just a flash. But it was also that same forest where a child, \n\
5 years of age, watched longingly to the joyous village full of happiness.\n\
No one celebrated his birth with him, he was a child abandoned, and only the devil spirits had been the one raising this little lad.\n\
And as the child grew, so did his hatred. And thus, no one should set foot in this forest hidden at the edge of the Earth. \n \n\
Year 875. \n \n\
Eljin had just celebrated his 21st birthday, and his only wish was to explore the world beyond the village's borders.\n\
His parents were worried, of course. No one has ever set foot outside the village, no one dared to see the outside world. \n\
But his courage, and his love for adventures urged him to go forward, and explore more than any human has explored. \n\
After weeks of searching for the unknown, he has finally stumbled upon the deep dark path and decided to move forward.\n \n\
"""

    typewriterEffect(story)

    loadingText = "..."
    typewriterEffect(loadingText)
    print()

    instructions = """INSTRUCTIONS:

1. Explore the island by moving around the map. You can move up [W], down [S], left [A], or right [D].
2. After moving 5 times, combat begins! Prepare for battle.
3. Exchange three attacks with the enemy before you can retreat and leave combat.
4. If you collide with an enemy, the combat mode starts automatically.
5. Keep an eye out for surprises marked with "[?]" on the map. \n 
Colliding with a surprise may affect your HP either negatively or positively. You might also encounter a random enemy so watch out.
6. Watch out for trees marked with "[#]" — you can't collide with them (deerrr).
7. To quit the game, simply input "quit" at any user prompt.

Get ready for an exciting adventure! May you conquer the challenges of the island.
"""

    print(instructions)

    loadIslandMap()



# ISLAND MAP ---->


# INSTRUCTIONS:
# >> WHEN PLAYER MOVES 5 TIMES IN THE MAP, COMBAT BEGINS
# >> PLAYER MUST EXCHANGE THREE ATTACKS WITH THE ENEMY BEFORE THEY CAN RETREAT AND LEAVE COMBAT WITH THE ENEMY
# >> IF THEY COLLIDE WITH THE ENEMY, COMBAT WILL BEGIN
# >> inform the user about the symbol surprise
# >> [?] surprise: if user collides with "?", they will be given something, which will either increase or decrease their HP
# >> [#] means trees, basically (deerrr) (they can't collide with these)
# >> print instruction first before the game begins
# >> It should mention that if users want to quit, they should just input "quit" for every user prompt

global inGame
inGame = True

# Define map symbols at the global level
symbols = {
    'ground': '.',
    'boundary': ',',
    'trace': '"',
    'tree': '#',
    'surprise': '?',
    'player': '✌️',
    'enemy': '☠️'
}

# Player and enemy initial stats
player_stats = {'hp': 100}
enemy_stats = {'hp': 100}

def generate_island_map(width, height):

    # Initialize the map with ground
    island_map = [['ground' for _ in range(width)] for _ in range(height)]

    # Add boundaries around the island
    for i in range(height):
        island_map[i][0] = 'boundary'
        island_map[i][width - 1] = 'boundary'
    for j in range(width):
        island_map[0][j] = 'boundary'
        island_map[height - 1][j] = 'boundary'

    # Add some trace to character movement
    for _ in range(10):
        x = random.randint(1, width - 2)
        y = random.randint(1, height - 2)
        island_map[y][x] = 'trace'

    # Add trees
    for _ in range(50):
        x = random.randint(1, width - 2)
        y = random.randint(1, height - 2)
        island_map[y][x] = 'tree'

    # Add "surprise"
    for _ in range(20):
        x = random.randint(1, width - 2)
        y = random.randint(1, height - 2)
        island_map[y][x] = 'surprise'

    # Add the player
    player_x = random.randint(1, width - 2)
    player_y = random.randint(1, height - 2)
    island_map[player_y][player_x] = 'player'

    # Add the enemy
    enemy_x = random.randint(1, width - 2)
    enemy_y = random.randint(1, height - 2)
    island_map[enemy_y][enemy_x] = 'enemy'

    return island_map, player_x, player_y, enemy_x, enemy_y

def print_island_map(island_map):
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console

    # Print the map with borders
    print('+' + '-' * (len(island_map[0]) * 2 - 1) + '+')
    for row in island_map:
        print('|' + ' '.join(symbols[cell] for cell in row) + '|')
    print('+' + '-' * (len(island_map[0]) * 2 - 1) + '+')

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
    print(f"\n>>> ENEMY ATTACKS! You take [{damage}] damage.")
    
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

    choice = input("  What's your attack?: ")

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

def move_player(island_map, player_x, player_y, enemy_x, enemy_y, direction, move_counter):
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
    island_map[player_y][player_x] = 'trace'
    island_map[enemy_y][enemy_x] = 'trace'

    #as long as the direction upon which the player is going to is not close to tree or the enemy...
    if direction == 'w' and player_y > 1 and island_map[player_y - 1][player_x] != 'tree' and island_map[player_y - 1][player_x] != 'enemy':
        if island_map[player_y - 1][player_x] == 'surprise':
            surprise_event = True
            #if the player moves and it's close to '?' symbol, it will trigger a surprise event by setting its value to True
        if island_map[player_y - 1][player_x] == 'enemy':
            combat(player_stats, enemy_stats)
            #if the player moves and it's close to the enemy, it will start the battle
        new_y -= 1
    elif direction == 's' and player_y < len(island_map) - 2 and island_map[player_y + 1][player_x] != 'tree' and island_map[player_y + 1][player_x] != 'enemy':
        if island_map[player_y + 1][player_x] == 'surprise':
            surprise_event = True
        if island_map[player_y + 1][player_x] == 'enemy':
            combat(player_stats, enemy_stats)
        new_y += 1
    elif direction == 'a' and player_x > 1 and island_map[player_y][player_x - 1] != 'tree' and island_map[player_y][player_x - 1] != 'enemy':
        if island_map[player_y][player_x - 1] == 'surprise':
            surprise_event = True
        if island_map[player_y][player_x - 1] == 'enemy':
            combat(player_stats, enemy_stats)
        new_x -= 1
    elif direction == 'd' and player_x < len(island_map[0]) - 2 and island_map[player_y][player_x + 1] != 'tree' and island_map[player_y][player_x + 1] != 'enemy':
        if island_map[player_y][player_x + 1] == 'surprise':
            surprise_event = True
        if island_map[player_y][player_x + 1] == 'enemy':
            combat(player_stats, enemy_stats)
        new_x += 1
    elif direction == 'quit':
        print("Redirecting to the the main menu", end="")
        loading = "..."
        typewriterEffect(loading)
        input("Press enter to continue...")

        inGame = False

    island_map[new_y][new_x] = 'player'

    # Move the enemy towards the player
    if enemy_x < new_x and island_map[enemy_y][enemy_x + 1] != 'player':
        if island_map[enemy_y - 1][enemy_x] == 'player':
            combat(player_stats, enemy_stats)
        enemy_x += 1
    elif enemy_x > new_x and island_map[enemy_y][enemy_x - 1] != 'player':
        if island_map[enemy_y + 1][enemy_x] == 'enemy':
            combat(player_stats, enemy_stats)
        enemy_x -= 1
    elif enemy_y < new_y and island_map[enemy_y + 1][enemy_x] != 'player':
        if island_map[enemy_y][enemy_x - 1] == 'enemy':
            combat(player_stats, enemy_stats)
        enemy_y += 1
    elif enemy_y > new_y and island_map[enemy_y - 1][enemy_x] != 'player':
        if island_map[enemy_y][enemy_x + 1] == 'enemy':
            combat(player_stats, enemy_stats)
        enemy_y -= 1

    island_map[enemy_y][enemy_x] = 'enemy'

    if surprise_event:
        surprise = {
        'Health Potion': 20,
        'Lucky Charm': 5,
        'Venomous Snakes': -10,
        'Cursed Relic': -20,
        'Minion of the Enemy Boss' : -40,
        'Nothing': 0
        }

        surprise_list = ("Health Potion", "Lucky Charm", "Venomous Snakes", "Cursed Relic", "Minion of the Enemy Boss", "Nothing")

        input("You reached a surprise area. Press enter to see what you got...")
        random_surprise = random.choice(surprise_list)
        
        
        if random_surprise in surprise:
            if surprise[random_surprise] >= 0:
                input(f"You got {random_surprise}! That's worth {surprise[random_surprise]} points of HP!")
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

    return island_map, new_x, new_y, enemy_x, enemy_y, move_counter


def loadIslandMap():
    if inGame:
        #print instructions here

        # Set the size of the map
        map_width = 25
        map_height = 15

        # Generate the initial map and player position
        island_map, player_x, player_y, enemy_x, enemy_y = generate_island_map(map_width, map_height)

        # Main game loop
        move_counter = 0

    while inGame:
        # Print the map
        print_island_map(island_map)

        # Get user input for movement
        move_direction = input("Where do you want to go? (W/A/S/D): ").lower()

        # Move the player, enemy, and handle events
        island_map, player_x, player_y, enemy_x, enemy_y, move_counter = move_player(
            island_map, player_x, player_y, enemy_x, enemy_y, move_direction, move_counter
        )

        if not inGame:
            input("Press enter to return to go back to Main Menu...")
            import main
            main

            break
            # should go to main menu
