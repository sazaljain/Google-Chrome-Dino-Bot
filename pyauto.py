import pyautogui
from PIL import Image, ImageGrab
import time


def test(data):

    if data[220, 200] > (230):
        for i in range(250, 325):
            for j in range(455, 475):
                if data[i, j] < 90:
                    pyautogui.press('up')
                    # pyautogui.keyUp('up')
                    return True
      # For Birds
        for i in range(240, 300):
            for j in range(390, 410):
                if data[i, j] < 90:
                    pyautogui.keyDown('down')
                    time.sleep(0.05)
                    pyautogui.keyUp('down')
                    return True
    else:
        for i in range(250, 325):
            for j in range(455, 475):
                if data[i, j] > 169:
                    pyautogui.press('up')
                    # pyautogui.keyUp('up')
                    return True
      # For Birds
        for i in range(240, 300):
            for j in range(390, 410):
                if data[i, j] > 169:
                    pyautogui.keyDown('down')
                    time.sleep(0.05)
                    pyautogui.keyUp('down')
                    return True
    return False


print("Hey.. Dino game about to start in 2 seconds")
time.sleep(2)

while True:
    image = ImageGrab.grab().convert('L')
    data = image.load()
    test(data)

    # for i in range(250, 300):
    #     for j in range(455, 475):
    #         data[i, j] = 0

    # image.show()
    # break
