import time
import random
from scene_1 import scene1


def startGame():
    print("""
    -->> MENU <<--
    [1] Start Game
    [2] Credits
    [3] Quit""")

    print()

    user_input = input("Enter an option: ")

    if user_input == '1':

        sceneList = (scene1) #list of the different scenes excluding the boss fight
        random.choice(sceneList) #randomly choose from the scenes in sceneList
        
    elif user_input == '2':
        credits()
    elif user_input == '3':
        global isPlaying #makes isPlaying accessible inside this function

        print("\nThank you for playing The Escape!")
        print("Quote dito huehuehue")

        isPlaying = False
    else: #if player entered a number other than 1, 2, or 3
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



#while isPlaying is True, the program or the game will continue to run and will be terminated when it is set to False perhaps when player wants to quit or when they lose?
#btw should we give them the option to quit while in game?

isPlaying = True
while isPlaying:
    print("\n========================================================================================================================\n")
    print("Welcome to The Escape!")
    startGame()

