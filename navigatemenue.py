from pyautogui import *  # Importiere Libraries die man braucht
import pyautogui
import time
import keyboard
import numpy as np
import random
import win32api
import win32con

# Voraussetzungen: Home Screen | Full Sreeen 1920x1080

# # check for Play button shwon and
# Click Play @ 827, 927 if Play Button is shown

# Click on Map @ 532, 261 if Map is shown in Map Selection Screen

# Click @ 622, 417 to select difficulty easy

# Click @ 630, 573 to select gamemode "standard" 

# # # Loadin Screen appears

# # Map loaded after ~ 2.97s 
# -> check if Map is loaded [ monkey_madows_map] or time.sleep(4) 
# -> if map loaded or slept 4 seconds play script "botproject.py"

def navToMap():
    """Wähle Map, wenn im Homescreen"""

    playClicked = False
    mapClicked = False
    diffClicked = False
    gamemodeClicked = False

    print("checking for play button")
    time.sleep(0.35)

    while keyboard.is_pressed('ü') == False:
    # check if play button appeared
        if pyautogui.locateOnScreen(r'C:\Users\Marvin\Documents\dev\Bot\playbutton_lobby_homescreen.png', grayscale=False, confidence=0.9) != None:
                print("Play Button Found")
                time.sleep(0.35)
                print("Clicking on Play Button")
                # click on "Play Button"
                click(827, 927)
                playClicked = True
                time.sleep(0.5)

    # check for Monkey Madows Map
        if pyautogui.locateOnScreen(r'C:\Users\Marvin\Documents\dev\Bot\monkey_madows_selectscreen.png', grayscale=False, confidence=0.9) != None and playClicked is True:
                print("Monkey Madows Map Found")
                time.sleep(0.35)
                print("Choosing Map")
                # click on Monkey Madows Map
                click(532, 261)
                mapClicked = True
                time.sleep(0.3)
    
        # check for Difficulty
        if pyautogui.locateOnScreen(r'C:\Users\Marvin\Documents\dev\Bot\easydiff.png', grayscale=False, confidence=0.9) != None and mapClicked is True:
                print("Difficulties Found")
                time.sleep(0.35)
                print("Selecting Easy Difficulty")
                # click on Monkey Madows Map
                click(622, 417)
                diffClicked = True
                time.sleep(0.3)
    
            # check for Gamemode
        if pyautogui.locateOnScreen(r'C:\Users\Marvin\Documents\dev\Bot\standard_gamemode.png', grayscale=False, confidence=0.9) != None and diffClicked is True:
                print("Gamemode Found")
                time.sleep(0.35)
                print("Selecting Standard Gamemode")
                # click on Monkey Madows Map
                click(630, 573)
                gamemodeClicked = True
                time.sleep(0.3)
                break
    
    else: 
        print("Starting New Game stopped")

    # Home menu opens up - return restartgame = true
    return gamemodeClicked