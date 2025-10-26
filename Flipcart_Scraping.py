from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Edge()

driver.get('https://www.flipkart.com/')

search = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/header/div[1]/div[2]/form/div/div/input')
search.send_keys(Keys="watch")