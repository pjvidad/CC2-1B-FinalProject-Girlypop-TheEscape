import time
import random
from scene_1 import scene1
from scene_2 import scene2

def startGame():
    print()
    print("##########################")
    print("# Welcome to The Escape! #")
    print("##########################")
    print("#  -->>> M E N U <<<--   #")
    print("#    [1]  Start Game     #")
    print("#    [2]  Credits        #")
    print("#    [3]  Quit           #")
    print("##########################")

    print()

    user_input = input("Enter an option: ")

    if user_input == '1':
        sceneList = (scene1, scene2) 
        #this is a list of the different scenes, which are functions

        random.choice(sceneList)()
        #we are randomly selecting a choice from any of the functions inside the sceneList

    elif user_input == '2':
        credits()
    elif user_input == '3':
        global isPlaying 
        #global makes isPlaying accessible inside this function

        print("\nThank you for playing The Escape!")
        print("Quote dito huehuehue")

        isPlaying = False
    else: 
        #if player entered a number other than 1, 2, or 3
        print("\nOption Invalid!")


def credits():
    print("\n========================================================================================================================\n")

    time.sleep(1)
    print("The geniuses behind The Escape!")
    print()

    time.sleep(1)

    load = "..."
    for char in load:
        print(char, end='')
        time.sleep(.5)

    time.sleep(1)
    print("GIRLY POP!")
    print()
    
    time.sleep(1)

    print("Lucci Ania Luisse Fagela")
    time.sleep(1)
    print("Rupert Xavier Galera")
    time.sleep(1)
    print("Jenny Ann Guyong")
    time.sleep(1)
    print("Princess Joy Vidad")

#since isPlaying is set to True, it will execute the while loop and will continue to do so until it is set to False

isPlaying = True
while isPlaying:
    startGame()
