from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Edge()

driver.get('https://www.flipkart.com/')

input_search = driver.find_element(By.XPATH, '//input[@name="q"]')
input_search.send_keys("smart watches")
input_search.send_keys(Keys.ENTER)

time.sleep(2)  

product_card = driver.find_elements(By.XPATH, '//div[@class="_1sdMkc LFEi7Z"]')
print(len(product_card))

for index, product in enumerate(product_card, 1):
    try:
        link = product.find_element(By.XPATH, './/a').get_attribute('href')
        print(f'Opening product {index}: {link}')

        driver.execute_script("window.open(arguments[0], '_blank');", link)
        driver.switch_to.window(driver.window_handles[1])

        print(driver.title)

        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)
    except Exception as e:
        print(f"Skipping product {index} due to error: {e}")
