from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import random
import json
import time
import os


# Behavior finctions
from behavior_function import human_delay, human_click
# from shopee_scraper import simulate_human_behavior



#credential
load_dotenv()

email=os.getenv('shoppy_mail')
password=os.getenv('shoppy_password')



# options = Options()
options = uc.ChromeOptions()
# options.add_argument(r"--user-data-dir=C:\Users\User\AppData\Local\Google\Chrome\User Data")
# options.add_argument("--profile-directory=Profile 3")
options.add_argument('--disable-blink-features=AutomationControlled')


# driver = webdriver.Chrome(options=options)
driver = uc.Chrome(options=options)
driver.get('https://shopee.sg')
driver.maximize_window()
WebDriverWait(driver, 5).until(
    lambda d: d.execute_script("return document.readyState") == "complete"
)

# time.sleep(1.5)


# Login to shoppy
user_mail_imput = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/form/div[1]/div[1]/input'))
)
human_click(driver, user_mail_imput)
human_delay(0.5, 2)
for char in email:
    user_mail_imput.send_keys(char)
    time.sleep(random.uniform(0.05,0.2))
user_mail_imput.click()
time.sleep(0.5)


user_password_imput = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/form/div[2]/div[1]/input'))
)
human_click(driver, user_password_imput)
for char in password:
    user_password_imput.send_keys(char)
    time.sleep(random.uniform(0.05, 0.2))
user_password_imput.click()
time.sleep(0.8)


login_button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/form/button'))
)
human_click(driver, login_button)




driver.quit()
time.sleep(10)







