from pyautogui import *  # Importiere Libraries die man braucht
import pyautogui
import time
import keyboard
import numpy as np
import random
import win32api
import win32con
#from levelup import checkLvlUp

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

def checkLvlUp():
    """Checking for Level Up and Knowledge Point"""

    # print("Checking for LevelUP")
    levelUp = False
    knowledgePoint = False

    if pyautogui.locateOnScreen(r'C:\Users\Marvin\Documents\dev\Bot\resource\levelup.png', grayscale=False, confidence=0.9) != None:
                # check if level up occured
                # click
                print("Level UP detected")
                time.sleep(0.2)
                levelUp = True
                click(1145, 956)
                time.sleep(0.7)
    if pyautogui.locateOnScreen(r'C:\Users\Marvin\Documents\dev\Bot\resource\levelup_knowledgeicon.png', grayscale=False, confidence=0.9) != None and levelUp is True:
                # check if knowledge point was gained
                # click
                print("Knowledge Point gained")
                time.sleep(0.2)
                click(1145, 956)
                countDown(3, msg="Resuming in: ")

    if knowledgePoint and levelUp is True:
                # Start Game and fast forward
                print("Starting Game")
                click(1827, 999)
                time.sleep(0.1)
                click(1827, 999)

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

def wait_for_game_finished(game_finished:bool = False):
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
    
        return game_finished

class Unit: 

    """build constructor """

    def __init__(self, name:str, x:int, y:int, shortcut:str, state=[0,0, 0], endstate=[0, 0, 0]):  
 
        self.name = name           # Unit Name
        self.state = state            
        self.x = x                 # x Pixel
        self.y = y                 # y Pixel
        self.shortcut = shortcut   # shortcut used to select Unit
        self.endstate = endstate
    
    def check_for_interface(self):
        # locate UI if not found
        checkLvlUp()
        if pyautogui.locateOnScreen(r'C:\Users\Marvin\Documents\dev\Uebungen\resource\interfaceUp.png', grayscale=False,confidence=0.7) is None:
            print(f"{self.name} Upgrade UI NOT found - opening now")
            time.sleep(np.random.uniform(0.4,0.6))
            click(self.x, self.y)
            time.sleep(np.random.uniform(0.5,1))

    def placeUnit(self):                                # placeUnit function
        """
        Places Unit at location x, y  \n
        unitName = "Sniper" : Name of Unit - used by print function \n
        shortcut = "Z" : Shortcut used to select Unit ingame
        """
        print(f'Placing {self.name}')
        pyautogui.keyDown(self.shortcut)
        time.sleep(np.random.uniform(0.1,0.2))
        pyautogui.keyUp(self.shortcut)
        time.sleep(np.random.uniform(0.1,0.2))
        click(self.x, self.y)
        time.sleep(np.random.uniform(0.1,0.2))
        print(f'Pressing {self.shortcut} to place {self.name}')
        print(f'My position is {self.x}, {self.y}')

    def _upgrade_fully(self):
        
        while keyboard.is_pressed('ü') is False:
            self.check_for_interface()
            checkLvlUp()
            if self.state[0] < self.endstate[0] and pyautogui.locateOnScreen(r"C:\Users\Marvin\Documents\dev\Uebungen\resource\upgradeAvail.png", region=(1448, 416, 171, 128), grayscale=False, confidence=0.7) != None:
                click(1543, 482) 
                time.sleep(np.random.uniform(1,1.3))
                self.state[0] += 1
                print(f"{self.name} upgraded to {self.state[0]}-{self.state[1]}-{self.state[2]}")     
            if self.state[0] == self.endstate[0]:
                break    

        while keyboard.is_pressed('ü') is False:
            self.check_for_interface()
            checkLvlUp()
            if self.state[1] < self.endstate[1] and pyautogui.locateOnScreen(r"C:\Users\Marvin\Documents\dev\Uebungen\resource\upgradeAvail.png", region=(1448, 574, 171, 128), grayscale=False, confidence=0.7) != None:
                click(1543, 628) 
                time.sleep(np.random.uniform(1,1.3))
                self.state[1] += 1
                print(f"{self.name} upgraded to {self.state[0]}-{self.state[1]}-{self.state[2]}")     
            if self.state[1] == self.endstate[1]:
                break
        
        while keyboard.is_pressed('ü') is False:
            self.check_for_interface()
            checkLvlUp()
            if self.state[2] < self.endstate[2] and pyautogui.locateOnScreen(r"C:\Users\Marvin\Documents\dev\Uebungen\resource\upgradeAvail.png", region=(1448, 574, 171, 128), grayscale=False, confidence=0.7) != None:
                click(1543, 777) 
                time.sleep(np.random.uniform(1,1.3))
                self.state[2] += 1
                print(f"{self.name} upgraded to {self.state[0]}-{self.state[1]}-{self.state[2]}")     
            if self.state[2] == self.endstate[2]:
                break

