from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from urls.generals import *
from urls.credentials import *
from classes.Login import Login

#Set up chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#Define all classes
Login = Login(driver, LOGIN_URL, USERNAME, PASSWORD)



