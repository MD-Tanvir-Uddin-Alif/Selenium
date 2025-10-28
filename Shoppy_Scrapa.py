from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from dotenv import load_dotenv


# Behavior finctions
from behavior_function import human_delay, random_short_delay, random_long_delay ,human_scroll, human_click, move_mouse_randomly, act_like_human, setup_human_browser



#credential
load_dotenv()

email=os.getenv('shoppy_mail')
password=os.getenv('shoppy_password')


driver = webdriver.Edge()
driver.get('https://shopee.sg/buyer/login?fu_tracking_id=58372aa6363-9433-408e-910e-b12ae64b270d&next=https%3A%2F%2Fshopee.sg%2F')
driver.maximize_window()
human_delay()
# move_mouse_randomly(driver)


# Login to shoppy
user_mail_imput = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/form/div[1]/div[1]/input'))
)
human_delay()
human_click(driver, user_mail_imput)
random_short_delay()
user_mail_imput.send_keys(email)
user_mail_imput.click()
human_delay()


user_password_imput = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/form/div[2]/div[1]/input'))
)
human_delay()
human_click(driver, user_password_imput)
random_short_delay()
user_password_imput.send_keys(password)
user_password_imput.click()
human_delay()


login_button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/form/button'))
)
login_button.send_keys(Keys.ENTER)


WebDriverWait(driver, 20).until(
    lambda d: d.execute_script("return document.readyState") == "complete"
)
