
import cv2 as cv
import numpy as np
import pyautogui
import time

def search(char):
    while True:
        if pyautogui.position() == (0,0):
            break

        screenshot = pyautogui.screenshot("cureentScreen.png")
        screenshot = np.array(screenshot)
        screenshot = screenshot[:, :, ::-1].copy()


        haystack_img = cv.imread("cureentScreen.png", cv.IMREAD_UNCHANGED)
        haystack_img = cv.cvtColor(haystack_img, cv.COLOR_BGR2GRAY)

        scale_percent = 50
        width = int(haystack_img.shape[1] * scale_percent / 100)
        height = int(haystack_img.shape[0] * scale_percent / 100)
        dim = (width, height)
        haystack_img = cv.resize(haystack_img, dim, interpolation = cv.INTER_AREA)

        needle_img = cv.imread(f"assets/{char}.png", cv.IMREAD_UNCHANGED)
        needle_img = cv.cvtColor(needle_img, cv.COLOR_BGR2GRAY)

        scale_percent = 50
        width = int(needle_img.shape[1] * scale_percent / 100)
        height = int(needle_img.shape[0] * scale_percent / 100)
        dim = (width, height)
        needle_img = cv.resize(needle_img, dim, interpolation = cv.INTER_AREA)

        result = cv.matchTemplate(haystack_img, needle_img, cv.TM_CCOEFF_NORMED)
        
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
        if max_val > 0.7:
            pyautogui.moveTo(max_loc[0]*2+10, max_loc[1]*2+10)  # TODO tam ortasını bul
            pyautogui.click()
            pyautogui.click()
            needle_img = cv.imread("assets/lockTR.png", cv.IMREAD_UNCHANGED)
            needle_img = cv.cvtColor(needle_img, cv.COLOR_BGR2GRAY)
            scale_percent = 50
            width = int(needle_img.shape[1] * scale_percent / 100)
            height = int(needle_img.shape[0] * scale_percent / 100)
            dim = (width, height)
            needle_img = cv.resize(needle_img, dim, interpolation = cv.INTER_AREA)

            result = cv.matchTemplate(haystack_img, needle_img, cv.TM_CCOEFF_NORMED)
            
            min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
            pyautogui.moveTo(max_loc[0]*2+10, max_loc[1]*2+10)  # TODO tam ortasını bul
            pyautogui.click()
            quit()
