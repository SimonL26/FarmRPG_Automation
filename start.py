from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

#Set up chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get(f"https://farmrpg.com/index.php#!/login.php")
time.sleep(0.5)
driver.find_element(By.NAME, "username").send_keys("CustardMustard")
time.sleep(0.3)
driver.find_element(By.NAME, "password").send_keys("05bnr3sa")
time.sleep(0.7)
driver.find_element(By.CSS_SELECTOR, "input#login_sub.button.btngreen").click()

time.sleep(4)
