from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.randomtime import random_time
from datetime import datetime

class Explore: 
    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver

    def go_explore(self, url:str, click_times:int):
        """Explore given area for a given number of clicks"""
        try:
            if self.driver: 
                self.driver.get(url)
                random_time(0.1, 0.2)
                self.driver.refresh()
                random_time(1, 3)
                explore_button = self.driver.find_element(By.CSS_SELECTOR, "div#exploreconsole.explorebtn.disable-select")
                count = 0
                while count < click_times:
                    explore_button.click()
                    random_time(0.03, 0.08)
                    count += 1
                    print(f"[{datetime.now()}]: Button is clicked {count} time(s)")
            else:
                print(f"[{datetime.now()}]: WebDriver is not found")
        except Exception as e:
            print(f"[{datetime.now()}]: Exception {e} has occurred")
        
        
        