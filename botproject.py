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
    """ Skript, welches Spiel spielt."""
    
    # check if Map is loaded
    mapLoaded = checkForMap()
    
    #########################################################################################################################
    #               Placing Ninja                                                                                           #
    #########################################################################################################################

    ninja100 = False
    ninja200 = False
    ninja201 = False
    ninja301 = False
    ninja401 = False

    if ninja401 == False and mapLoaded is True:
        print("Starting by placing Ninja")
        # Selecting Unit
        pyautogui.keyDown('D')  # Drücke "D" um einen Ninja auszuwählen
        time.sleep(0.1)
        pyautogui.keyUp('D')  # Taste "D" wieder loslassen

        # wait before next acion
        time.sleep(0.5)

        # click to place Unit
        click(623, 505)  # klicken an Stelle um Ninja zu platzieren

        # wait before next acion
        time.sleep(0.7)

        # start game and fast forward
        startgame()

        # wait before next acion
        time.sleep(0.3)

        # click Ninja to Upgrade
        print("Attempting to upgrade Ninja to 4-0-1")
        click(632, 505)  # navigate to and click ninja

        while keyboard.is_pressed('ü') is False:
            checkLvlUp()
            
            # check if upgrade Interface is up for Ninja
            if pyautogui.locateOnScreen(r'C:\Users\Marvin\Documents\dev\Bot\resource\UpgradeNinja.png', grayscale=False,confidence=0.9) is None:
                print("Ninja Upgrade UI NOT found - opening now")
                time.sleep(0.3)
                click(632, 505)
                time.sleep(0.2)

            # check if the Ü key is being pressed to Stop Bot
            # Checks if ü key is pressed, if it is, it will stop the script, else it will let the while loop run
            if pyautogui.locateOnScreen(r'C:\Users\Marvin\Documents\dev\Bot\resource\ninjaupgrade100.png', grayscale=False, confidence=0.9) != None:
                # check if Ninja upgrade 1-0-0 is available
                # click on upgrade
                click(1498, 478)
                ninja100 = True
                if ninja100 == True:
                    print("Ninja upgraded to 1-0-0")

            if pyautogui.locateOnScreen(r'C:\Users\Marvin\Documents\dev\Bot\resource\ninjaupgrade200.png', grayscale=False, confidence=0.9) != None and ninja100 == True:
                # check if Ninja upgrade 2-0-0 is available
                # click on upgrade
                click(1498, 478)
                ninja200 = True
                if ninja200 == True:
                    print("Ninja upgraded to 2-0-0")
            time.sleep(0.1)

            if pyautogui.locateOnScreen(r'C:\Users\Marvin\Documents\dev\Bot\resource\ninjaupgrade201.png', grayscale=False, confidence=0.9) != None and ninja200 == True:
                # check if Ninja upgrade 2-0-1 is available
                # click on upgrade
                click(1518, 778)
                ninja201 = True
                if ninja201 == True:
                    print("Ninja upgraded to 2-0-1")
            time.sleep(0.1)

            if pyautogui.locateOnScreen(r'C:\Users\Marvin\Documents\dev\Bot\resource\ninjaupgrade301.png', grayscale=False, confidence=0.9) != None and ninja201 == True:
                # check if Ninja upgrade 2-0-1 is available
                # click on upgrade
                click(1498, 478)
                ninja301 = True
                if ninja301 == True:
                    print("Ninja upgraded to 3-0-1")
            time.sleep(0.1)

            if pyautogui.locateOnScreen(r'C:\Users\Marvin\Documents\dev\Bot\resource\ninjaupgrade401.png', grayscale=False, confidence=0.9) != None and ninja301 == True:
                # check if Ninja upgrade 2-0-1 is available
                # click on upgrade
                click(1498, 478)
                ninja401 = True
                if ninja401 == True:
                    print("Ninja upgraded to 4-0-1")
            time.sleep(0.1)

            # End Loop and Exit Upgrade Screen
            if ninja401 is True:
                print("Ninja successfully upgraded to 4-0-1")
                time.sleep(0.2)
                # Drücke "ESC" um Upgrade Screen zu verlassen
                pyautogui.keyDown('ESC')
                time.sleep(0.1)
                pyautogui.keyUp('ESC')
                time.sleep(0.5)  # Taste "ESC" wieder loslassen
                break
        else:
            print("Bot is stopping - Keep holding Ü")

    #########################################################################################################################
    #               Intermission                                                                                            #
    #########################################################################################################################
    # check if Sniper is available to buy

    sniperAvail = False
    if ninja401 is True:
        sniperAvail = checkAvailability("sniper", "sniperAvail.png")    

    #########################################################################################################################
    #               Placing Sniper                                                                                          #
    #########################################################################################################################

    sniper100 = False
    sniper110 = False
    sniper210 = False
    sniper310 = False

    if sniper310 == False and sniperAvail == True:

        print("Placing Sniper Monkey")
        # Selecting Unit
        pyautogui.keyDown('Z')  
        time.sleep(0.2)
        pyautogui.keyUp('Z')  

        # wait before next acion
        time.sleep(0.5)

        # click to place Unit
        click(721, 545)  
    
        time.sleep(0.3)

        print("Attempting to upgrade Sniper to 3-1-0")
        click(721, 545)

        while keyboard.is_pressed('ü') == False:
            checkLvlUp()

            # check if upgrade Interface is up for Sniper
            if pyautogui.locateOnScreen(r'C:\Users\Marvin\Documents\dev\Bot\resource\UpgradeSniper.png', grayscale=False,confidence=0.9) is None:
                print("Sniper Upgrade UI NOT found - opening now")
                time.sleep(0.3)
                click(721, 545)
                time.sleep(0.2)

            if pyautogui.locateOnScreen(r'C:\Users\Marvin\Documents\dev\Bot\resource\sniper100.png', grayscale=False, confidence=0.9) != None:
                # check if Sniper upgrade 1-0-0 is available
                click(1498, 478)
                sniper100 = True
                if sniper100 == True:
                    print("Sniper upgraded to 1-0-0")
            time.sleep(0.2)

            if pyautogui.locateOnScreen(r'C:\Users\Marvin\Documents\dev\Bot\resource\sniper110.png', grayscale=False, confidence=0.9) != None and sniper100 == True:
                # check if Sniper upgrade 1-1-0 is available
                click(1561, 636)
                sniper110 = True
                if sniper110 == True:
                    print("Sniper upgraded to 1-1-0")

            time.sleep(0.1)

            if pyautogui.locateOnScreen(r'C:\Users\Marvin\Documents\dev\Bot\resource\sniper210.png', grayscale=False, confidence=0.9) != None and sniper110 == True:
                # check if Sniper upgrade 2-1-0 is available
                click(1498, 478)
                sniper210 = True
                if sniper210 == True:
                    print("Sniper upgraded to 2-1-0")
            time.sleep(0.3)

            if pyautogui.locateOnScreen(r'C:\Users\Marvin\Documents\dev\Bot\resource\sniper310.png', grayscale=False, confidence=0.9) != None and sniper210 == True:
                # check if Sniper upgrade 3-1-0 is available
                click(1498, 478)
                sniper310 = True
                if sniper310 == True:
                    print("Sniper upgraded to 3-1-0")
            time.sleep(0.1)

            if sniper310 == True:
                print("Sniper successfully upgraded to 3-1-0")
                time.sleep(0.2)
                # Drücke "ESC" um Upgrade Screen zu verlassen
                pyautogui.keyDown('ESC')
                time.sleep(0.1)
                pyautogui.keyUp('ESC') 
                time.sleep(0.4)
                break
        else:
            print("Bot is stopping - Keep holding Ü")


    #########################################################################################################################
    #               Intermission #2                                                                                         #
    #########################################################################################################################

    canonAvail = False
    if sniper310 is True: 
        canonAvail = checkAvailability("cannon", "canonAvail.png")  

    #########################################################################################################################
    #               Placing Canon                                                                                           #
    #########################################################################################################################

    canon010 = False
    canon020 = False
    canon030 = False
    canon130 = False
    canon230 = False
    canon240 = False

    if canon010 == False and canonAvail == True:

        print("Placing Bomb Shooter")
        # Selecting Unit
        pyautogui.keyDown('E')  # Drücke "E" um einen Bomb Shooter auszuwählen
        time.sleep(0.2)
        pyautogui.keyUp('E')  # Taste "E" wieder loslassen
        
        time.sleep(0.5)

        # click to place Unit
        click(434, 730) 

        # wait before next acion
        time.sleep(0.3)

        # click Sniper Monkey to Upgrade
        print("Attempting to upgrade Bomb Shooter to 2-4-0")
        click(434, 730)

        while keyboard.is_pressed('ü') == False:
            checkLvlUp()

            # check if upgrade Interface is up for Sniper
            if pyautogui.locateOnScreen(r'C:\Users\Marvin\Documents\dev\Bot\resource\UpgradeCannon.png', grayscale=False,confidence=0.9) is None:
                print("Cannon Upgrade UI NOT found - opening now")
                time.sleep(0.3)
                click(434, 730)
                time.sleep(0.2)

            if pyautogui.locateOnScreen(r'C:\Users\Marvin\Documents\dev\Bot\resource\canon010.png', grayscale=False, confidence=0.9) != None:
                click(1561, 636)
                canon010 = True
                if canon010 == True:
                    print("Bomb Shooter upgraded to 0-1-0")
            time.sleep(0.2)

            if pyautogui.locateOnScreen(r'C:\Users\Marvin\Documents\dev\Bot\resource\canon020.png', grayscale=False, confidence=0.9) != None and canon010 == True:
                click(1561, 636)
                canon020 = True
                if canon020 == True:
                    print("Bomb Shooter upgraded to 0-2-0")

            time.sleep(0.1)

            if pyautogui.locateOnScreen(r'C:\Users\Marvin\Documents\dev\Bot\resource\canon030.png', grayscale=False, confidence=0.9) != None and canon020 == True:
                click(1561, 636)
                canon030 = True
                if canon030 == True:
                    print("Bomb Shooter upgraded to 0-3-0")
            time.sleep(0.3)

            if pyautogui.locateOnScreen(r'C:\Users\Marvin\Documents\dev\Bot\resource\canon130.png', grayscale=False, confidence=0.9) != None and canon030 == True:
                click(1498, 478)
                canon130 = True
                if canon130 == True:
                    print("Bomb Shooter upgraded to 1-3-0")
            time.sleep(0.1)

            if pyautogui.locateOnScreen(r'C:\Users\Marvin\Documents\dev\Bot\resource\canon230.png', grayscale=False, confidence=0.9) != None and canon130 == True:
                click(1498, 478)
                canon230 = True
                if canon230 == True:
                    print("Bomb Shooter upgraded to 2-3-0")
            time.sleep(0.1)

            if pyautogui.locateOnScreen(r'C:\Users\Marvin\Documents\dev\Bot\resource\canon240.png', grayscale=False, confidence=0.9) != None and canon230 == True:
                click(1561, 636)
                canon240 = True
                if canon240 == True:
                    print("Bomb Shooter upgraded to 2-4-0")
            time.sleep(0.1)

            if canon240 == True:
                print("Bomb Shooter successfully upgraded to 2-4-0")
                time.sleep(0.2)
                pyautogui.keyDown('ESC')
                time.sleep(0.1)
                pyautogui.keyUp('ESC')  
                time.sleep(0.4)
                break

        else:
            print("Bot is stopping - Keep holding Ü")

    game_finished = False

    # Game Won Message
    if canon240 == True:
        print("Waiting for Game to finish")
        while keyboard.is_pressed('ü') == False:
            checkLvlUp()
            # check if victory sign appears -> if it does, print and set game_finished to true
            if pyautogui.locateOnScreen(r'C:\Users\Marvin\Documents\dev\Bot\resource\gamewon.png', grayscale=False, confidence=0.9) != None:
                print("Game is won ... GG")
                time.sleep(0.2)
                print("Exiting Game")
                game_finished = True
                break
            time.sleep(1)
        else:
            print("Bot is stopping - Keep holding Ü")
    
    return game_finished