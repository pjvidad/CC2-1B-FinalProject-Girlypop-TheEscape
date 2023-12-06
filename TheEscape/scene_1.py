import time, random, os, sys

class Typewriter:
    @staticmethod
    def type_effect(message):
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

def story():
    print("\n=======================================================================================")
    print()

    while(True):
        skip_story = input("Island Game loaded. Do you want to skip the story? [Y/N] ").lower()

        if skip_story == 'n':

            story1 = """\n \nYear 854.

Peace has reigned in the heavens and the Earth after 2000 long years of war between angels and devils.
It was peaceful they said, where laughter of children rang, and songs of glory were sung in choirs.
The grass dances with the wind, the birds sing songs of freedom, everything is peaceful.
The cry of a new born baby sounded across the small village.
“IT'S A BOY!” announced by the physician, and everyone clapped and exclaimed their excitement.
A new baby boy was born, not a royal, nor divine, but every birth is celebrated as a baby symbolizes a new hope.
Everyone cheered and celebrated, tears of joy were raining, and everyone was just enormously grateful.
The family was showered with love and support. Everything is peaceful.
But one shouldn't be blinded by the beauty of it all.

In the deep dark forest, remnants of the dead were lingering. Those mortals who were caught between the war of
angels and devils suffered the most gut-wrenching and insufferable consequences. 80%.
It was believed that 80% of the world's population vanished in just a flash. But it was also that same forest where a child,
5 years of age, watched longingly to the joyous village full of happiness.
No one celebrated his birth with him, he was a child abandoned, and only the devil spirits had been the one raising this little lad.
And as the child grew, so did his hatred. And thus, no one should set foot in this forest hidden at the edge of the Earth.

Year 875.

Eljin had just celebrated his 21st birthday, and his only wish was to explore the world beyond the village's borders.
His parents were worried, of course. No one has ever set foot outside the village, no one dared to see the outside world.
But his courage, and his love for adventures urged him to go forward, and explore more than any human has explored.
After weeks of searching for the unknown, he has finally stumbled upon the deep dark path and decided to move forward. \n \n\
"""

            story2 = """\n \nIt wasn't easy exploring an unknown path, surviving the lonely nights, and fighting the great unknown all by yourself. 
It's terrifying and daunting, leaving our hero Eljin, in great horror. Fighting the last battle was like fighting an army all alone.
It drains our hero's energy and physical health, giving the monsters the upper hand, but despite the obvious disadvantage,
he is still determined and has a strong will to continue fighting for the future he hoped for and the land he seeks to find.
And as the sun began to bring color to the world, he set off again and to the unknown world, ready to fight whatever comes his way. 

Walking down the path just admiring the lovely view of the sunrise definitely healed our hero's tainted heart. 
It calmed the uneasiness that surrounded him for the past 48 hours, and as if he could breathe once again. 
But of course, still in the devils den, dangers meant to come chasing him everywhere he goes. 

“Hello there, sweet child.” a beautiful and dazzling fairy greeted him. 
“Are you lost?” He nodded slowly. 
Satisfied with his answer, the dazzling fairy smiled. “Come, I'll show you the way…” 

And so he did. \n \n\
"""

            story_list = (story1, story2)
            print()
            Typewriter.type_effect("...")
            Typewriter.type_effect(random.choice(story_list))

            Typewriter.type_effect("...")
        elif skip_story == 'y':
            break
        else:
            continue
        break
    print()

    instructions = """\nINSTRUCTIONS:

1. Explore the island by moving around the map. You can move up [W], down [S], left [A], or right [D].
2. While exploring the map, combat may begin! Prepare for battle.
3. Exchange few attacks with the enemy before you can have the option to retreat and leave combat.
4. Keep an eye out for surprises marked with "[?]" on the map. \n 
Colliding with a surprise symbol may affect your HP either negatively or positively. You might also encounter a random enemy, so watch out.
5. Watch out for trees marked with "[#]" — you can't collide with them.
6. To quit the game, simply input "quit" at any user prompt.

Get ready for an exciting adventure! May you conquer the challenges of the island.

[ @  ] - player
[ X ] - enemy
"""
    
    print(instructions)
    input("\nPress enter to continue...")

    # resetting settings after restarting
    global in_game
    in_game = True
    global player_stats, enemy_stats
    player_stats = {'hp': 100}
    enemy_stats = {'hp': 100}

