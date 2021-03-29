from pyautogui import *  # Importiere Libraries die man braucht
import pyautogui
import numpy as np
import random
import win32api
import win32con
# Importiere die Funktion run() als playgame() -> Führt dann botproject.py aus und spielt das game
from botproject import run as playgame 
# Importiere die Funktion navHome() und führt navHome() in restartgame.py aus 
from restartgame import restartGame
# Importiere navToMap() to choose map aus navigatemenue.py
from navigatemenue import navToMap
import time
import keyboard
import functions

# Welcome message
print("Open up the Game with the following settings:")
print("1920x1080 | Fullscreen | Autoplay ON")
print("Start at Home Screen")
print("To stop the bot hold 'Ü'- DON'T MOVE YOUR Mouse")
print("Keep in Foreground")

# Delay, damit man in das Game tabben kann
functions.countDown(3)

# Navigate to Map
print("Navigating to Map")
navToMap()

while keyboard.is_pressed('ü') == False:
    print("Starting New Game")

    # game_won wird True, wenn playgame() durchgelaufen ist
    game_won = playgame() 
    time.sleep(2)

    # wenn game gewonnen, dann restarte
    if game_won is True: 
        print("Restart Game")
        # game_won in restartGame() mitgeben als Parameter, damit in restartgame.py darauf zugegriffen werden kann
        homescreen = restartGame(game_won)
    time.sleep(1)

else:
    print("Bot is stopping - Keep holding Ü")

print("Bot has stopped")