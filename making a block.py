import pyautogui
from PIL import Image ,ImageGrab
import time
time.sleep(1)
#pyautogui.keyDown("up")
image=ImageGrab.grab().convert('L')
data=image.load()
for i in range(310,390):
        for j in range (490,540):
            data[i ,j] =0

image.show()