import pyautogui
import random
import time
import sys

time.sleep(6)#gives you time to click the right window

try:
    while True:    
        x = random.randint(239, 1536)#randomizes the position of the mouse

        pyautogui.moveTo(x,663)      #moves the mouse to position

        pyautogui.doubleClick()      #fires the gun in game twise   

        time.sleep(30); pyautogui.doubleClick()#gives time for the game to 
                                              #catch up with the mouse and fires gun
        # pyautogui.doubleClick()     #fires gun twice again                                

except KeyboardInterrupt:
    sys.exit()
