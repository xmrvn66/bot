from pyautogui import *  # Importiere Libraries die man braucht
import pyautogui
import time
import keyboard
import numpy as np
import random
import win32api
import win32con
from functions import *

# Voraussetzungen: Home Screen | Full Sreeen 1920x1080

# Victory (gamewon.png) + "next button" appears

# click @ 967, 901 on next Button (next_aftergame.png)

# Home-Button appears

# click @ 792, 846 if home-button (home.png) is visible

# loading screen (2.97s) into Home-Menue
# start navigatemenue.py

# game_won als Parameter muss in die Klammern, damit der Parameter mitgegeben wird
def restartGame(game_won):
    """Skript, welches Spiel neustartet"""

    victoryClicked = False
    freeplayClicked = False
    settingsClicked = False
    okayClicked = False
    restartClicked = False
    gameRestarted = False

    print("checking for victory image")
    time.sleep(1)

    while keyboard.is_pressed('ü') == False:
    # check if victory image appeared
        if pyautogui.locateOnScreen(r'C:\Users\Marvin\Documents\dev\Bot\resource\gamewon.png', grayscale=False, confidence=0.9) != None and game_won is True:
                time.sleep(0.35)
                print("Clicking on Next")
                # click on "next Button"
                click(967, 901)
                victoryClicked = True
                time.sleep(0.35)

    # check for Freeplay Button
        if pyautogui.locateOnScreen(r'C:\Users\Marvin\Documents\dev\Bot\resource\freeplaybutton.png', grayscale=False, confidence=0.9) != None and victoryClicked is True:
                time.sleep(0.35)
                print("Clicking on Freeplay")
                # click on Freeplay
                click(1116, 837)
                freeplayClicked = True
                time.sleep(0.5)

                # check for Okay Button
        if pyautogui.locateOnScreen(r'C:\Users\Marvin\Documents\dev\Bot\resource\okaybutton.png', grayscale=False, confidence=0.9) != None and freeplayClicked is True:
                time.sleep(0.35)
                print("Clicking on Okay")
                # click on Okay
                click(945, 758)
                okayClicked = True
                time.sleep(0.5)

                # check for Settings Button
        if pyautogui.locateOnScreen(r'C:\Users\Marvin\Documents\dev\Bot\resource\settings.png', grayscale=False, confidence=0.9) != None and okayClicked is True:
                time.sleep(0.35)
                print("Opening Settings")
                # click on Settings
                click(1595, 33)
                settingsClicked = True
                time.sleep(0.5)

                # check for Restart Button
        if pyautogui.locateOnScreen(r'C:\Users\Marvin\Documents\dev\Bot\resource\restartbutton.png', grayscale=False, confidence=0.7) != None and settingsClicked is True:
                time.sleep(0.35)
                print("Restarting")
                # click on Restart
                click(1089, 836)
                restartClicked = True
                time.sleep(0.5)

                # check for Restart Confirmation Button
        if pyautogui.locateOnScreen(r'C:\Users\Marvin\Documents\dev\Bot\resource\confirmrestart.png', grayscale=False, confidence=0.9) != None and restartClicked is True:
                print("Confirming ...")
                time.sleep(0.35)
                # click on RestartConfirmation
                click(1134, 716)
                gameRestarted = True
                time.sleep(0.35)
                break
    
    else: 
        print("Bot is stopping - Keep holding Ü")

    # Home menu opens up - return restartgame = true
    return gameRestarted

                