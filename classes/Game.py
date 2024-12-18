from selenium import webdriver
from classes.Login import Login
from classes.Explore import Explore
from classes.Fishing import Fishing
from urls.generals import *
from datetime import datetime


class Game: 
    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver
        self.login_bot = Login(driver)
        self.explore_bot = Explore(driver)
        self.fish_bot = Fishing(driver)

    def login(self, url, username, password):
        self.login_bot.signin(url, username, password)
    
    def explore(self, url:str, click_times:int): 
        self.explore_bot.go_explore(url, click_times)

    def start_fishing(self, url:str):
        fish_image_path = "../utils/images/fish.png" 
        self.fish_bot.start_fishing(url, fish_image_path)

    def quit(self):
        if self.driver: 
            self.driver.quit()
            print(f'[{datetime.now()}]: Session closed')


    