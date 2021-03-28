# Importiere die Funktion run() als playgame() -> Führt dann botproject.py aus und spielt das game
from botproject import run as playgame 
# Importiere die Funktion navHome() und führt navHome() in restartgame.py aus 
from restartgame import navHome
# Importiere navToMap() to choose map aus navigatemenue.py
from navigatemenue import navToMap
import time

print("Main starting")
time.sleep(0.3)

# game_won wird True, wenn playgame() durchgelaufen ist
game_won = playgame() 

time.sleep(1.5)

# wenn game gewonnen, dann gehe zum Homescreen
if game_won is True: 
    print("Navigating home")
    # Turns to True if restartgame.py runs through and game navigates to homescreen
    # game_won in navHome() mitgeben als Parameter, damit in restartgame.py darauf zugegriffen werden kann
    homescreen = navHome(game_won)
time.sleep(1)

# wenn im homescreen, dann öffne Map im richtigen Schwierigkeitsgrad
if homescreen is True: 
    print("Opening up new Game")
    # s.o.
    gameStarted = navToMap(homescreen)
time.sleep(1)

# format string -> meint das game_won und gibt neben dem String auch den Wert der Variablen in einer Zeile aus
print(f"game_won is: {game_won}")
print(f"homescreen is: {homescreen}")
print(f'gameStarted is: {gameStarted}')
print("Main durchgelaufen - Skript vorbei")