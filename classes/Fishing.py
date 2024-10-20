import time
import cv2
import numpy as np
from selenium import webdriver
from PIL import Image
import pyautogui
from utils.randomtime import random_time

class Fishing: 
    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver 
    
    def capture_screenshot(self): 
        # Get the size and location of the browser window
        browser_rect = self.driver.get_window_rect()
        # Take browser screen shot
        screenshot = pyautogui.screenshot()
        # Convert to np array
        screenshot_np = np.array(screenshot)
        cropped_screenshot = screenshot_np[
            browser_rect['y']:browser_rect['y'] + browser_rect['height'],
            browser_rect['x']:browser_rect['x'] + browser_rect['width']
        ]

        return cropped_screenshot

    def detect_fish(self, screenshot, src_image): 
        fish_image = cv2.imread(src_image, cv2.IMREAD_COLOR)

        result = cv2.matchTemplate(screenshot, fish_image, cv2.TM_CCOEFF_NORMED)

        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        threshold = 0.8