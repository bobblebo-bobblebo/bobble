#pip install pyautogui
#pip install keyboard
import pyautogui
import time
import keyboard

if __name__ =  "__main__":

    play = True
    while  play = True:

        if keyboard.is_pressed("shift"):
            time.sleep(0.5)

            while True:
                x,y=pyautogui.position()
                pyautogui.moveTo(x,y)
                #time.sleep(0.005)

                if keyboard.is_pressed("shift"):
                    time.sleep(0.5)

                if keyboard.is_pressed("esc"):
                    play=False
                    break