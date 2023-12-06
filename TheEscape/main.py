import time, sys, random
from scene_2 import Game2
from scene_1 import Game1, Typewriter

def start_game():
    print()

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
        Game1()
    elif user_input == '2':
        credits()
    elif user_input == '3':
        global is_playing 
        #global makes isPlaying accessible inside this function

        print("""\n𝕿𝖍𝖆𝖓𝖐 𝖞𝖔𝖚 𝖋𝖔𝖗 𝖕𝖑𝖆𝖞𝖎𝖓𝖌 𝕿𝖍𝖊 𝕰𝖘𝖈𝖆𝖕𝖊❗""")
        print("""𝔄 𝔥𝔢𝔯𝔬 𝔦𝔰 𝔞𝔫 𝔬𝔯𝔡𝔦𝔫𝔞𝔯𝔶 𝔦𝔫𝔡𝔦𝔳𝔦𝔡𝔲𝔞𝔩 𝔴𝔥𝔬 𝔣𝔦𝔫𝔡𝔰 𝔱𝔥𝔢 𝔰𝔱𝔯𝔢𝔫𝔤𝔱𝔥 𝔱𝔬 𝔭𝔢𝔯𝔰𝔢𝔳𝔢𝔯𝔢 𝔞𝔫𝔡 𝔢𝔫𝔡𝔲𝔯𝔢 𝔦𝔫 𝔰𝔭𝔦𝔱𝔢 𝔬𝔣 𝔬𝔳𝔢𝔯𝔴𝔥𝔢𝔩𝔪𝔦𝔫𝔤 𝔬𝔟𝔰𝔱𝔞𝔠𝔩𝔢𝔰.""")

        is_playing = False
        sys.exit()
    else: 
        #if player entered a number other than 1, 2, or 3
        print("\nOption Invalid!")


def credits():

    print("\n=======================================================================================")

    credits_intro = "The geniuses behind The Escape!\n \n"
    Typewriter.type_effect(credits_intro)

    Typewriter.type_effect("...")
    
    print("""       ___               __              ___   ___            __                      __      
  .'|=|_.'    .'|   .'|=|  |   .'|      |   | |   |      .'|=|  |    .'|=|`.     .'|=|  |     
.'  |___    .'  | .'  | |  | .'  |      `.  |_|  .'    .'  | |  |  .'  | |  `. .'  | |  |     
|   |`._|=. |   | |   |=|.'  |   |        `.   .'      |   |=|.'   |   | |   | |   |=|.'      
`.  |  __|| |   | |   |  |`. |   |  ___    |   |       |   |       `.  | |  .' |   |          
  `.|=|_.'' |___| |___|  |_| |___|=|_.'    |___|       |___|         `.|=|.'   |___|          
                                                                                              
""")
    print()

    time.sleep(1)
    
    print("""
█░░ █░█ █▀▀ █▀▀ █   ▄▀█ █▄░█ █ ▄▀█   █░░ █░█ █ █▀ █▀ █▀▀   █▀▀ ▄▀█ █▀▀ █▀▀ █░░ ▄▀█
█▄▄ █▄█ █▄▄ █▄▄ █   █▀█ █░▀█ █ █▀█   █▄▄ █▄█ █ ▄█ ▄█ ██▄   █▀░ █▀█ █▄█ ██▄ █▄▄ █▀█""")
    time.sleep(1)
    print("""
█▀█ █░█ █▀█ █▀▀ █▀█ ▀█▀   ▀▄▀ ▄▀█ █░█ █ █▀▀ █▀█   █▀▀ ▄▀█ █░░ █▀▀ █▀█ ▄▀█
█▀▄ █▄█ █▀▀ ██▄ █▀▄ ░█░   █░█ █▀█ ▀▄▀ █ ██▄ █▀▄   █▄█ █▀█ █▄▄ ██▄ █▀▄ █▀█""")
    time.sleep(1)
    print("""
░░█ █▀▀ █▄░█ █▄░█ █▄█   ▄▀█ █▄░█ █▄░█   █▀▀ █░█ █▄█ █▀█ █▄░█ █▀▀
█▄█ ██▄ █░▀█ █░▀█ ░█░   █▀█ █░▀█ █░▀█   █▄█ █▄█ ░█░ █▄█ █░▀█ █▄█""")
    time.sleep(1)
    print("""
█▀█ █▀█ █ █▄░█ █▀▀ █▀▀ █▀ █▀   ░░█ █▀█ █▄█   █░█ █ █▀▄ ▄▀█ █▀▄
█▀▀ █▀▄ █ █░▀█ █▄▄ ██▄ ▄█ ▄█   █▄█ █▄█ ░█░   ▀▄▀ █ █▄▀ █▀█ █▄▀""")
    time.sleep(1)
    
    print("\n=======================================================================================")
    
    
#since isPlaying is set to True, it will execute the while loop and will continue to do so until it is set to False

is_playing = True
while is_playing:
    start_game()
