import random, time, sys
from scene_1 import scene1, typewriterEffect
from scene_2 import scene2

def startGame():
    print("""
        █░█░█ █▀▀ █░░ █▀▀ █▀█ █▀▄▀█ █▀▀   ▀█▀ █▀█
        ▀▄▀▄▀ ██▄ █▄▄ █▄▄ █▄█ █░▀░█ ██▄   ░█░ █▄█""")
    print("""
███████████████████████████████████████████████████████
█─▄─▄─█─█─█▄─▄▄─███▄─▄▄─█─▄▄▄▄█─▄▄▄─██▀▄─██▄─▄▄─█▄─▄▄─█
███─███─▄─██─▄█▀████─▄█▀█▄▄▄▄─█─███▀██─▀─███─▄▄▄██─▄█▀█
▀▀▄▄▄▀▀▄▀▄▀▄▄▄▄▄▀▀▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▀▀▀▄▄▄▄▄▀""")
    print()
    print("             ##########################")
    print("             #  -->>> M E N U <<<--   #")
    print("             #    [1]  Start Game     #")
    print("             #    [2]  Credits        #")
    print("             #    [3]  Quit           #")
    print("             ##########################")
    print()

    user_input = input("Enter an option: ")

   if user_input == '1':
        scene1()
    elif user_input == '2':
        credits()
    elif user_input == '3':
        global isPlaying 
        #global makes isPlaying accessible inside this function

        print("\nThank you for playing The Escape!")
        print("Quote dito huehuehue")

        isPlaying = False
        sys.exit()
    else: 
        #if player entered a number other than 1, 2, or 3
        print("\nOption Invalid!")


def credits():

    print("\n=======================================================================================")

    creditsIntro = "The geniuses behind The Escape!\n \n"
    typewriterEffect(creditsIntro)

    loadingText = "..."
    typewriterEffect(loadingText)
    
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
    time.sleep(1)
    
    
#since isPlaying is set to True, it will execute the while loop and will continue to do so until it is set to False

isPlaying = True
while isPlaying:
    startGame()
