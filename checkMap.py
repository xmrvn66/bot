from pyautogui import *  # Importiere Libraries die man braucht
import pyautogui
import time
import keyboard
import numpy as np
import random
import win32api
import win32con

def checkForMap():
    """Checking if Map is loaded"""

    # print("Checking for Map")    
    if pyautogui.locateOnScreen(r'C:\Users\Marvin\Documents\dev\Bot\monkey_madows_map.png', grayscale=False, confidence=0.9) != None:
        mapLoaded = True
        print("Map is loaded")
        time.sleep(1)
        return mapLoaded    

