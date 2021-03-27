# Importiere die Funktion run() als playgame() -> Führt dann botproject.py aus und spielt das game
from botproject import run as playgame 
# Importiere die Funktion navHome() und führt navHome() in restartgame.py aus 
from restartgame import navHome
# from navigatemenu import run as menu_run
import time

print("Main starting")
time.sleep(0.3)

# game_won wird True, wenn playgame() durchgelaufen ist
game_won = playgame() 
print("game_won is:")
print(game_won)

time.sleep(1.5)

print("Importing navHome")

game_won = True

print("Imported navHome")
time.sleep(0.2)

if game_won is True: 
    print("Navigating home")
    # Turns to True if restartgame.py runs through and game navigates to homescreen
    # game_won in navHome() mitgeben als Parameter, damit in restartgame.py darauf zugegriffen werden kann
    homescreen = navHome(game_won)

time.sleep(1.5)


# format string -> meint das game_won und gibt neben dem String auch den Wert der Variablen in einer Zeile aus
print(f"game_won is: {game_won}")
print(f"homescreen is: {homescreen}")
print("Main durchgelaufen - Skript vorbei")


#menu_run()


# while True:
   # if check_popover() is True:
    #    close_popover()
    #
   # ninja_needs_to_update = check_ninja()
   # if ninja_needs_to_update is True:
   #     update_ninja()
#
    #    ninja_needs_to_update = True
#
   # if needs_to_exit is True:
   #     break