from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.randomtime import random_time
from datetime import datetime

class Login:
    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver
    
    #Main function to sign user in
    def signin(self, url:str, username:str, password:str):
        """Sign user into the game"""
        try:
            if self.driver:
                self.driver.get(url)
                random_time(2, 4)
                self.driver.find_element(By.NAME, "username").send_keys(username)
                random_time(0.1, 0.3)
                self.driver.find_element(By.NAME, "password").send_keys(password)
                random_time(0.2, 0.3)
                self.driver.find_element(By.CSS_SELECTOR, "input#login_sub.button.btngreen").click()
                
                #print as log
                print(f'[{datetime.now()}]: Logged in as {username}')
            else:
                print(f'[{datetime.now()}]: There is a problem starting the browser')
        except Exception as exception:
            print(f'[{datetime.now()}]: Exception occurred: {exception}')
        
