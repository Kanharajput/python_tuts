import pyautogui
from PIL import Image ,ImageGrab
import time 
global data

def hit(key):
    pyautogui.keyDown(key)
    return

def iscollide(data):
        for i in range(310,390):
            for j in range (490,540):
                if data[i ,j] < 100:
                    hit("up")
                    return

if __name__=="__main__":
    print("game is stariting hold the sit belts")
    time.sleep(3)
    pyautogui.press("enter")
    while True:    
        image=ImageGrab.grab().convert('L')
        data=image.load()
        iscollide(data)
        

    #image.show() 

