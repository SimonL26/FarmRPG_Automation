from selenium import webdriver
from classes.Login import Login
from urls.credentials import *
from urls.generals import *
from datetime import datetime

class Game: 
    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver
        self.login_bot = Login(driver)

    def login(self, url, username, password):
        self.login_bot.signin(url, username, password)

    def quit(self):
        if self.driver: 
            self.driver.quit()
            print(f'[{datetime.now()}]: Session closed')