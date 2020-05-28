from PIL import Image,ImageGrab
import pyautogui
from numpy import asarray
import time
#### for Screen Sort

"""def ss():
    img = ImageGrab.grab().convert('L')
    #img.show()
    return img"""
#ss()

def hit(key):
    pyautogui.keyDown(key)

def isCollied(data):
    for i in range(300,415):
        for j in range(600,650):
            if data[i,j] < 100:
                return True
    return False


print('hey dino game start will 3 seconds')
time.sleep(3)
hit('up')
while True:
    #img = ss()
    #print(asarray(img))
    img = ImageGrab.grab().convert('L')
    data = img.load()
    if isCollied(data):
        hit('up')
    for i in range(300,415):
       for j in range(600,650):
          data[i,j] = 0
    #
    # img.show()
    break