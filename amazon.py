from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES

driver = webdriver.Edge()


driver.get("https://www.amazon.com/")

driver.find_element.until(
    ES.presence_of_all_elements_located(By.CLASS_NAME, 'a-button-text')
)


driver.find_element(By.CLASS_NAME, 'a-button-text')

html_template = driver.page_source

print(html_template)