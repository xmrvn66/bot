from pyautogui import *  # Importiere Libraries die man braucht
import pyautogui
import time
import keyboard
import numpy as np
import random
import win32api
import win32con

# Voraussetzungen: Home Screen | Full Sreeen 1920x1080

# Victory (gamewon.png) + "next button" appears

# click @ 967, 901 on next Button (next_aftergame.png)

# Home-Button appears

# click @ 792, 846 if home-button (home.png) is visible

# loading screen (2.97s) into Home-Menue
# start navigatemenue.py

# game_won als Parameter muss in die Klammern, damit der Parameter mitgegeben wird
def navHome(game_won):
    
    victoryClicked = False
    homeClicked = False

    print("checking for victory image")
    time.sleep(1)

    while keyboard.is_pressed('ü') == False:
    # check if victory image appeared
        if pyautogui.locateOnScreen(r'C:\Users\Marvin\Documents\dev\Bot\gamewon.png', grayscale=False, confidence=0.9) != None and game_won is True:
                print("Victory Found")
                time.sleep(1)
                print("Clicking on Next")
                # click on "next Button"
                click(967, 901)
                victoryClicked = True
                time.sleep(0.7)


    # check for Home Button
        if pyautogui.locateOnScreen(r'C:\Users\Marvin\Documents\dev\Bot\home.png', grayscale=False, confidence=0.9) != None and victoryClicked is True:
                print("Home Button Found")
                time.sleep(1)
                print("Clicking on Home")
                # click on Home
                click(792, 846)
                homeClicked = True
                time.sleep(0.7)
                break
    
    else: 
        print("Returning to Home Screen stopped")

    # Home menu opens up - return restartgame = true
    return homeClicked

                