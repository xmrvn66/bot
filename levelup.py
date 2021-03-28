from pyautogui import *  # Importiere Libraries die man braucht
import pyautogui
import time
import keyboard
import numpy as np
import random
import win32api
import win32con

def checkLvlUp():
    """Checking for Level Up and Knowledge Point"""

    print("Checking for LevelUP")
    levelUp = False

    if pyautogui.locateOnScreen(r'C:\Users\Marvin\Documents\dev\Bot\levelup.png', grayscale=False, confidence=0.9) != None:
                # check if level up occured
                # click
                print("Level UP detected")
                time.sleep(0.2)
                levelUp = True
                click(1145, 956)
                time.sleep(0.7)
    if pyautogui.locateOnScreen(r'C:\Users\Marvin\Documents\dev\Bot\levelup_knowledgeicon.png', grayscale=False, confidence=0.9) != None and levelUp is True:
                # check if knowledge point was gained
                # click
                print("Knowledge Point gained")
                time.sleep(0.2)
                click(1145, 956)
                print("Continuing in 3")
                time.sleep(1)
                print("Continuing in 2")
                time.sleep(1)
                print("Continuing in 1")