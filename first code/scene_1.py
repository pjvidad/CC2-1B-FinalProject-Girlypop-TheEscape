import time
from island_map import loadMap

def scene1():
    print("\n========================================================================================================================")
    print()

    line1 = "Year 854.\n" #since the end parameter is an empty string and not \n anymore, we need that \n to display line 2 to the next line
    for char in line1:
        print(char, end='')
        #this loops through each of line1's characters and prints them without adding any new line in between, that's why the end parameter is empty
        time.sleep(.05)
        #each character gets printed with 0.5 secs delay in between

    time.sleep(1)
    print()

    line2 = """Peace has reigned in the heavens and the Earth after 2000 long years of war between angels and devils.
It was peaceful they said, where laughter of children rang, and songs of glory were sung in choirs.
The grass dances with the wind, the birds sing songs of freedom, everything is peaceful.
The cry of a new born baby sounded across the small village.
“IT'S A BOY!” announced by the physician, and everyone clapped and exclaimed their excitement.
A new baby boy was born, not a royal, nor divine, but every birth is celebrated as a baby symbolizes a new hope.
Everyone cheered and celebrated, tears of joy were raining, and everyone was just enormously grateful.
The family was showered with love and support. Everything is peaceful.  But one shouldn't be blinded by the beauty of it all.\n"""
    for char in line2:
        print(char, end='')
        time.sleep(.05)

    time.sleep(1)
    print()

    line3 = "Year 875.\n"
    for char in line3:
        print(char, end='')
        time.sleep(.05)

    time.sleep(1)
    print()

    line4 = """Eljin had just celebrated his 21st birthday, and his only wish was to explore the world beyond the village's borders.
His parents were worried, of course. No one has ever set foot outside the village, no one dared to see the outside world.
But his courage, and his love for adventures urged him to go forward, and explore more than any human has explored.
After weeks of searching for the unknown, he has finally stumbled upon the deep dark path and decided to move forward.\n"""
    for char in line4:
        print(char, end='')
        time.sleep(.05)

    time.sleep(1)

    loading = "..."
    for char in loading:
        print(char, end='')
        time.sleep(.5)

    forestMap() 

def forestMap():
    hasNotWon = True

    if (hasNotWon):
        loadMap()
    elif (not hasNotWon):
        print("Congrats yey! You attained nirvana sheesh!")
