from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Edge()

driver.get('https://www.flipkart.com/')


input_search = driver.find_element(By.XPATH, '//input[@name="q"]')
input_search.send_keys("smart watches")
input_search.send_keys(Keys.ENTER)

All_watches_Card = driver.find_elements(By.XPATH, '//div[@class="_75nlfW LYgYA3"]')

for index, card in enumerate(All_watches_Card, 1):
    print(f'-------------------- Card {index} --------------------')
    watch_images = card.find_elements(By.XPATH, './/img')
    for i, image in enumerate(watch_images[0], 1):
        w_i = image.get_attribute('src')
        if 'https://static-assets-web.flixcart.com/fk-p-linchpin-web/fk-cp-zion/img/fa_9e47c1.png' in w_i:
            continue
        print(f"Image {i}: {w_i}") 


# for index, card in enumerate(All_watches_Card, 1):
#     print(f'-------------------- Card {index} --------------------')
#     watch_images = card.find_elements(By.XPATH, './/img')
    
#     if watch_images:  
#         first_image = watch_images[0].get_attribute('src')
#         print(f"First Image: {first_image}")

product_Card = driver.find_elements()

for product in product_Card:
    