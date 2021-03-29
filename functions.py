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
    win32api.SetCursorPos((x, y))  # set cursor position
    # warte zufällig zwischen 0.1s und 0.3s (sonst kommt Spiel nicht klar)
    time.sleep(np.random.uniform(0.1,0.3))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)  # push left click
    time.sleep(np.random.uniform(0.1,0.3))  # hold button for 0.1 - 0.3s 
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0, 0)  # release left click

    # click to start game + fast forward
def startgame():
        click(1827, 999)
        time.sleep(0.1)
        click(1827, 999)

# Countdown der von t runterzählt und einen String voranstellt msg="Bot ist starting in"
def countDown(t, msg):
    for t in range(t, 0, -1):
      print(msg + str(t))
      time.sleep(1)
      t -= 1