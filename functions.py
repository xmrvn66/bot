from pyautogui import *  # Importiere Libraries die man braucht
import pyautogui
import time
import keyboard
import numpy as np
import random
import win32api
import win32con

# Click Function -> Kann dann immer gecalled werden, wenn man irgendwo clicken will
def click(x, y):
    """
    Click(x, y): \n
    Click function to click at location x, y with random delay between 0.1, 0.3 seconds \n
    """
    win32api.SetCursorPos((x, y))
    time.sleep(np.random.uniform(0.1,0.3))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)  # push left click
    time.sleep(np.random.uniform(0.1,0.3))  # hold button for 0.1 - 0.3s 
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0, 0)  # release left click

# click to start game + fast forward
def startgame():
    """
    startgame(): \n
    Function to start the game and click fast forward with 0.1 delay between clicks
    """
      
    click(1827, 999)
    time.sleep(0.1)
    click(1827, 999)
# Countdown der von t runterzählt und einen String voranstellt msg="Bot ist starting in"
def countDown(t=3, msg="Bot is starting in: "):
    """
    countDown(t, msg): \n
    function to count down in console \n
    t = int = Bsp. 5 \n
    msg = string = Bsp. msg="Bot starting in: "
    """
    for t in range(t, 0, -1):
      print(msg + str(t))
      time.sleep(1)
      t -= 1

# Check if Unit is available for purchase
def checkAvailability(unitName: str, pngFile: str, special_key: str = 'ü') -> bool:
    """
    Funktion um Availabilty einer Unit zu checken \n
    unitName = String = Bsp. : unitname="Sniper" \n
    pngFile = String = Bsp. : pngFile="sniper.png" \n
    special_key = String = Bsp. : special_key="Ü"
    """

    unitAvail = False

    while keyboard.is_pressed(special_key) == False:
        print("Checking if " + unitName + " is ready for purchase")
        if pyautogui.locateOnScreen('C:\\Users\\Marvin\\Documents\\dev\\Bot\\resource\\'+pngFile, grayscale=False, confidence=0.8) != None:
                print(unitName + " available for purchase")
                unitAvail = True
                print(f'unitAvail is {unitAvail}')
                break
        time.sleep(2)
    else:
        print(f"Bot is stopping - Keep holding {special_key}")

    return unitAvail