class Game1:
    # Player and enemy initial stats
    global player_stats, enemy_stats
    player_stats = {'hp': 100}
    enemy_stats = {'hp': 100}

    global in_game
    in_game = True

    # Define map symbols at the global level
    symbols = {
        'ground': '.',
        'boundary': ',',
        'trace': '"',
        'tree': '#',
        'surprise': '?',
        'player': '@',
        'enemy': 'X'
    }

    def __init__(self):
        story()

        if in_game:
            # Set the size of the map
            map_width = 30
            map_height = 20

        # Generate the initial map and player position
        island_map, player_x, player_y, enemy_x, enemy_y = self.generate_island_map(map_width, map_height)

        # Main game loop
        move_counter = 0

        while in_game:
            self.check_health()
            # Print the map
            self.print_island_map(island_map)

            # Get user input for movement
            move_direction = input("Where do you want to go? (W/A/S/D): ").lower()

            # Move the player, enemy, and handle events
            island_map, player_x, player_y, enemy_x, enemy_y, move_counter = self.move_player(
                island_map, player_x, player_y, enemy_x, enemy_y, move_direction, move_counter
            )
            

        if not in_game:
            input("Press enter to return to Main Menu...")
            Typewriter.type_effect("...")
            print()
            print()

            import main
            main
            # go back to main menu

    def generate_island_map(self, width, height):

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


    def display_legend(self):
        legend_items = {
            "Player": "[@]",
            "Enemy": "[X]",
            "Surprise": "[?]",
            "Tree": "#", 
            "Boundary": ",", 
        }

        print("\n>> MAP LEGENDS <<")
        for item, symbol in legend_items.items():
            print(f"{item}: {symbol}", end="  ")

    def print_island_map(self, island_map):
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console

        self.display_legend()
        print()

        # Print the map with borders
        print('+' + '-' * (len(island_map[0]) * 2 - 1) + '+')
        for row in island_map:
            print('|' + ' '.join(self.symbols[cell] for cell in row) + '|')
        print('+' + '-' * (len(island_map[0]) * 2 - 1) + '+')
    
    def move_player(self, island_map, player_x, player_y, enemy_x, enemy_y, direction, move_counter):
        global in_game

        #for every move of the player, check if the enemy's hp falls below 0
        if enemy_stats['hp'] <= 0:
                print()
                print(" ============================================== ")
                print("||  You defeated the enemy. CONGRATULATIONS!  ||")
                print(" ==============================================  ")
                print("\n")
                
                in_game = False

        #for every move of the player, check if the player's hp falls below 0
        if player_stats['hp'] <= 0:
                print()
                print(" ======================================== ")
                print("||  You have been defeated. GAME OVER.  ||")
                print(" ======================================== ")
                print("\n")
                
                in_game = False

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
                self.combat(player_stats, enemy_stats)
                #if the player moves and it's close to the enemy, it will start the battle
            new_y -= 1
        elif direction == 's' and player_y < len(island_map) - 2 and island_map[player_y + 1][player_x] != 'tree' and island_map[player_y + 1][player_x] != 'enemy':
            if island_map[player_y + 1][player_x] == 'surprise':
                surprise_event = True
            if island_map[player_y + 1][player_x] == 'enemy':
                self.combat(player_stats, enemy_stats)
            new_y += 1
        elif direction == 'a' and player_x > 1 and island_map[player_y][player_x - 1] != 'tree' and island_map[player_y][player_x - 1] != 'enemy':
            if island_map[player_y][player_x - 1] == 'surprise':
                surprise_event = True
            if island_map[player_y][player_x - 1] == 'enemy':
                self.combat(player_stats, enemy_stats)
            new_x -= 1
        elif direction == 'd' and player_x < len(island_map[0]) - 2 and island_map[player_y][player_x + 1] != 'tree' and island_map[player_y][player_x + 1] != 'enemy':
            if island_map[player_y][player_x + 1] == 'surprise':
                surprise_event = True
            if island_map[player_y][player_x + 1] == 'enemy':
                self.combat(player_stats, enemy_stats)
            new_x += 1

        island_map[new_y][new_x] = 'player'

        # Move the enemy towards the player
        if enemy_x < new_x and island_map[enemy_y][enemy_x + 1] != 'player':
            if island_map[enemy_y - 1][enemy_x] == 'player':
                self.combat(player_stats, enemy_stats)
            enemy_x += 1
        elif enemy_x > new_x and island_map[enemy_y][enemy_x - 1] != 'player':
            if island_map[enemy_y + 1][enemy_x] == 'enemy':
                self.combat(player_stats, enemy_stats)
            enemy_x -= 1
        elif enemy_y < new_y and island_map[enemy_y + 1][enemy_x] != 'player':
            if island_map[enemy_y][enemy_x - 1] == 'enemy':
                self.combat(player_stats, enemy_stats)
            enemy_y += 1
        elif enemy_y > new_y and island_map[enemy_y - 1][enemy_x] != 'player':
            if island_map[enemy_y][enemy_x + 1] == 'enemy':
                self.combat(player_stats, enemy_stats)
            enemy_y -= 1

        island_map[enemy_y][enemy_x] = 'enemy'

        if surprise_event:
            surprise = {
            'Health Potion': 20,
            'Lucky Charm': 5,
            'Venomous Snakes': -5,
            'Cursed Relic': -10,
            'Minion of the Enemy Boss' : -20
            }

            surprise_list = ("Health Potion", "Lucky Charm", "Venomous Snakes", "Cursed Relic", "Minion of the Enemy Boss")

            input("\nYou reached a surprise area. Press enter to see what you got...")
            random_surprise = random.choice(surprise_list)
            
            
            if random_surprise in surprise:
                if surprise[random_surprise] >= 0:
                    input(f"\nYou got {random_surprise}! That's worth {surprise[random_surprise]} points of HP!")
                    player_stats['hp'] += surprise[random_surprise]
                elif surprise[random_surprise] < 0:
                    input(f"\nOh no! You encountered a {random_surprise}! That's worth {surprise[random_surprise]} points of HP!")
                    player_stats['hp'] += surprise[random_surprise]


        move_counter += random.randint(1,8)
        if move_counter >= 20:

            while(True):
                self.check_health()
                play_game = input("The enemy is eager for a clash! Will you engage in a combat? [Y/N] ").lower()

                if(play_game == 'y'):
                    move_counter = 0
                    print("\n=======================================================================================")
                    print()
                    print(">>>   COMBAT BEGINS!  <<<")
                    print()
                    print("    ================     ")
                    print("   ||  HP STATUS:  ||    ")
                    print("    ================     ")
                    print(f"  Your remaining HP: [{player_stats['hp']}]")
                    print(f"  Enemy HP: [{enemy_stats['hp']}]")
                    
                    self.combat(player_stats, enemy_stats)

                    break
                elif(play_game == 'n'):
                    Typewriter.type_effect("Opting for a strategic retreat...")
                    move_counter = 0
                    time.sleep(1)
                    break
                else:
                    continue
        return island_map, new_x, new_y, enemy_x, enemy_y, move_counter
    

    def combat(self, player_stats, enemy_stats):
        global in_game
        print()
        print(">>>>> Battle starts! <<<<<")

        player_attack_count = 0  # Counter for player attacks

        in_combat = True
        while in_combat:
            if player_stats['hp'] <= 0:
                player_stats['hp'] = 0
                break
            self.player_attack(enemy_stats)
            player_attack_count += 1
            # after attacking the enemy, increase player_attack_count
            # when it reaches a certain condition, they should be able to have the option to retreat

            if player_attack_count >= random.randint(5,7):
                continue_combat = input("\nThe battle is looking dire! Do you wish to escape? [Y/N] ").lower()

                if(continue_combat) == 'n':
                    Typewriter.type_effect("\nContinuing combat...")
                    time.sleep(1)
                    print()
                    continue
                elif(continue_combat) == 'y':
                    print()
                    print(" ================================")
                    print("||  You successfully retreated!  ||")
                    print(" ================================")
                    input("Press enter to continue...")
                    print("\n")

                    break
                else:
                    print("You lost the chance to run.")
                    Typewriter.type_effect("\nContinuing combat...")
                    time.sleep(1)
                    break
                    # Simulate enemy's turn
            if enemy_stats['hp'] <= 0:
                break
            if player_stats['hp'] <= 0:
                player_stats['hp'] = 0
                break
            self.enemy_attack(player_stats, enemy_stats)
            
    
    def check_health(self):
        global in_game, in_combat
        
        if enemy_stats['hp'] == 0:
            print()
            print(" ============================================ ")
            print("||  You defeated the enemy. CONGRATULATIONS! ||")
            print(" ============================================ ")
            print("\n")
            
            in_game = False
            in_combat = False


        if player_stats['hp'] == 0:
            print()
            print(" ======================================== ")
            print("||  You have been defeated. GAME OVER.  ||")
            print(" ======================================== ")
            print("\n")
            
            in_game = False
            in_combat = False
    
    def enemy_attack(self, player_stats, enemy_stats):
        global in_game

        # Simulate enemy attacking player
        damage = random.randint(8, 20) #the damage the enemy inflict on you will be between 8 to 20
        player_stats['hp'] -= damage
        if player_stats['hp'] <= 0:
            player_stats['hp'] = 0
            
        print()

        Typewriter.type_effect("...")

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
            player_stats['hp'] = 0
            self.check_health()


    def player_attack(self, enemy_stats):
        global in_game
        if player_stats['hp'] <= 0:
            player_stats['hp'] = 0
            in_game = False

        print()
        print("+--------------------------------+")
        print("|       Choose your attack       |")
        print("+--------------------------------+")
        print("  1.        Chi Strike            ")
        print("  2.   Artificial Hand Blast      ")
        print("  3.    Baseball Bat Attack       ")
        print("  4.     Berserker Combat         ")
        print("+--------------------------------+")

        choice = input("  What's your attack?: ")

        if choice == '1':
            #chi strike
            damage = random.randint(10, 20)
            enemy_stats['hp'] -= damage
            if enemy_stats['hp'] <= 0:
                enemy_stats['hp'] = 0
            if player_stats['hp'] <= 0:
                player_stats['hp'] = 0
            print(f"\n>> You attacked with Chi Strike! Enemy takes [{damage}] damage.")
        elif choice == '2':
            #artificial hand blast
            damage = random.randint(8, 15)
            enemy_stats['hp'] -= damage
            if enemy_stats['hp'] <= 0:
                enemy_stats['hp'] = 0
            if player_stats['hp'] <= 0:
                player_stats['hp'] = 0 
            print(f"\n>> You attacked with Articifical Hand Blast! Enemy takes [{damage}] damage.")
        elif choice == '3':
            #baseball bat attack
            damage = random.randint(10, 15)
            enemy_stats['hp'] -= damage
            if enemy_stats['hp'] <= 0:
                enemy_stats['hp'] = 0
            if player_stats['hp'] <= 0:
                player_stats['hp'] = 0
            print(f"\n>> You attacked with Baseball Bat Attack! Enemy takes [{damage}] damage.")
        elif choice == '4':
            #berserker combat
            damage = random.randint(15, 25)
            enemy_stats['hp'] -= damage
            if enemy_stats['hp'] <= 0:
                enemy_stats['hp'] = 0
            if player_stats['hp'] <= 0:
                player_stats['hp'] = 0
            print(f"\n>> You attacked with Berserker Combat! Enemy takes [{damage}] damage.")
        elif choice == 'quit':
            print()
            print("Redirecting to the the main menu", end=" ")
            Typewriter.type_effect("...")
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
        self.check_health()
