from selenium import webdriver
from selenium.webdriver.common.keys import  Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get("http://www.python.org")

# print(driver.title)


# assert "Python" in driver.title
