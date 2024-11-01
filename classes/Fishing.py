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
        self.browser_rect = self.driver.get_window_rect()
    
    def capture_screenshot(self): 
        # Get the size and location of the browser window
        # Take browser screen shot
        screenshot = pyautogui.screenshot()
        # Convert to np array
        screenshot_np = np.array(screenshot)
        cropped_screenshot = screenshot_np[
            self.browser_rect['y']:self.browser_rect['y'] + self.browser_rect['height'],
            self.browser_rect['x']:self.browser_rect['x'] + self.browser_rect['width']
        ]

        return cropped_screenshot

    def detect_fish(self, screenshot, src_image): 
        fish_image = cv2.imread(src_image, cv2.IMREAD_COLOR)

        result = cv2.matchTemplate(screenshot, fish_image, cv2.TM_CCOEFF_NORMED)

        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        threshold = 0.8
        
        if max_val >= threshold:
            return max_loc
        else:
            return None

    def click_fish(self, fish_position): 
        screen_x = self.browser_rect['x'] + fish_position[0]
        screen_y = self.browser_rect['y'] + fish_position[1]

        pyautogui.click(screen_x, screen_y)

    def perform_fishing(self, fish_image_path, timeout): 

        start_time = time.time()

        while time.time() - start_time < timeout:
            screenshot = self.capture_screenshot()

            fish_position = self.detect_fish(screenshot, fish_image_path)

            if fish_position:
                print(f'Fish found a {fish_position}, clicking!')
                self.click_fish(fish_position)
                break
            else:
                print(f'Fish not found, retrying')
            
            time.sleep(0.1)

    def start_fishing(self, url, fish_image_path, timeout=3):
        self.driver.get(url)
        random_time(0.1, 0.5)
        self.driver.refresh()
        random_time(0.1, 0.5)

        self.perform_fishing(fish_image_path, timeout)
        
        #Adding fish times later...  
        

        