from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time



options = Options()
options.add_argument("--incognito")

driver = webdriver.Chrome(options=options)
driver.get('https://www.linkedin.com/')

time.sleep(2)

signIn_Button = driver.find_element(By.XPATH, '/html/body/nav/div/a[1]').click()

time.sleep(3)

email = 'mdtanviruddinalif@gmail.com'
password = 'dummy2345'

send_emil = driver.find_element(By.XPATH, '//*[@id="username"]')
time.sleep(1.1)
send_emil.send_keys(email)
time.sleep(1.8)
send_emil.send_keys(Keys.ENTER)
time.sleep(2.7)

send_password = driver.find_element(By.XPATH, '//*[@id="password"]')
time.sleep(1.3)
send_password.send_keys(password)
time.sleep(2.3)
send_password.send_keys(Keys.ENTER)
time.sleep(2.8)

search_bar = driver.find_element(By.XPATH, '//*[@id="global-nav-search"]/div/button/span/svg')
time.sleep(1.5)
search_bar.send_keys("#itclanbd", Keys.ENTER)

