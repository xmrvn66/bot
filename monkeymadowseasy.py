from pyautogui import *  # Importiere Libraries die man braucht
import pyautogui
import time
import keyboard
import numpy as np
import random
import win32api
import win32con
from levelup import checkLvlUp
from checkMap import checkForMap
from functions import *


def run():
    
    # place Ninja 1 at 623, 535 -> upgrade to 4-0-1
    ninja1 = Unit("Ninja Monkey 1", x=623, y=535, shortcut="D", [0,0,0], [0,0,0])

    ninja1.placeUnit()
    time.sleep(1)

    ninja1.endstate[0] = 2
    ninja1._upgrade_fully()
    time.sleep(1)

    ninja1.endstate[2] = 1
    ninja1._upgrade_fully()
    time.sleep(1)

    ninja1.endstate[0] = 4
    ninja1._upgrade_fully()
    time.sleep(1)

    # place sniper at 721, 545 upgrade to 3-1-0 (1 - 2 - 1 - 1)
    sniper1 = Unit("Sniper Monkey 1", 721, 545, "Z", [0,0,0], [0,0,0])

    sniper1.placeUnit()
    time.sleep(1)

    sniper1.endstate[0] = 1
    sniper1._upgrade_fully()
    time.sleep(1)

    sniper1.endstate[1] = 1
    sniper1._upgrade_fully()
    time.sleep(1)

    sniper1.endstate[0] = 3
    sniper1._upgrade_fully()
    time.sleep(1)

    print(f" 2. {sniper1.name} is upgraded to {sniper1.state[0]}-{sniper1.state[1]}-{sniper1.state[2]}")
    sniper1._upgrade_fully()

    # place cannon at 434, 730 upgrade to 2 - 4 - 0 -> 2 - 2 -2 - 1 - 1 - 2

    cannon1 = Unit("Cannon Monkey 1", 434, 730, "E", [0,0,0], [0,0,0])

    cannon1.placeUnit()
    time.sleep(1)

    cannon1.endstate[1] = 3
    cannon1._upgrade_fully()
    time.sleep(1)

    cannon1.endstate[0] = 2
    cannon1._upgrade_fully()
    time.sleep(1)

    cannon1.endstate[1] = 4
    cannon1._upgrade_fully()
    time.sleep(1)

    print(f" {ninja1.name} was upgraded to {ninja1.state[0]}-{ninja1.state[1]}-{ninja1.state[2]}")
    print(f" {sniper1.name} was upgraded to {sniper1.state[0]}-{sniper1.state[1]}-{sniper1.state[2]}")
    print(f" {cannon1.name} was upgraded to {cannon1.state[0]}-{cannon1.state[1]}-{cannon1.state[2]}")

    wait_for_game_finished()