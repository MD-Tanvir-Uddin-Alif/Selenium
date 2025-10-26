from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Edge()

driver.get('https://www.flipkart.com/')


#searing the product
input_search = driver.find_element(By.XPATH, '//input[@name="q"]')
input_search.send_keys("smart watches")
input_search.send_keys(Keys.ENTER)


#wait until the page loded
WebDriverWait(driver, 20).until(
    lambda d: d.execute_script("return document.readyState") == "complete"
)


#Loded all the product cad of the page
All_watches_Card = driver.find_elements(By.XPATH, '//div[@class="_75nlfW LYgYA3"]')


for index, Watch_single_card in enumerate(All_watches_Card, 1):
    # watch_image = Watch_single_card.find_element(By.XPATH, './/a[@class="rPDeLR"]').get_attribute('href')
    link = Watch_single_card.find_element(By.XPATH, './/a').get_attribute('href')
    
    print(f'-----------------------------------{index}---------------------')
    print(link)
