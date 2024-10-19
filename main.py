from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from urls.generals import *
from classes.Game import Game
from classes.GUI import GUI

#Set up chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#get game set up
game = Game(driver)
app = GUI(game)

#Run 
app.run()

