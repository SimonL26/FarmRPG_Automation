from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.randomtime import random_time
class Explore: 
    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver

    def go_explore(self, url:str):
        self.driver.get(url)
        random_time(1, 3)
        self.driver.find_element(By.CSS_SELECTOR, "div#exploreconsole.explorebtn.disable-select").click()
        random_time(0.01, 0.02)
        