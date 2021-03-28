# Importiere die Funktion run() als playgame() -> Führt dann botproject.py aus und spielt das game
from botproject import run as playgame 
# Importiere die Funktion navHome() und führt navHome() in restartgame.py aus 
from restartgame import navHome
# Importiere navToMap() to choose map aus navigatemenue.py
from navigatemenue import navToMap
import time
import keyboard

# Welcome message
print("Open up the Game with the following settings:")
print("1920x1080 | Fullscreen | Autoplay ON")
print("Start at Home Screen")
print("To stop the bot hold 'Ü'- DON'T MOVE YOUR Mouse")
print("Keep in Foreground")

# Delay, damit man in das Game tabben kann
print("Bot is starting in 3")
time.sleep(1)
print("Bot is starting in 2")
time.sleep(1)
print("Bot is starting in 1")
time.sleep(1)

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
        # Turns to True if restartgame.py runs through and has restarted
        # game_won in navHome() mitgeben als Parameter, damit in restartgame.py darauf zugegriffen werden kann
        homescreen = navHome(game_won)
    time.sleep(1)

    # wenn im homescreen, dann öffne Map im richtigen Schwierigkeitsgrad
   # if homescreen is True: 
    #    print("Opening up new Game")
     #   # s.o.
      #  gameStarted = navToMap(homescreen)
    #time.sleep(2) D

    # format string -> meint das game_won und gibt neben dem String auch den Wert der Variablen in einer Zeile aus
    # print(f"game_won is: {game_won}")
    # print(f"homescreen is: {homescreen}")
    # print(f'gameStarted is: {gameStarted}')

else:
    print("Bot is stopping - Keep holding Ü")

print("Bot has stopped")